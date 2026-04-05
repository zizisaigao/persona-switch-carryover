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
    do_warmup = bool(condition_config.get("do_warmup", False))
    reinforcement_repeats = int(condition_config.get("reinforcement_repeats", 1 if do_warmup else 0))
    warmup_persona = _resolve_persona_reference(
        condition_config.get("warmup_persona_override"),
        persona_a=persona_a,
        persona_b=persona_b,
        default_persona=persona_a,
    )
    prior_history: list[dict[str, str]] = []
    warmup_history: list[dict[str, str]] = []
    memory_summary: str | None = None

    if do_warmup:
        warmup_prompt_blocks = _resolve_warmup_prompt_blocks(
            warmup_config=warmup_config,
            reinforcement_repeats=reinforcement_repeats,
        )
        for warmup_prompts in warmup_prompt_blocks:
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
                existing_history=prior_history,
                start_turn_index=len(prior_history) + 1,
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
        condition_config=condition_config,
        prior_history=prior_history if condition_config.get("use_history", False) else None,
        memory_summary=memory_summary,
        prior_persona_name=warmup_persona if do_warmup else None,
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
        "warmup_persona": warmup_persona if do_warmup else None,
        "warmup_history": warmup_history,
        "warmup_turn_count": len(warmup_history),
        "warmup_prompt_blocks": warmup_prompt_blocks if do_warmup else [],
        "memory_summary": memory_summary,
        "switch_strength": condition_config.get("switch_strength", "default"),
        "retain_mechanism": condition_config.get("retain_mechanism", ""),
        "reinforcement_repeats": reinforcement_repeats,
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


def _resolve_persona_reference(
    reference: str | None,
    *,
    persona_a: str,
    persona_b: str,
    default_persona: str,
) -> str:
    if not reference:
        return default_persona
    if reference == "A":
        return persona_a
    if reference == "B":
        return persona_b
    return reference


def _resolve_warmup_prompt_blocks(
    *,
    warmup_config: dict[str, Any],
    reinforcement_repeats: int,
) -> list[list[str]]:
    if reinforcement_repeats <= 0:
        return []

    turns = int(warmup_config.get("turns", 0))
    base_prompts = list(warmup_config.get("prompts", []))[:turns]
    reinforcement_blocks = [
        list(block)[:turns]
        for block in warmup_config.get("reinforcement_prompt_blocks", [])
    ]

    required_extra_blocks = max(0, reinforcement_repeats - 1)
    if len(reinforcement_blocks) < required_extra_blocks:
        raise ValueError(
            "Not enough warm-up reinforcement prompt blocks configured for "
            f"reinforcement_repeats={reinforcement_repeats}."
        )

    prompt_blocks = [base_prompts]
    prompt_blocks.extend(reinforcement_blocks[:required_extra_blocks])
    return prompt_blocks
