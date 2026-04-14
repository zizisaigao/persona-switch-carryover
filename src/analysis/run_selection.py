from __future__ import annotations

from collections import defaultdict
from typing import Any


def build_run_metadata(raw_records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in raw_records:
        by_run[str(record["run_id"])].append(record)

    metadata: dict[str, dict[str, Any]] = {}
    for run_id, items in by_run.items():
        first = items[0]
        meta_json = first.get("meta_json", {}) or {}
        timestamps = [str(item.get("timestamp", "")) for item in items if item.get("timestamp")]
        metadata[run_id] = {
            "run_id": run_id,
            "task_type": first.get("task_type", ""),
            "condition": first.get("condition", ""),
            "persona_a": first.get("persona_a", ""),
            "persona_b": first.get("persona_b", ""),
            "model_name": first.get("model_name", ""),
            "source_dataset": str(meta_json.get("source_dataset", "")),
            "sample_count": len(items),
            "timestamp": max(timestamps) if timestamps else "",
            "retain_mechanism": str(meta_json.get("retain_mechanism", "")),
            "reinforcement_repeats": int(meta_json.get("reinforcement_repeats", 0) or 0),
            "switch_strength": str(meta_json.get("switch_strength", "default")),
        }
    return metadata


def select_latest_pair_run(
    *,
    run_metadata: dict[str, dict[str, Any]],
    scored_run_ids: set[str] | None,
    task_type: str,
    condition: str,
    persona_a: str,
    persona_b: str,
    model_name: str | None,
    source_dataset: str | None,
) -> str | None:
    candidates = [
        meta
        for meta in run_metadata.values()
        if meta["task_type"] == task_type
        and meta["condition"] == condition
        and meta["persona_a"] == persona_a
        and meta["persona_b"] == persona_b
        and (scored_run_ids is None or meta["run_id"] in scored_run_ids)
        and (model_name is None or meta["model_name"] == model_name)
        and (source_dataset is None or meta["source_dataset"] == source_dataset)
    ]
    if not candidates:
        return None
    latest = max(candidates, key=lambda item: (item["sample_count"], item["timestamp"]))
    return str(latest["run_id"])


def select_latest_premise_mbti_only_run(
    *,
    run_metadata: dict[str, dict[str, Any]],
    scored_run_ids: set[str] | None,
    task_type: str,
    premise_persona: str,
    model_name: str | None,
    source_dataset: str | None,
) -> str | None:
    candidates = [
        meta
        for meta in run_metadata.values()
        if meta["task_type"] == task_type
        and meta["condition"] == "MBTI_only"
        and meta["persona_b"] == premise_persona
        and (scored_run_ids is None or meta["run_id"] in scored_run_ids)
        and (model_name is None or meta["model_name"] == model_name)
        and (source_dataset is None or meta["source_dataset"] == source_dataset)
    ]
    if not candidates:
        return None

    def _sort_key(item: dict[str, Any]) -> tuple[int, int, str]:
        exact_self_target = int(item["persona_a"] == premise_persona and item["persona_b"] == premise_persona)
        return (exact_self_target, int(item["sample_count"]), str(item["timestamp"]))

    latest = max(candidates, key=_sort_key)
    return str(latest["run_id"])


def build_selection_row(
    *,
    task_type: str,
    selection_role: str,
    condition_label: str,
    run_id: str,
    run_metadata: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    meta = run_metadata[run_id]
    return {
        "task_type": task_type,
        "selection_role": selection_role,
        "condition": condition_label,
        "run_id": run_id,
        "source_dataset": meta["source_dataset"],
        "model_name": meta["model_name"],
        "retain_mechanism": meta.get("retain_mechanism", ""),
        "reinforcement_repeats": meta.get("reinforcement_repeats", 0),
        "sample_count": meta["sample_count"],
        "timestamp": meta["timestamp"],
        "source_persona_a": meta["persona_a"],
        "source_persona_b": meta["persona_b"],
    }
