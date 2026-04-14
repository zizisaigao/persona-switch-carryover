from __future__ import annotations

import argparse
import csv
import json
import random
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from src.models.cache import RequestCache
from src.models.gemini_client import GeminiClient
from src.models.mock_client import MockClient
from src.models.openrouter_client import OpenRouterClient
from src.runner.batch_run import run_batch
from src.scoring import score_ifeval, score_mbti
from src.scoring.score_machine_mindset import (
    DEFAULT_EMBEDDING_MODEL,
    active_persona_for_condition,
    build_reference_bank,
    score_dimension_response,
    score_self_awareness_response,
)
from src.utils.config import get_project_root, load_all_configs
from src.utils.ids import make_run_id
from src.utils.io import load_samples, write_jsonl
from src.utils.logging import configure_logging
from src.utils.schema import ExperimentSample


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Persona switching experiment runner.")
    parser.add_argument("--condition", type=str, default=None, help="Condition name from configs/experiments.yaml")
    parser.add_argument("--persona-a", type=str, default=None, help="Warm-up / persona A label")
    parser.add_argument("--persona-b", type=str, default=None, help="Evaluation persona B label")
    parser.add_argument(
        "--model-config",
        type=str,
        default=None,
        help="Named model preset from configs/models.yaml. Defaults to default_model or mock_model.",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default=None,
        help="Optional direct override for the resolved model name.",
    )
    parser.add_argument("--mock", action="store_true", help="Use mock model client")
    parser.add_argument("--no-mock", action="store_true", help="Force real provider even if config default enables mock mode")
    parser.add_argument("--no-resume", action="store_true", help="Disable resumable skipping for this run")
    parser.add_argument("--max-samples", type=int, default=None, help="Override budget max samples")
    parser.add_argument("--samples-file", type=str, default=None, help="Override sample dataset path (.csv or .jsonl)")
    parser.add_argument("--samples-csv", type=str, default=None, help="Deprecated alias for --samples-file")
    parser.add_argument(
        "--sample-ids-file",
        type=str,
        default=None,
        help="Optional newline-delimited, CSV, or JSONL file listing sample_ids to keep.",
    )
    parser.add_argument(
        "--sample-seed",
        type=int,
        default=None,
        help="Optional shuffle seed applied before truncating to max samples.",
    )
    parser.add_argument(
        "--trials-per-sample",
        type=int,
        default=None,
        help="Override experiment.trials_per_sample for repeat runs.",
    )
    return parser.parse_args()


