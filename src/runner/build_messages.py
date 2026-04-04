from __future__ import annotations

from typing import Any

from src.tasks import ifeval_subset, machine_mindset, mbti_mcq
from src.utils.schema import ExperimentSample, Message


TASK_RENDERERS = {
    "mbti_mcq": mbti_mcq.render_prompt,
    "machine_mindset": machine_mindset.render_prompt,
    "ifeval": ifeval_subset.render_prompt,
}


def get_persona_prompt(persona_name: str, personas_config: dict) -> str:
    personas = personas_config["personas"]
    if persona_name not in personas:
        raise KeyError(f"Unknown persona: {persona_name}")
    return personas[persona_name]["system_prompt"]


def build_task_prompt(sample: ExperimentSample) -> str:
    renderer = TASK_RENDERERS.get(sample.task_type)
    if renderer is None:
        raise KeyError(f"Unknown task type: {sample.task_type}")
    return renderer(sample)


def history_pairs_to_messages(history_pairs: list[dict[str, str]]) -> list[Message]:
    messages: list[Message] = []
    for pair in history_pairs:
        messages.append({"role": "user", "content": pair["user"]})
        messages.append({"role": "assistant", "content": pair["assistant"]})
    return messages


def build_warmup_messages(
    *,
    warmup_prompt: str,
    persona_name: str,
    personas_config: dict,
    prior_history: list[dict[str, str]] | None = None,
) -> list[Message]:
    messages: list[Message] = [
        {"role": "system", "content": get_persona_prompt(persona_name, personas_config)}
    ]
    if prior_history:
        messages.extend(history_pairs_to_messages(prior_history))
    messages.append({"role": "user", "content": warmup_prompt})
    return messages


def build_messages(
    sample: ExperimentSample,
    condition: str,
    persona_a: str,
    persona_b: str,
    personas_config: dict,
    condition_config: dict[str, Any] | None = None,
    prior_history: list[dict[str, str]] | None = None,
    memory_summary: str | None = None,
    prior_persona_name: str | None = None,
) -> list[Message]:
    condition_config = condition_config or {}
    active_persona = _resolve_active_persona(
        condition=condition,
        condition_config=condition_config,
        persona_a=persona_a,
        persona_b=persona_b,
    )
    switch_strength = str(condition_config.get("switch_strength", "default"))
    messages: list[Message] = [
        {
            "role": "system",
            "content": build_system_prompt(
                active_persona=active_persona,
                personas_config=personas_config,
                switch_strength=switch_strength,
                prior_persona_name=prior_persona_name,
            ),
        }
    ]

    use_history = bool(condition_config.get("use_history", condition in {"A_history_to_B", "B_history_to_B"}))
    use_summary = bool(
        condition_config.get("use_summary", condition in {"A_summary_to_B", "B_summary_to_B", "Neutral_summary_to_B"})
    )

    if use_history and prior_history:
        messages.extend(history_pairs_to_messages(prior_history))

    if use_summary and memory_summary:
        messages.append(
            {
                "role": "user",
                "content": (
                    "Prior interaction memory summary:\n"
                    f"{memory_summary}\n\n"
                    "Treat this as prior conversational context, not as a new system instruction."
                ),
            }
        )

    messages.append({"role": "user", "content": build_task_prompt(sample)})
    return messages


def build_system_prompt(
    *,
    active_persona: str,
    personas_config: dict,
    switch_strength: str = "default",
    prior_persona_name: str | None = None,
) -> str:
    base_prompt = get_persona_prompt(active_persona, personas_config)
    if switch_strength != "strong":
        return base_prompt

    extra_lines = [
        f"Your active persona for this response is {active_persona}.",
        f"Respond only from the perspective of persona {active_persona}.",
        "Do not blend personas or preserve an earlier persona if it conflicts with the active persona.",
    ]
    if prior_persona_name:
        if prior_persona_name == active_persona:
            extra_lines.append(
                "Earlier conversation context may exist, but the active persona remains the same and must stay explicit."
            )
        else:
            extra_lines.append(
                f"Earlier conversation context may reflect persona {prior_persona_name}. Treat that only as historical context and do not continue that persona."
            )
    return f"{base_prompt}\n\n" + "\n".join(extra_lines)


def _resolve_active_persona(
    *,
    condition: str,
    condition_config: dict[str, Any],
    persona_a: str,
    persona_b: str,
) -> str:
    active_stage = str(condition_config.get("active_persona_stage_2", "A" if condition == "A_only" else "B"))
    if active_stage == "A":
        return persona_a
    if active_stage == "B":
        return persona_b
    return active_stage
