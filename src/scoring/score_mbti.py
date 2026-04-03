from __future__ import annotations

import re
from typing import Any

from src.utils.schema import ExperimentSample


def score_response(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    predicted = extract_option_label(response_text)
    option_dimensions = sample.metadata.get("option_dimensions", {})
    selected_dimension = option_dimensions.get(predicted) if predicted else None
    is_correct = None
    if sample.target_label:
        is_correct = bool(predicted and predicted == sample.target_label)
    return {
        "sample_id": sample.sample_id,
        "score_type": "mbti_mcq",
        "predicted_label": predicted,
        "selected_dimension": selected_dimension,
        "target_label": sample.target_label,
        "is_correct": is_correct,
    }


def extract_option_label(response_text: str) -> str | None:
    match = re.search(r"^\s*([ABCD])(?:[\.\):]|\b)", response_text.strip(), flags=re.IGNORECASE)
    return match.group(1) if match else None


def aggregate_profiles(scored_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str, str, str], list[dict[str, Any]]] = {}
    for record in scored_records:
        if record.get("task_type") != "mbti_mcq":
            continue
        if not record.get("selected_dimension"):
            continue
        key = (
            record["run_id"],
            record["condition"],
            record["persona_a"],
            record["persona_b"],
            record.get("model_name", ""),
            record.get("trial_id", ""),
        )
        grouped.setdefault(key, []).append(record)

    return [_aggregate_single_group(group_key, items) for group_key, items in grouped.items()]


def _aggregate_single_group(
    group_key: tuple[str, str, str, str, str, str],
    items: list[dict[str, Any]],
) -> dict[str, Any]:
    run_id, condition, persona_a, persona_b, model_name, trial_id = group_key
    counts = {dim: 0 for dim in ["E", "I", "S", "N", "T", "F", "J", "P"]}
    for item in items:
        counts[item["selected_dimension"]] += 1

    final_type = "".join(
        [
            _pick_dimension(counts, "E", "I"),
            _pick_dimension(counts, "S", "N"),
            _pick_dimension(counts, "T", "F"),
            _pick_dimension(counts, "J", "P"),
        ]
    )
    return {
        "run_id": run_id,
        "condition": condition,
        "persona_a": persona_a,
        "persona_b": persona_b,
        "model_name": model_name,
        "trial_id": trial_id,
        "score_type": "mbti_profile",
        "items_scored": len(items),
        "dimension_counts": counts,
        "final_type": final_type,
    }


def _pick_dimension(counts: dict[str, int], left: str, right: str) -> str:
    if counts[left] > counts[right]:
        return left
    if counts[right] > counts[left]:
        return right
    return "X"
