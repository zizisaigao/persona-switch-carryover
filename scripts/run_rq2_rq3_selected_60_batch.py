from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys
from datetime import datetime
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.main import build_client, score_batch, _resolve_model_config
from src.models.cache import RequestCache
from src.runner.batch_run import _load_existing_keys, run_batch
from src.scoring import score_mbti
from src.scoring.score_machine_mindset import build_reference_bank
from src.utils.config import get_project_root, load_all_configs
from src.utils.ids import make_run_id
from src.utils.io import load_samples, write_jsonl
from src.utils.logging import configure_logging
from scripts.rq2_rq3_selected_60_plan import (
    DATASETS,
    DATASET_SAMPLE_LIMITS,
    RQ2_CONDITIONS,
    RQ2_BATCH2_PAIRS,
    RQ2_PAIRS,
    RQ2_PREMISE_MBTI,
    RQ3_CONDITIONS,
    RQ3_BATCH2_PAIRS,
    RQ3_PAIRS,
)


class ProgressReporter:
    def __init__(self, log_path: Path, status_path: Path) -> None:
        self.log_path = log_path
        self.status_path = status_path
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self._handle = self.log_path.open("a", encoding="utf-8", buffering=1)

    def write(self, message: str) -> None:
        line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
        self._handle.write(line + "\n")
        self._handle.flush()
        self.status_path.write_text(line + "\n", encoding="utf-8")
        print(line, flush=True)

    def close(self) -> None:
        self._handle.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Single-process resumable RQ2/RQ3 batch runner.")
    parser.add_argument("--model-config", default="gemini_flash_lite")
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--gemini-api-key", default="")
    parser.add_argument("--pair-batch", type=int, choices=[1, 2], default=1)
    parser.add_argument("--skip-rq2-premise", action="store_true")
    parser.add_argument("--skip-rq2", action="store_true")
    parser.add_argument("--skip-rq3", action="store_true")
    return parser.parse_args()