def main() -> None:
    logger = configure_logging()
    load_dotenv()
    args = parse_args()
    project_root = get_project_root()
    configs = load_all_configs(project_root)

    experiments = configs["experiments"]
    experiment_defaults = experiments["experiment"]
    paths_config = experiments["paths"]

    condition_name = args.condition or experiment_defaults["default_condition"]
    persona_a = args.persona_a or experiment_defaults["default_persona_a"]
    persona_b = args.persona_b or experiment_defaults["default_persona_b"]

    if condition_name not in experiments["conditions"]:
        raise KeyError(f"Unknown condition: {condition_name}")

    mock_mode = bool(experiments["runtime"].get("mock_mode", False))
    if args.mock:
        mock_mode = True
    if args.no_mock:
        mock_mode = False
    model_config = _resolve_model_config(configs["models"], mock_mode, args.model_config, args.model_name)
    samples_path_arg = args.samples_file or args.samples_csv
    samples_path = Path(samples_path_arg) if samples_path_arg else project_root / paths_config["samples_csv"]

    if args.trials_per_sample is not None:
        experiments["experiment"]["trials_per_sample"] = args.trials_per_sample
    if args.no_resume:
        experiments["runtime"]["resume"] = False
    effective_trials = int(experiments["experiment"]["trials_per_sample"])

    client = build_client(model_config)
    cache_enabled = bool(experiments["runtime"].get("use_cache", True))
    if effective_trials > 1:
        cache_enabled = False
    cache = RequestCache(project_root / paths_config["cache_dir"]) if cache_enabled else None
    usage_log_path = project_root / paths_config["api_usage_log"]
    raw_output_path = project_root / paths_config["raw_generations"]

    samples = load_samples(samples_path)
    samples, selection_applied = _select_samples(
        samples=samples,
        max_samples=args.max_samples,
        sample_seed=args.sample_seed,
        sample_ids_path=Path(args.sample_ids_file) if args.sample_ids_file else None,
        default_limit=int(experiments["budget"].get("max_samples_per_run", len(samples))),
    )
    if selection_applied:
        experiments["budget"]["max_samples_per_run"] = len(samples)
    run_id = make_run_id("persona")

    logger.info(
        "Starting run_id=%s condition=%s persona_a=%s persona_b=%s mock=%s model=%s samples=%s trials=%s cache=%s",
        run_id,
        condition_name,
        persona_a,
        persona_b,
        mock_mode,
        model_config["model_name"],
        len(samples),
        effective_trials,
        cache_enabled,
    )

    records = run_batch(
        samples=samples,
        condition_name=condition_name,
        persona_a=persona_a,
        persona_b=persona_b,
        experiments_config=experiments,
        personas_config=configs["personas"],
        model_config=model_config,
        client=client,
        cache=cache,
        usage_log_path=usage_log_path,
        raw_output_path=raw_output_path,
        run_id=run_id,
    )

    scored_records = score_batch(records, samples, project_root=project_root)
    scored_output = project_root / paths_config["scored_dir"] / f"{run_id}_scores.jsonl"
    write_jsonl(scored_output, scored_records)
    mbti_profiles = score_mbti.aggregate_profiles(scored_records)
    if mbti_profiles:
        profile_output = project_root / "outputs" / "tables" / f"{run_id}_mbti_profiles.jsonl"
        write_jsonl(profile_output, mbti_profiles)

    logger.info(
        "Completed run_id=%s new_records=%s scored_records=%s raw_output=%s",
        run_id,
        len(records),
        len(scored_records),
        raw_output_path,
    )


def build_client(model_config: dict[str, Any]):
    provider = model_config["provider"]
    if provider == "mock":
        return MockClient()
    if provider == "gemini":
        return GeminiClient(
            api_key_env=model_config["api_key_env"],
            timeout_seconds=int(model_config.get("timeout_seconds", 60)),
            max_retries=int(model_config.get("max_retries", 3)),
        )
    if provider == "openrouter":
        return OpenRouterClient(
            api_key_env=model_config["api_key_env"],
            timeout_seconds=int(model_config.get("timeout_seconds", 60)),
            max_retries=int(model_config.get("max_retries", 3)),
        )
    raise ValueError(f"Unsupported provider: {provider}")


def _resolve_model_config(
    model_configs: dict[str, dict[str, Any]],
    mock_mode: bool,
    model_config_name: str | None,
    model_name_override: str | None,
) -> dict[str, Any]:
    resolved_name = model_config_name or ("mock_model" if mock_mode else "default_model")
    if resolved_name not in model_configs:
        raise KeyError(f"Unknown model config: {resolved_name}")
    model_config = dict(model_configs[resolved_name])
    if model_name_override:
        model_config["model_name"] = model_name_override
    return model_config


def _select_samples(
    *,
    samples: list[ExperimentSample],
    max_samples: int | None,
    sample_seed: int | None,
    sample_ids_path: Path | None,
    default_limit: int,
) -> tuple[list[ExperimentSample], bool]:
    selection_applied = bool(sample_ids_path or sample_seed is not None or max_samples is not None)
    if not selection_applied:
        return samples, False

    selected = list(samples)
    if sample_ids_path is not None:
        selected = _filter_samples_by_id(selected, sample_ids_path)

    if sample_seed is not None:
        random.Random(sample_seed).shuffle(selected)

    if max_samples is not None:
        limit = max_samples
    elif sample_ids_path is not None:
        limit = len(selected)
    else:
        limit = default_limit
    if limit >= 0:
        selected = selected[:limit]
    return selected, True


def _filter_samples_by_id(samples: list[ExperimentSample], sample_ids_path: Path) -> list[ExperimentSample]:
    selected_ids = _load_sample_ids(sample_ids_path)
    if not selected_ids:
        return []
    order = {sample_id: index for index, sample_id in enumerate(selected_ids)}
    filtered = [sample for sample in samples if sample.sample_id in order]
    filtered.sort(key=lambda sample: order[sample.sample_id])
    return filtered


