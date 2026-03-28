from __future__ import annotations

from src.utils.schema import ExperimentSample


def render_prompt(sample: ExperimentSample) -> str:
    option_lines = []
    for option in sample.options:
        option_lines.append(f"{option.get('label', '?')}. {option.get('text', '').strip()}")
    options_block = "\n".join(option_lines) if option_lines else "No options provided."
    return (
        f"{sample.prompt_text}\n\n"
        f"Question: {sample.question_text}\n"
        f"Options:\n{options_block}\n\n"
        "Return exactly one option label first (for example: A or B), followed by a short justification."
    )