def main() -> None:
    logger = configure_logging()
    args = parse_args()
    project_root = get_project_root()
    progress_timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    progress_dir = project_root / "outputs" / "logs"
    batch_tag = f"batch{args.pair_batch}"
    progress_log_path = progress_dir / f"run_rq2_rq3_selected_60_{batch_tag}_progress_{progress_timestamp}.log"
    progress_status_path = progress_dir / f"run_rq2_rq3_selected_60_{batch_tag}_progress_{progress_timestamp}.status.txt"
    latest_log_path = progress_dir / f"run_rq2_rq3_selected_60_{batch_tag}_progress_latest.log"
    latest_status_path = progress_dir / f"run_rq2_rq3_selected_60_{batch_tag}_progress_latest.status.txt"
    reporter = ProgressReporter(progress_log_path, progress_status_path)
    configs = load_all_configs(project_root)
    experiments = configs["experiments"]
    paths_config = experiments["paths"]

    try:
        latest_log_path.write_text(str(progress_log_path) + "\n", encoding="utf-8")
        latest_status_path.write_text(str(progress_status_path) + "\n", encoding="utf-8")

        if args.gemini_api_key:
            os.environ["GEMINI_API_KEY"] = args.gemini_api_key

        experiments["runtime"]["resume"] = True
        model_config = _resolve_model_config(configs["models"], False, args.model_config, args.model_name)
        client = build_client(model_config)
        cache = RequestCache(project_root / paths_config["cache_dir"])
        usage_log_path = project_root / paths_config["api_usage_log"]
        raw_output_path = project_root / paths_config["raw_generations"]
        scored_dir = project_root / paths_config["scored_dir"]
        scored_dir.mkdir(parents=True, exist_ok=True)
        embedding_cache_dir = project_root / "outputs" / "embedding_cache"
        reference_bank = build_reference_bank(project_root / "data" / "processed" / "machine_mindset_labeled.parquet")

        sample_cache = {
            dataset: load_samples(project_root / dataset)[: DATASET_SAMPLE_LIMITS[dataset]]
            for dataset in DATASETS
        }
        existing_keys = _load_existing_keys(raw_output_path)
        logger.info("Preloaded %s existing resume keys from %s", len(existing_keys), raw_output_path)

        plan = build_plan(
            pair_batch=args.pair_batch,
            include_rq2_premise=not args.skip_rq2_premise,
            include_rq2=not args.skip_rq2,
            include_rq3=not args.skip_rq3,
        )
        reporter.write(
            f"START pair_batch={args.pair_batch} total_specs={len(plan)} preloaded_resume_keys={len(existing_keys)} model={model_config['model_name']}"
        )

        completed_specs = 0
        skipped_specs = 0
        produced_records = 0

        for index, spec in enumerate(plan, start=1):
            dataset = spec["dataset"]
            samples = sample_cache[dataset]
            run_id = make_run_id("persona")
            stage = _infer_stage(spec["condition"])
            reporter.write(
                f"[{index}/{len(plan)}] stage={stage} condition={spec['condition']} "
                f"persona_a={spec['persona_a']} persona_b={spec['persona_b']} dataset={dataset}"
            )
            logger.info(
                "[%s/%s] condition=%s persona_a=%s persona_b=%s dataset=%s",
                index,
                len(plan),
                spec["condition"],
                spec["persona_a"],
                spec["persona_b"],
                dataset,
            )
            records = run_batch(
                samples=samples,
                condition_name=spec["condition"],
                persona_a=spec["persona_a"],
                persona_b=spec["persona_b"],
                experiments_config=experiments,
                personas_config=configs["personas"],
                model_config=model_config,
                client=client,
                cache=cache,
                usage_log_path=usage_log_path,
                raw_output_path=raw_output_path,
                run_id=run_id,
                existing_keys=existing_keys,
                max_samples_override=DATASET_SAMPLE_LIMITS[dataset],
            )
            if not records:
                skipped_specs += 1
                reporter.write(
                    f"[{index}/{len(plan)}] SKIPPED condition={spec['condition']} "
                    f"persona_a={spec['persona_a']} persona_b={spec['persona_b']} dataset={dataset}"
                )
                logger.info("[%s/%s] skipped; all samples already completed", index, len(plan))
                continue

            scored_records = score_batch(
                records,
                samples,
                project_root=project_root,
                reference_bank=reference_bank,
                embedding_cache_dir=embedding_cache_dir,
            )
            write_jsonl(scored_dir / f"{run_id}_scores.jsonl", scored_records)
            mbti_profiles = score_mbti.aggregate_profiles(scored_records)
            if mbti_profiles:
                write_jsonl(project_root / "outputs" / "tables" / f"{run_id}_mbti_profiles.jsonl", mbti_profiles)

            completed_specs += 1
            produced_records += len(records)
            reporter.write(
                f"[{index}/{len(plan)}] COMPLETED run_id={run_id} new_records={len(records)} "
                f"scored_records={len(scored_records)} completed_specs={completed_specs} skipped_specs={skipped_specs}"
            )
            logger.info(
                "[%s/%s] completed run_id=%s new_records=%s scored_records=%s",
                index,
                len(plan),
                run_id,
                len(records),
                len(scored_records),
            )

        reporter.write(
            f"FINISHED completed_specs={completed_specs} skipped_specs={skipped_specs} "
            f"produced_records={produced_records} total_specs={len(plan)}"
        )
        logger.info(
            "Continuation finished. completed_specs=%s skipped_specs=%s produced_records=%s total_specs=%s",
            completed_specs,
            skipped_specs,
            produced_records,
            len(plan),
        )
    finally:
        reporter.close()


def build_plan(*, pair_batch: int, include_rq2_premise: bool, include_rq2: bool, include_rq3: bool) -> list[dict[str, str]]:
    plan: list[dict[str, str]] = []
    rq2_pairs = RQ2_PAIRS if pair_batch == 1 else RQ2_BATCH2_PAIRS
    rq3_pairs = RQ3_PAIRS if pair_batch == 1 else RQ3_BATCH2_PAIRS
    if include_rq2_premise:
        for persona in RQ2_PREMISE_MBTI:
            for dataset in DATASETS:
                plan.append(
                    {
                        "condition": "MBTI_only_strong",
                        "persona_a": persona,
                        "persona_b": persona,
                        "dataset": dataset,
                    }
                )
    if include_rq2:
        for pair in rq2_pairs:
            for condition in RQ2_CONDITIONS:
                for dataset in DATASETS:
                    plan.append(
                        {
                            "condition": condition,
                            "persona_a": pair["A"],
                            "persona_b": pair["B"],
                            "dataset": dataset,
                        }
                    )
    if include_rq3:
        for pair in rq3_pairs:
            for condition in RQ3_CONDITIONS:
                for dataset in DATASETS:
                    plan.append(
                        {
                            "condition": condition,
                            "persona_a": pair["A"],
                            "persona_b": pair["B"],
                            "dataset": dataset,
                        }
                    )
    return plan


def _infer_stage(condition: str) -> str:
    if condition == "MBTI_only_strong":
        return "rq2_strong_premise"
    if condition.endswith("_strong"):
        return "rq2_pairs"
    return "rq3_pairs"


if __name__ == "__main__":
    main()