def _load_sample_ids(path: Path) -> list[str]:
    suffix = path.suffix.lower()
    if suffix == ".jsonl":
        sample_ids: list[str] = []
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                sample_id = record.get("sample_id")
                if sample_id not in (None, ""):
                    sample_ids.append(str(sample_id))
        return sample_ids
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return [str(row["sample_id"]) for row in reader if row.get("sample_id")]
    with path.open("r", encoding="utf-8") as handle:
        return [line.strip() for line in handle if line.strip()]


def score_batch(
    records: list[dict[str, Any]],
    samples: list[ExperimentSample],
    *,
    project_root: Path,
    reference_bank: dict[str, Any] | None = None,
    embedding_cache_dir: Path | None = None,
) -> list[dict[str, Any]]:
    by_id = {sample.sample_id: sample for sample in samples}
    scored: list[dict[str, Any]] = []
    has_machine_mindset = any(sample.task_type == "machine_mindset" for sample in samples)
    if has_machine_mindset and reference_bank is None:
        reference_bank = build_reference_bank(project_root / "data" / "processed" / "machine_mindset_labeled.parquet")
    if embedding_cache_dir is None:
        embedding_cache_dir = project_root / "outputs" / "embedding_cache"

    for record in records:
        sample = by_id[record["sample_id"]]
        response_text = record["response_text"]
        task_type = record["task_type"]

        if task_type == "mbti_mcq":
            task_score = score_mbti.score_response(sample, response_text)
        elif task_type == "ifeval":
            task_score = score_ifeval.score_response(sample, response_text)
        else:
            task_score = _score_machine_mindset_response(
                sample=sample,
                record=record,
                response_text=response_text,
                reference_bank=reference_bank,
                embedding_cache_dir=embedding_cache_dir,
            )

        task_score.update(
            {
                "run_id": record["run_id"],
                "trial_id": record["trial_id"],
                "condition": record["condition"],
                "persona_a": record["persona_a"],
                "persona_b": record["persona_b"],
                "model_name": record["model_name"],
                "task_type": task_type,
            }
        )
        scored.append(task_score)
    return scored


def _score_machine_mindset_response(
    *,
    sample: ExperimentSample,
    record: dict[str, Any],
    response_text: str,
    reference_bank: dict[str, Any] | None,
    embedding_cache_dir: Path,
) -> dict[str, Any]:
    if reference_bank is None:
        raise ValueError("Machine Mindset scoring requires a loaded reference bank.")
    prompt_key = str(sample.metadata.get("prompt_key", ""))
    source_group = str(sample.metadata.get("source_group", ""))
    if not prompt_key or not source_group:
        raise ValueError(
            f"Machine Mindset sample {sample.sample_id} is missing prompt_key/source_group metadata required for alignment scoring."
        )

    active_persona = active_persona_for_condition(
        str(record.get("condition", "")),
        str(record.get("persona_a", "")),
        str(record.get("persona_b", "")),
    )
    task_score: dict[str, Any]
    if source_group == "self_awareness":
        task_score = score_self_awareness_response(
            response_text=response_text,
            prompt_key=prompt_key,
            target_mbti_type=active_persona,
            reference_bank=reference_bank,
            persona_a=str(record.get("persona_a", "")),
            embedding_cache_dir=embedding_cache_dir,
        )
    elif source_group == "dimension_pole":
        dimension = str(sample.metadata.get("mbti_dimension", ""))
        if not dimension:
            raise ValueError(
                f"Machine Mindset dimension-pole sample {sample.sample_id} is missing mbti_dimension metadata."
            )
        task_score = score_dimension_response(
            response_text=response_text,
            prompt_key=prompt_key,
            dimension=dimension,
            target_mbti_type=active_persona,
            reference_bank=reference_bank,
            persona_a=str(record.get("persona_a", "")),
            embedding_cache_dir=embedding_cache_dir,
        )
    else:
        raise ValueError(f"Unsupported Machine Mindset source_group: {source_group!r}")

    task_score.update(
        {
            "sample_id": sample.sample_id,
            "score_type": "machine_mindset_alignment",
            "similarity_backend": "embedding",
            "embedding_model": DEFAULT_EMBEDDING_MODEL,
        }
    )
    return task_score


if __name__ == "__main__":
    main()
