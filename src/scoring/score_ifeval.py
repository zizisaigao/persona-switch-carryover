from __future__ import annotations

from typing import Any

from src.utils.schema import ExperimentSample


def score_response(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    meets_constraint = True
    if sample.target_label == "format_two_bullets":
        bullet_lines = [line for line in response_text.splitlines() if line.strip().startswith("-")]
        meets_constraint = len(bullet_lines) == 2
    return {
        "sample_id": sample.sample_id,
        "score_type": "ifeval",
        "target_label": sample.target_label,
        "meets_constraint": meets_constraint,
    }
