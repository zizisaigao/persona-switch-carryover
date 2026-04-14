from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.rq2_rq3_selected_60_plan import (
    DATASETS,
    DATASET_SAMPLE_LIMITS,
    RQ2_STRONG_PREMISE_RERUN_13,
)
from src.main import _resolve_model_config, build_client, score_batch
from src.models.cache import RequestCache
from src.runner.batch_run import run_batch
from src.scoring import score_mbti
from src.scoring.score_machine_mindset import build_reference_bank
from src.utils.config import get_project_root, load_all_configs
from src.utils.ids import make_run_id
from src.utils.io import load_samples, write_jsonl
from src.utils.logging import configure_logging


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
    parser = argparse.ArgumentParser(description="Single-process rerun for 13 RQ2 strong premise MBTI.")
    parser.add_argument("--model-config", default="gemini_flash_lite")
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--gemini-api-key", default="")
    return parser.parse_args()


def build_plan() -> list[dict[str, str]]:
    plan: list[dict[str, str]] = []
    for persona in RQ2_STRONG_PREMISE_RERUN_13:
        for dataset in DATASETS:
            plan.append(
                {
                    "condition": "MBTI_only_strong",
                    "persona_a": persona,
                    "persona_b": persona,
                    "dataset": dataset,
                }
            )
    return plan


def main() -> None:
    logger = configure_logging()
    args = parse_args()
    project_root = get_project_root()
    progress_dir = project_root / "outputs" / "logs"
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    progress_log_path = progress_dir / f"run_rq2_strong_premise_rerun_13_progress_{timestamp}.log"
    progress_status_path = progress_dir / f"run_rq2_strong_premise_rerun_13_progress_{timestamp}.status.txt"
    latest_log_path = progress_dir / "run_rq2_strong_premise_rerun_13_progress_latest.log"
    latest_status_path = progress_dir / "run_rq2_strong_premise_rerun_13_progress_latest.status.txt"
    reporter = ProgressReporter(progress_log_path, progress_status_path)
    configs = load_all_configs(project_root)
    experiments = configs["experiments"]
    paths_config = experiments["paths"]

    try:
        latest_log_path.write_text(str(progress_log_path) + "\n", encoding="utf-8")
        latest_status_path.write_text(str(progress_status_path) + "\n", encoding="utf-8")

        if args.gemini_api_key:
            os.environ["GEMINI_API_KEY"] = args.gemini_api_key

        experiments["runtime"]["resume"] = False
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
        plan = build_plan()
        reporter.write(
            f"START total_specs={len(plan)} model={model_config['model_name']} personas={len(RQ2_STRONG_PREMISE_RERUN_13)}"
        )

        completed_specs = 0
        produced_records = 0
        for index, spec in enumerate(plan, start=1):
            dataset = spec["dataset"]
            samples = sample_cache[dataset]
            run_id = make_run_id("persona")
            reporter.write(
                f"[{index}/{len(plan)}] condition={spec['condition']} persona={spec['persona_a']} dataset={dataset}"
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
                existing_keys=set(),
                max_samples_override=DATASET_SAMPLE_LIMITS[dataset],
            )
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
                f"[{index}/{len(plan)}] COMPLETED run_id={run_id} new_records={len(records)} scored_records={len(scored_records)} completed_specs={completed_specs}"
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
            f"FINISHED completed_specs={completed_specs} produced_records={produced_records} total_specs={len(plan)}"
        )
    finally:
        reporter.close()


if __name__ == "__main__":
    main()
