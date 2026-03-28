from __future__ import annotations

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
    prior_history: list[dict[str, str]] | None = None,
    memory_summary: str | None = None,
) -> list[Message]:
    active_persona = persona_a if condition == "A_only" else persona_b
    messages: list[Message] = [
        {"role": "system", "content": get_persona_prompt(active_persona, personas_config)}
    ]

    if condition == "A_history_to_B" and prior_history:
        messages.extend(history_pairs_to_messages(prior_history))

    if condition in {"A_summary_to_B", "Neutral_summary_to_B"} and memory_summary:
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
