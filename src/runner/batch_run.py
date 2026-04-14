from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.models.base_client import BaseClient
from src.models.cache import RequestCache
from src.runner.execute_trial import execute_trial, make_resume_key, prepare_shared_warmup_context
from src.utils.ids import make_trial_id
from src.utils.io import append_jsonl, read_jsonl
from src.utils.schema import ExperimentSample


def run_batch(
    *,
    samples: list[ExperimentSample],
    condition_name: str,
    persona_a: str,
    persona_b: str,
    experiments_config: dict[str, Any],
    personas_config: dict[str, Any],
    model_config: dict[str, Any],
    client: BaseClient,
    cache: RequestCache | None,
    usage_log_path: Path,
    raw_output_path: Path,
    run_id: str,
    existing_keys: set[str] | None = None,
    max_samples_override: int | None = None,
) -> list[dict[str, Any]]:
    condition_config = experiments_config["conditions"][condition_name]
    experiment_defaults = experiments_config["experiment"]
    runtime_config = experiments_config["runtime"]
    budget_config = experiments_config["budget"]
    warmup_config = experiments_config["warmup"]

    trials_per_sample = int(experiment_defaults.get("trials_per_sample", 1))
    configured_max_samples = int(budget_config.get("max_samples_per_run", len(samples)))
    max_samples = int(max_samples_override) if max_samples_override is not None else configured_max_samples
    resume = bool(runtime_config.get("resume", True))
    save_messages = bool(runtime_config.get("save_messages", True))
    stop_on_error = bool(budget_config.get("stop_on_error", False))

    if existing_keys is None:
        existing_keys = _load_existing_keys(raw_output_path) if resume else set()
    collected: list[dict[str, Any]] = []
    shared_warmup_contexts: dict[str, dict[str, Any] | None] = {}

    if condition_config.get("do_warmup", False):
        for trial_index in range(1, trials_per_sample + 1):
            trial_id = make_trial_id(trial_index)
            shared_warmup_contexts[trial_id] = prepare_shared_warmup_context(
                condition_config=condition_config,
                persona_a=persona_a,
                persona_b=persona_b,
                personas_config=personas_config,
                warmup_config=warmup_config,
                model_config=model_config,
                client=client,
                cache=cache,
                usage_log_path=usage_log_path,
                run_id=run_id,
                trial_id=trial_id,
            )

    for sample in samples[:max_samples]:
        for trial_index in range(1, trials_per_sample + 1):
            trial_id = make_trial_id(trial_index)
            pending_key = json.dumps(
                {
                    "sample_id": sample.sample_id,
                    "model_name": model_config["model_name"],
                    "condition": condition_name,
                    "persona_a": persona_a,
                    "persona_b": persona_b,
                    "trial_id": trial_id,
                },
                sort_keys=True,
            )
            if pending_key in existing_keys:
                continue

            record = execute_trial(
                sample=sample,
                condition_name=condition_name,
                condition_config=condition_config,
                persona_a=persona_a,
                persona_b=persona_b,
                personas_config=personas_config,
                warmup_config=warmup_config,
                model_config=model_config,
                client=client,
                cache=cache,
                usage_log_path=usage_log_path,
                run_id=run_id,
                trial_id=trial_id,
                save_messages=save_messages,
                shared_warmup_context=shared_warmup_contexts.get(trial_id),
            )
            append_jsonl(raw_output_path, record)
            existing_keys.add(make_resume_key(record))
            collected.append(record)

            if record["status"] != "success" and stop_on_error:
                return collected

    return collected


def _load_existing_keys(raw_output_path: Path) -> set[str]:
    existing = read_jsonl(raw_output_path)
    return {make_resume_key(record) for record in existing}
