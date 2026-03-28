from __future__ import annotations

from dataclasses import asdict
import json
from pathlib import Path
from typing import Any

from src.models.base_client import BaseClient
from src.models.cache import RequestCache
from src.runner.build_messages import build_messages
from src.runner.inference import generate_with_cache
from src.runner.summarize_memory import summarize_history
from src.runner.warmup import run_warmup_dialogue
from src.utils.ids import timestamp_utc
from src.utils.schema import ExperimentSample


def execute_trial(
    *,
    sample: ExperimentSample,
    condition_name: str,
    condition_config: dict[str, Any],
    persona_a: str,
    persona_b: str,
    personas_config: dict[str, Any],
    warmup_config: dict[str, Any],
    model_config: dict[str, Any],
    client: BaseClient,
    cache: RequestCache | None,
    usage_log_path: Path,
    run_id: str,
    trial_id: str,
    save_messages: bool = True,
) -> dict[str, Any]:
    warmup_persona = condition_config.get("warmup_persona_override", persona_a)
    prior_history: list[dict[str, str]] = []
    warmup_history: list[dict[str, str]] = []
    memory_summary: str | None = None

    if condition_config.get("do_warmup", False):
        warmup_prompts = list(warmup_config.get("prompts", []))[: int(warmup_config.get("turns", 0))]
        prior_history = run_warmup_dialogue(
            client=client,
            cache=cache,
            usage_log_path=usage_log_path,
            provider=model_config["provider"],
            model_name=model_config["model_name"],
            temperature=float(model_config["temperature"]),
            max_tokens=int(model_config["max_tokens"]),
            persona_name=warmup_persona,
            personas_config=personas_config,
            warmup_prompts=warmup_prompts,
            run_id=run_id,
            trial_id=trial_id,
            sample_id=sample.sample_id,
        )
        warmup_history = list(prior_history)
        if condition_config.get("use_summary", False):
            memory_summary = summarize_history(prior_history)
            prior_history = []

    messages = build_messages(
        sample=sample,
        condition=condition_name,
        persona_a=persona_a,
        persona_b=persona_b,
        personas_config=personas_config,
        prior_history=prior_history if condition_config.get("use_history", False) else None,
        memory_summary=memory_summary,
    )
    response = generate_with_cache(
        client=client,
        cache=cache,
        usage_log_path=usage_log_path,
        provider=model_config["provider"],
        model_name=model_config["model_name"],
        messages=messages,
        temperature=float(model_config["temperature"]),
        max_tokens=int(model_config["max_tokens"]),
        log_context={
            "run_id": run_id,
            "trial_id": trial_id,
            "sample_id": sample.sample_id,
            "phase": "evaluation",
            "condition": condition_name,
        },
    )

    meta = {
        "source_dataset": sample.source_dataset,
        "warmup_persona": warmup_persona if condition_config.get("do_warmup", False) else None,
        "warmup_history": warmup_history,
        "memory_summary": memory_summary,
        "target_label": sample.target_label,
        "usage": asdict(response.usage),
        "cache_hit": response.cache_hit,
        "latency_seconds": response.latency_seconds,
        "raw_response": response.raw_response,
    }

    return {
        "run_id": run_id,
        "sample_id": sample.sample_id,
        "task_type": sample.task_type,
        "model_name": model_config["model_name"],
        "condition": condition_name,
        "persona_a": persona_a,
        "persona_b": persona_b,
        "trial_id": trial_id,
        "messages_json": messages if save_messages else [],
        "response_text": response.text,
        "timestamp": timestamp_utc(),
        "status": response.status,
        "meta_json": meta,
    }


def make_resume_key(record: dict[str, Any]) -> str:
    return json.dumps(
        {
            "sample_id": record["sample_id"],
            "model_name": record["model_name"],
            "condition": record["condition"],
            "persona_a": record["persona_a"],
            "persona_b": record["persona_b"],
            "trial_id": record["trial_id"],
        },
        sort_keys=True,
    )
