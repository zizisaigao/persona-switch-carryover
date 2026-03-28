from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from src.models.cache import RequestCache
from src.models.mock_client import MockClient
from src.models.openrouter_client import OpenRouterClient
from src.runner.batch_run import run_batch
from src.scoring import score_ifeval, score_mbti, score_similarity
from src.utils.config import get_project_root, load_all_configs
from src.utils.ids import make_run_id
from src.utils.io import load_samples_csv, write_jsonl
from src.utils.logging import configure_logging
from src.utils.schema import ExperimentSample


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Persona switching experiment runner.")
    parser.add_argument("--condition", type=str, default=None, help="Condition name from configs/experiments.yaml")
    parser.add_argument("--persona-a", type=str, default=None, help="Warm-up / persona A label")
    parser.add_argument("--persona-b", type=str, default=None, help="Evaluation persona B label")
    parser.add_argument("--mock", action="store_true", help="Use mock model client")
    parser.add_argument("--no-mock", action="store_true", help="Force real provider even if config default enables mock mode")
    parser.add_argument("--no-resume", action="store_true", help="Disable resumable skipping for this run")
    parser.add_argument("--max-samples", type=int, default=None, help="Override budget max samples")
    parser.add_argument("--samples-csv", type=str, default=None, help="Override sample CSV path")
    return parser.parse_args()


def main() -> None:
    logger = configure_logging()
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
    model_config = configs["models"]["mock_model"] if mock_mode else configs["models"]["default_model"]
    samples_csv = Path(args.samples_csv) if args.samples_csv else project_root / paths_config["samples_csv"]

    if args.max_samples is not None:
        experiments["budget"]["max_samples_per_run"] = args.max_samples
    if args.no_resume:
        experiments["runtime"]["resume"] = False

    client = build_client(model_config)
    cache = RequestCache(project_root / paths_config["cache_dir"]) if experiments["runtime"].get("use_cache", True) else None
    usage_log_path = project_root / paths_config["api_usage_log"]
    raw_output_path = project_root / paths_config["raw_generations"]

    samples = load_samples_csv(samples_csv)
    run_id = make_run_id("persona")

    logger.info(
        "Starting run_id=%s condition=%s persona_a=%s persona_b=%s mock=%s samples=%s",
        run_id,
        condition_name,
        persona_a,
        persona_b,
        mock_mode,
        len(samples),
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

    scored_records = score_batch(records, samples)
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
    if provider == "openrouter":
        return OpenRouterClient(
            api_key_env=model_config["api_key_env"],
            timeout_seconds=int(model_config.get("timeout_seconds", 60)),
            max_retries=int(model_config.get("max_retries", 3)),
        )
    raise ValueError(f"Unsupported provider: {provider}")


def score_batch(records: list[dict[str, Any]], samples: list[ExperimentSample]) -> list[dict[str, Any]]:
    by_id = {sample.sample_id: sample for sample in samples}
    scored: list[dict[str, Any]] = []

    for record in records:
        sample = by_id[record["sample_id"]]
        response_text = record["response_text"]
        task_type = record["task_type"]

        if task_type == "mbti_mcq":
            task_score = score_mbti.score_response(sample, response_text)
        elif task_type == "ifeval":
            task_score = score_ifeval.score_response(sample, response_text)
        else:
            task_score = score_similarity.score_text_similarity(sample.question_text, response_text)
            task_score["sample_id"] = sample.sample_id
            task_score["score_type"] = "machine_mindset"

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


if __name__ == "__main__":
    main()
