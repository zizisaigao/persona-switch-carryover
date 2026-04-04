from __future__ import annotations

from pathlib import Path

from src.models.base_client import BaseClient
from src.models.cache import RequestCache
from src.runner.build_messages import build_warmup_messages
from src.runner.inference import generate_with_cache


def run_warmup_dialogue(
    *,
    client: BaseClient,
    cache: RequestCache | None,
    usage_log_path: Path,
    provider: str,
    model_name: str,
    temperature: float,
    max_tokens: int,
    persona_name: str,
    personas_config: dict,
    warmup_prompts: list[str],
    run_id: str,
    trial_id: str,
    sample_id: str,
    existing_history: list[dict[str, str]] | None = None,
    start_turn_index: int = 1,
) -> list[dict[str, str]]:
    history_pairs: list[dict[str, str]] = list(existing_history or [])
    for turn_index, warmup_prompt in enumerate(warmup_prompts, start=start_turn_index):
        messages = build_warmup_messages(
            warmup_prompt=warmup_prompt,
            persona_name=persona_name,
            personas_config=personas_config,
            prior_history=history_pairs,
        )
        response = generate_with_cache(
            client=client,
            cache=cache,
            usage_log_path=usage_log_path,
            provider=provider,
            model_name=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            log_context={
                "run_id": run_id,
                "trial_id": trial_id,
                "sample_id": sample_id,
                "phase": "warmup",
                "turn_index": str(turn_index),
            },
        )
        assistant_text = response.text if response.status == "success" else f"ERROR: {response.error_message}"
        history_pairs.append({"user": warmup_prompt, "assistant": assistant_text})
    return history_pairs
