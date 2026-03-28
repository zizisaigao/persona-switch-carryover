from __future__ import annotations

from src.utils.schema import ExperimentSample


def render_prompt(sample: ExperimentSample) -> str:
    return (
        f"{sample.prompt_text}\n\n"
        f"Instruction: {sample.question_text}\n\n"
        "Follow the instruction exactly."
    )
