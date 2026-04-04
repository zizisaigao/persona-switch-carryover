from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


TRACKS = {
    "history": {
        "simple_condition": "A_history_to_B",
        "reinforced_conditions": ["A2_history_to_B", "A3_history_to_B"],
    },
    "summary": {
        "simple_condition": "A_summary_to_B",
        "reinforced_conditions": ["A2_summary_to_B", "A3_summary_to_B"],
    },
}
BASELINE_CONDITION = "B_only"
OPTIONAL_REFERENCE_CONDITIONS = ["A_only"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare reusable RQ1 successful switches against reinforced-A RQ3 runs."
    )
    parser.add_argument("--persona-a", required=True)
    parser.add_argument("--persona-b", required=True)
    parser.add_argument("--task-types", nargs="+", default=["mbti_mcq", "machine_mindset", "ifeval"])
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--source-dataset", default=None)
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    parser.add_argument("--classification-file", type=Path, default=None)
    parser.add_argument(
        "--required-overall-classification",
        choices=["failed", "successful"],
        default="successful",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    run_metadata = _build_run_metadata(raw_records)
    scored_run_ids = {str(record["run_id"]) for record in scored_records}
    success_keys = _build_success_key_set(raw_records)
    classification_map = _load_classification_map(args.classification_file)
    eligible_tracks = _resolve_eligible_tracks(
        classification_map=classification_map,
        required_classification=args.required_overall_classification,
    )
    if not eligible_tracks:
        raise SystemExit("No RQ3 tracks satisfied the requested RQ1 classification filter.")

    selected_runs = _select_runs(
        run_metadata=run_metadata,
        scored_run_ids=scored_run_ids,
        persona_a=args.persona_a,
        persona_b=args.persona_b,
        task_types=args.task_types,
        model_name=args.model_name,
        source_dataset=args.source_dataset,
        eligible_tracks=eligible_tracks,
    )

    summary_rows: list[dict[str, Any]] = []
    selected_rows: list[dict[str, Any]] = []
    for task_type in args.task_types:
        task_tracks = selected_runs.get(task_type, {})
        if not task_tracks:
            continue

        for track_name, condition_runs in sorted(task_tracks.items()):
            for condition, run_id in sorted(condition_runs.items()):
                meta = run_metadata[run_id]
                selected_rows.append(
                    {
                        "task_type": task_type,
                        "track": track_name,
                        "condition": condition,
                        "run_id": run_id,
                        "source_dataset": meta["source_dataset"],
                        "model_name": meta["model_name"],
                        "retain_mechanism": meta["retain_mechanism"],
                        "reinforcement_repeats": meta["reinforcement_repeats"],
                        "sample_count": meta["sample_count"],
                        "timestamp": meta["timestamp"],
                    }
                )

            if task_type == "mbti_mcq":
                summary_rows.extend(
                    _analyze_mbti(
                        track_name=track_name,
                        condition_runs=condition_runs,
                        scored_records=scored_records,
                        persona_b=args.persona_b,
                        success_keys=success_keys,
                        run_metadata=run_metadata,
                    )
                )
            elif task_type == "machine_mindset":
                summary_rows.extend(
                    _analyze_machine_mindset(
                        track_name=track_name,
                        condition_runs=condition_runs,
                        raw_records=raw_records,
                        scored_records=scored_records,
                        success_keys=success_keys,
                        run_metadata=run_metadata,
                    )
                )
            elif task_type == "ifeval":
                summary_rows.extend(
                    _analyze_ifeval(
                        track_name=track_name,
                        condition_runs=condition_runs,
                        raw_records=raw_records,
                        scored_records=scored_records,
                        success_keys=success_keys,
                        run_metadata=run_metadata,
                    )
                )

    if not summary_rows:
        raise SystemExit("No complete RQ3 simple-vs-reinforced task groups were found.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or _default_prefix(args.persona_a, args.persona_b)
    summary_path = args.output_dir / f"{prefix}_summary.csv"
    runs_path = args.output_dir / f"{prefix}_selected_runs.csv"
    report_path = args.output_dir / f"{prefix}_report.md"
    _write_csv(summary_path, summary_rows)
    _write_csv(runs_path, selected_rows)
    report_path.write_text(_render_report(summary_rows, selected_rows), encoding="utf-8")

    print(f"wrote summary -> {summary_path}")
    print(f"wrote selected runs -> {runs_path}")
    print(f"wrote report -> {report_path}")


def _load_scored_records(scored_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(scored_dir.glob("*_scores.jsonl")):
        records.extend(read_jsonl(path))
    return records


def _build_run_metadata(raw_records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
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
        }
    return metadata


def _build_success_key_set(raw_records: list[dict[str, Any]]) -> set[str]:
    success_keys: set[str] = set()
    for record in raw_records:
        if record.get("status") != "success":
            continue
        success_keys.add(_record_key(record))
    return success_keys


def _load_classification_map(path: Path | None) -> dict[str, str]:
    if path is None:
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {
        str(row.get("switch_condition", "")): str(row.get("overall_classification", ""))
        for row in rows
        if row.get("switch_condition")
    }


def _resolve_eligible_tracks(
    *,
    classification_map: dict[str, str],
    required_classification: str,
) -> dict[str, dict[str, str | list[str]]]:
    if not classification_map:
        return TRACKS
    eligible: dict[str, dict[str, str | list[str]]] = {}
    for track_name, track_config in TRACKS.items():
        simple_condition = str(track_config["simple_condition"])
        if classification_map.get(simple_condition) == required_classification:
            eligible[track_name] = track_config
    return eligible


def _select_runs(
    *,
    run_metadata: dict[str, dict[str, Any]],
    scored_run_ids: set[str],
    persona_a: str,
    persona_b: str,
    task_types: list[str],
    model_name: str | None,
    source_dataset: str | None,
    eligible_tracks: dict[str, dict[str, str | list[str]]],
) -> dict[str, dict[str, dict[str, str]]]:
    selected: dict[str, dict[str, dict[str, str]]] = {}

    for task_type in task_types:
        candidates = [
            meta
            for meta in run_metadata.values()
            if meta["run_id"] in scored_run_ids
            and meta["task_type"] == task_type
            and meta["persona_a"] == persona_a
            and meta["persona_b"] == persona_b
            and (model_name is None or meta["model_name"] == model_name)
            and (source_dataset is None or meta["source_dataset"] == source_dataset)
        ]
        by_condition: dict[str, str] = {}
        available_conditions = {meta["condition"] for meta in candidates}
        for condition in sorted(available_conditions | set(OPTIONAL_REFERENCE_CONDITIONS) | {BASELINE_CONDITION}):
            condition_candidates = [meta for meta in candidates if meta["condition"] == condition]
            if not condition_candidates:
                continue
            latest = max(condition_candidates, key=lambda item: item["timestamp"])
            by_condition[condition] = latest["run_id"]

        track_runs: dict[str, dict[str, str]] = {}
        for track_name, track_config in eligible_tracks.items():
            required_conditions = {
                BASELINE_CONDITION,
                str(track_config["simple_condition"]),
                *[str(item) for item in track_config["reinforced_conditions"]],
            }
            if not required_conditions.issubset(by_condition):
                continue
            condition_map = {condition: by_condition[condition] for condition in required_conditions}
            for optional_condition in OPTIONAL_REFERENCE_CONDITIONS:
                if optional_condition in by_condition:
                    condition_map[optional_condition] = by_condition[optional_condition]
            track_runs[track_name] = condition_map
        if track_runs:
            selected[task_type] = track_runs
    return selected


def _analyze_mbti(
    *,
    track_name: str,
    condition_runs: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_b: str,
    success_keys: set[str],
    run_metadata: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "mbti_mcq", success_keys=success_keys)
    profiles: dict[str, dict[str, Any]] = {}
    labels_by_condition: dict[str, dict[str, str | None]] = {}
    for condition, run_id in condition_runs.items():
        run_records = records_by_run.get(run_id, [])
        if not run_records:
            continue
        labels_by_condition[condition] = {
            str(item["sample_id"]): item.get("predicted_label")
            for item in run_records
        }
        aggregates = aggregate_profiles(run_records)
        if aggregates:
            profiles[condition] = aggregates[0]

    simple_condition = str(TRACKS[track_name]["simple_condition"])
    b_only_labels = labels_by_condition.get(BASELINE_CONDITION, {})
    a_only_labels = labels_by_condition.get("A_only", {})
    rows: list[dict[str, Any]] = []
    for reinforced_condition in TRACKS[track_name]["reinforced_conditions"]:
        simple_labels = labels_by_condition.get(simple_condition, {})
        reinforced_labels = labels_by_condition.get(str(reinforced_condition), {})
        common_ids = sorted(set(simple_labels) & set(reinforced_labels) & set(b_only_labels))
        if not common_ids:
            continue

        simple_scs = mean(
            1.0 if simple_labels[sample_id] == b_only_labels[sample_id] else 0.0
            for sample_id in common_ids
        )
        reinforced_scs = mean(
            1.0 if reinforced_labels[sample_id] == b_only_labels[sample_id] else 0.0
            for sample_id in common_ids
        )
        row: dict[str, Any] = {
            "task_type": "mbti_mcq",
            "retain_mechanism": track_name,
            "simple_condition": simple_condition,
            "reinforced_condition": reinforced_condition,
            "reinforcement_repeats": run_metadata[condition_runs[str(reinforced_condition)]]["reinforcement_repeats"],
            "n_common_samples": len(common_ids),
            "simple_final_type": profiles.get(simple_condition, {}).get("final_type", ""),
            "reinforced_final_type": profiles.get(reinforced_condition, {}).get("final_type", ""),
        }
        row.update(
            _mbti_weakening_metrics(
                profiles=profiles,
                simple_condition=simple_condition,
                reinforced_condition=str(reinforced_condition),
                persona_b=persona_b,
                simple_scs=simple_scs,
                reinforced_scs=reinforced_scs,
            )
        )
        if a_only_labels:
            a_only_common = sorted(set(common_ids) & set(a_only_labels))
            if a_only_common:
                simple_a_agreement = mean(
                    1.0 if simple_labels[sample_id] == a_only_labels[sample_id] else 0.0
                    for sample_id in a_only_common
                )
                reinforced_a_agreement = mean(
                    1.0 if reinforced_labels[sample_id] == a_only_labels[sample_id] else 0.0
                    for sample_id in a_only_common
                )
                row["simple_rai_item_agreement_gap"] = round(simple_a_agreement - simple_scs, 4)
                row["reinforced_rai_item_agreement_gap"] = round(reinforced_a_agreement - reinforced_scs, 4)
                row["delta_rai_reinforced_minus_simple"] = round(
                    row["reinforced_rai_item_agreement_gap"] - row["simple_rai_item_agreement_gap"],
                    4,
                )
                row["increased_a_influence"] = (
                    row["reinforced_rai_item_agreement_gap"] > row["simple_rai_item_agreement_gap"]
                )
        row["rq3_weakened"] = _is_weakened(row, ["weakened_distance_to_b_only", "weakened_osr", "increased_a_influence"])
        rows.append(row)
    return rows


def _analyze_machine_mindset(
    *,
    track_name: str,
    condition_runs: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
    run_metadata: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, "machine_mindset", success_keys=success_keys)
    scored_by_run = _records_by_run_id(scored_records, "machine_mindset", success_keys=success_keys)
    b_only_texts = _sample_to_text(raw_by_run.get(condition_runs[BASELINE_CONDITION], []))
    a_only_texts = _sample_to_text(raw_by_run.get(condition_runs.get("A_only", ""), []))
    simple_condition = str(TRACKS[track_name]["simple_condition"])
    simple_texts = _sample_to_text(raw_by_run.get(condition_runs[simple_condition], []))
    simple_outcome = _summarize_machine_mindset_scores(scored_by_run.get(condition_runs[simple_condition], []))
    rows: list[dict[str, Any]] = []

    for reinforced_condition in TRACKS[track_name]["reinforced_conditions"]:
        reinforced_texts = _sample_to_text(raw_by_run.get(condition_runs[str(reinforced_condition)], []))
        reinforced_outcome = _summarize_machine_mindset_scores(
            scored_by_run.get(condition_runs[str(reinforced_condition)], [])
        )
        common_ids = sorted(set(simple_texts) & set(reinforced_texts) & set(b_only_texts))
        if not common_ids:
            continue

        simple_scs = mean(_lexical_f1(simple_texts[sample_id], b_only_texts[sample_id]) for sample_id in common_ids)
        reinforced_scs = mean(
            _lexical_f1(reinforced_texts[sample_id], b_only_texts[sample_id]) for sample_id in common_ids
        )
        row: dict[str, Any] = {
            "task_type": "machine_mindset",
            "retain_mechanism": track_name,
            "simple_condition": simple_condition,
            "reinforced_condition": reinforced_condition,
            "reinforcement_repeats": run_metadata[condition_runs[str(reinforced_condition)]]["reinforcement_repeats"],
            "n_common_samples": len(common_ids),
            "simple_mean_task_score": simple_outcome["mean_task_score"],
            "reinforced_mean_task_score": reinforced_outcome["mean_task_score"],
            "delta_mean_task_score": round(reinforced_outcome["mean_task_score"] - simple_outcome["mean_task_score"], 4),
            "simple_mean_keyword_recall": simple_outcome["mean_keyword_recall"],
            "reinforced_mean_keyword_recall": reinforced_outcome["mean_keyword_recall"],
            "delta_mean_keyword_recall": round(
                reinforced_outcome["mean_keyword_recall"] - simple_outcome["mean_keyword_recall"],
                4,
            ),
            "simple_scs_lexical_similarity_to_b_only": round(simple_scs, 4),
            "reinforced_scs_lexical_similarity_to_b_only": round(reinforced_scs, 4),
            "delta_scs_lexical_similarity": round(reinforced_scs - simple_scs, 4),
            "simple_distance_to_b_only": round(1.0 - simple_scs, 4),
            "reinforced_distance_to_b_only": round(1.0 - reinforced_scs, 4),
            "weakened_distance_to_b_only": (1.0 - reinforced_scs) > (1.0 - simple_scs),
            "weakened_task_score": reinforced_outcome["mean_task_score"] < simple_outcome["mean_task_score"],
        }
        if a_only_texts:
            a_only_common = sorted(set(common_ids) & set(a_only_texts))
            if a_only_common:
                simple_a_similarity = mean(
                    _lexical_f1(simple_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common
                )
                reinforced_a_similarity = mean(
                    _lexical_f1(reinforced_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common
                )
                row["simple_rai_lexical_gap"] = round(simple_a_similarity - simple_scs, 4)
                row["reinforced_rai_lexical_gap"] = round(reinforced_a_similarity - reinforced_scs, 4)
                row["delta_rai_lexical_gap"] = round(
                    row["reinforced_rai_lexical_gap"] - row["simple_rai_lexical_gap"],
                    4,
                )
                row["increased_a_influence"] = row["reinforced_rai_lexical_gap"] > row["simple_rai_lexical_gap"]
        row["rq3_weakened"] = _is_weakened(row, ["weakened_distance_to_b_only", "weakened_task_score", "increased_a_influence"])
        rows.append(row)
    return rows


def _analyze_ifeval(
    *,
    track_name: str,
    condition_runs: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
    run_metadata: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, "ifeval", success_keys=success_keys)
    scored_by_run = _records_by_run_id(scored_records, "ifeval", success_keys=success_keys)
    b_only_metrics = _summarize_ifeval_scores(scored_by_run.get(condition_runs[BASELINE_CONDITION], []))
    b_only_texts = _sample_to_text(raw_by_run.get(condition_runs[BASELINE_CONDITION], []))
    a_only_texts = _sample_to_text(raw_by_run.get(condition_runs.get("A_only", ""), []))
    simple_condition = str(TRACKS[track_name]["simple_condition"])
    simple_metrics = _summarize_ifeval_scores(scored_by_run.get(condition_runs[simple_condition], []))
    simple_texts = _sample_to_text(raw_by_run.get(condition_runs[simple_condition], []))
    rows: list[dict[str, Any]] = []

    for reinforced_condition in TRACKS[track_name]["reinforced_conditions"]:
        reinforced_metrics = _summarize_ifeval_scores(scored_by_run.get(condition_runs[str(reinforced_condition)], []))
        reinforced_texts = _sample_to_text(raw_by_run.get(condition_runs[str(reinforced_condition)], []))
        common_ids = sorted(set(simple_texts) & set(reinforced_texts) & set(b_only_texts))
        simple_scs = mean(_lexical_f1(simple_texts[sample_id], b_only_texts[sample_id]) for sample_id in common_ids) if common_ids else 0.0
        reinforced_scs = mean(
            _lexical_f1(reinforced_texts[sample_id], b_only_texts[sample_id]) for sample_id in common_ids
        ) if common_ids else 0.0

        row: dict[str, Any] = {
            "task_type": "ifeval",
            "retain_mechanism": track_name,
            "simple_condition": simple_condition,
            "reinforced_condition": reinforced_condition,
            "reinforcement_repeats": run_metadata[condition_runs[str(reinforced_condition)]]["reinforcement_repeats"],
            "n_common_samples": len(common_ids),
            "primary_metric_name": simple_metrics["primary_metric_name"],
            "secondary_metric_name": simple_metrics["secondary_metric_name"],
            "simple_primary_metric": simple_metrics["primary_metric"],
            "reinforced_primary_metric": reinforced_metrics["primary_metric"],
            "delta_primary_metric": round(reinforced_metrics["primary_metric"] - simple_metrics["primary_metric"], 4),
            "simple_secondary_metric": simple_metrics["secondary_metric"],
            "reinforced_secondary_metric": reinforced_metrics["secondary_metric"],
            "delta_secondary_metric": round(reinforced_metrics["secondary_metric"] - simple_metrics["secondary_metric"], 4),
            "simple_primary_delta_vs_b_only": round(simple_metrics["primary_metric"] - b_only_metrics["primary_metric"], 4),
            "reinforced_primary_delta_vs_b_only": round(
                reinforced_metrics["primary_metric"] - b_only_metrics["primary_metric"],
                4,
            ),
            "simple_distance_to_b_only": round(abs(simple_metrics["primary_metric"] - b_only_metrics["primary_metric"]), 4),
            "reinforced_distance_to_b_only": round(
                abs(reinforced_metrics["primary_metric"] - b_only_metrics["primary_metric"]),
                4,
            ),
            "weakened_distance_to_b_only": abs(reinforced_metrics["primary_metric"] - b_only_metrics["primary_metric"])
            > abs(simple_metrics["primary_metric"] - b_only_metrics["primary_metric"]),
            "weakened_primary_metric": reinforced_metrics["primary_metric"] < simple_metrics["primary_metric"],
            "simple_scs_lexical_similarity_to_b_only": round(simple_scs, 4),
            "reinforced_scs_lexical_similarity_to_b_only": round(reinforced_scs, 4),
            "weakened_lexical_scs": reinforced_scs < simple_scs,
        }
        if a_only_texts and common_ids:
            a_only_common = sorted(set(common_ids) & set(a_only_texts))
            if a_only_common:
                simple_a_similarity = mean(
                    _lexical_f1(simple_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common
                )
                reinforced_a_similarity = mean(
                    _lexical_f1(reinforced_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common
                )
                row["simple_rai_lexical_gap"] = round(simple_a_similarity - simple_scs, 4)
                row["reinforced_rai_lexical_gap"] = round(reinforced_a_similarity - reinforced_scs, 4)
                row["delta_rai_lexical_gap"] = round(
                    row["reinforced_rai_lexical_gap"] - row["simple_rai_lexical_gap"],
                    4,
                )
                row["increased_a_influence"] = row["reinforced_rai_lexical_gap"] > row["simple_rai_lexical_gap"]
        row["rq3_weakened"] = _is_weakened(
            row,
            ["weakened_distance_to_b_only", "weakened_primary_metric", "weakened_lexical_scs", "increased_a_influence"],
        )
        rows.append(row)
    return rows


def _records_by_run_id(
    records: list[dict[str, Any]],
    task_type: str,
    *,
    success_keys: set[str] | None = None,
) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("task_type") != task_type:
            continue
        if success_keys is not None and _record_key(record) not in success_keys:
            continue
        grouped[str(record["run_id"])].append(record)
    return grouped


def _sample_to_text(records: list[dict[str, Any]]) -> dict[str, str]:
    return {str(record["sample_id"]): str(record.get("response_text", "")) for record in records}


def _mbti_weakening_metrics(
    *,
    profiles: dict[str, dict[str, Any]],
    simple_condition: str,
    reinforced_condition: str,
    persona_b: str,
    simple_scs: float,
    reinforced_scs: float,
) -> dict[str, Any]:
    simple_osr = _letter_match_rate(str(profiles.get(simple_condition, {}).get("final_type", "")), persona_b)
    reinforced_osr = _letter_match_rate(str(profiles.get(reinforced_condition, {}).get("final_type", "")), persona_b)
    return {
        "simple_osr_final_type_match_target_b": int(profiles.get(simple_condition, {}).get("final_type", "") == persona_b),
        "reinforced_osr_final_type_match_target_b": int(
            profiles.get(reinforced_condition, {}).get("final_type", "") == persona_b
        ),
        "simple_osr_letter_match_rate": round(simple_osr, 4),
        "reinforced_osr_letter_match_rate": round(reinforced_osr, 4),
        "delta_osr_reinforced_minus_simple": round(reinforced_osr - simple_osr, 4),
        "simple_scs_vs_b_only": round(simple_scs, 4),
        "reinforced_scs_vs_b_only": round(reinforced_scs, 4),
        "delta_scs_reinforced_minus_simple": round(reinforced_scs - simple_scs, 4),
        "simple_distance_to_b_only": round(1.0 - simple_scs, 4),
        "reinforced_distance_to_b_only": round(1.0 - reinforced_scs, 4),
        "weakened_distance_to_b_only": (1.0 - reinforced_scs) > (1.0 - simple_scs),
        "weakened_osr": reinforced_osr < simple_osr,
    }


def _summarize_machine_mindset_scores(records: list[dict[str, Any]]) -> dict[str, float]:
    if not records:
        return {"mean_task_score": 0.0, "mean_keyword_recall": 0.0}
    task_scores = [float(record.get("score", 0.0) or 0.0) for record in records]
    keyword_recalls = [float(record.get("keyword_recall", 0.0) or 0.0) for record in records]
    return {
        "mean_task_score": round(mean(task_scores), 4),
        "mean_keyword_recall": round(mean(keyword_recalls), 4),
    }


def _summarize_ifeval_scores(records: list[dict[str, Any]]) -> dict[str, float | str]:
    if not records:
        return {
            "primary_metric_name": "missing",
            "primary_metric": 0.0,
            "secondary_metric_name": "missing",
            "secondary_metric": 0.0,
        }
    official = any(record.get("checker_source") == "official_google_ifeval" for record in records)
    if official:
        strict_all = [1.0 if bool(record.get("strict_follow_all")) else 0.0 for record in records]
        strict_fraction = []
        for record in records:
            total = int(record.get("instruction_count", 0) or 0)
            passed = int(record.get("strict_checks_passed", 0) or 0)
            strict_fraction.append((passed / total) if total else 0.0)
        return {
            "primary_metric_name": "strict_follow_all_rate",
            "primary_metric": round(mean(strict_all), 4),
            "secondary_metric_name": "mean_strict_instruction_fraction",
            "secondary_metric": round(mean(strict_fraction), 4),
        }

    meets_constraint = [1.0 if bool(record.get("meets_constraint")) else 0.0 for record in records]
    check_fraction = []
    for record in records:
        total = int(record.get("checks_total", 0) or 0)
        passed = int(record.get("checks_passed", 0) or 0)
        check_fraction.append((passed / total) if total else 1.0)
    return {
        "primary_metric_name": "meets_constraint_rate",
        "primary_metric": round(mean(meets_constraint), 4),
        "secondary_metric_name": "mean_checks_pass_fraction",
        "secondary_metric": round(mean(check_fraction), 4),
    }


def _letter_match_rate(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    return sum(1 for ltr_left, ltr_right in zip(left, right) if ltr_left == ltr_right) / min(len(left), len(right))


def _lexical_f1(left: str, right: str) -> float:
    left_tokens = _tokens(left)
    right_tokens = _tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    overlap = len(left_tokens & right_tokens)
    precision = overlap / len(left_tokens)
    recall = overlap / len(right_tokens)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[A-Za-z0-9']+", text)}


def _is_weakened(row: dict[str, Any], keys: list[str]) -> bool:
    present_votes = [bool(row[key]) for key in keys if key in row]
    return sum(1 for vote in present_votes if vote) >= 2


def _default_prefix(persona_a: str, persona_b: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rq3_reinforcement_{persona_a}_to_{persona_b}_{now}"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    fieldnames: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key in seen:
                continue
            seen.add(key)
            fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _render_report(summary_rows: list[dict[str, Any]], selected_rows: list[dict[str, Any]]) -> str:
    lines = ["# RQ3 Reinforcement Comparison", "", "## Selected Runs", ""]
    for row in sorted(selected_rows, key=lambda item: (item["task_type"], item["track"], item["condition"])):
        lines.append(
            f"- {row['task_type']} | {row['track']} | {row['condition']} | {row['run_id']} | "
            f"{row['source_dataset']} | {row['model_name']} | repeats={row['reinforcement_repeats']} | n={row['sample_count']}"
        )

    lines.extend(["", "## Summary", ""])
    for row in summary_rows:
        if row["task_type"] == "mbti_mcq":
            lines.append(
                f"- {row['retain_mechanism']} / {row['reinforced_condition']}: "
                f"OSR {row['simple_osr_letter_match_rate']} -> {row['reinforced_osr_letter_match_rate']}, "
                f"SCS {row['simple_scs_vs_b_only']} -> {row['reinforced_scs_vs_b_only']}, "
                f"weakened={row['rq3_weakened']}."
            )
            continue
        if row["task_type"] == "machine_mindset":
            lines.append(
                f"- {row['retain_mechanism']} / {row['reinforced_condition']}: "
                f"mean_task_score {row['simple_mean_task_score']} -> {row['reinforced_mean_task_score']}, "
                f"lexical SCS {row['simple_scs_lexical_similarity_to_b_only']} -> {row['reinforced_scs_lexical_similarity_to_b_only']}, "
                f"weakened={row['rq3_weakened']}."
            )
            continue
        lines.append(
            f"- {row['retain_mechanism']} / {row['reinforced_condition']}: "
            f"{row['primary_metric_name']} {row['simple_primary_metric']} -> {row['reinforced_primary_metric']}, "
            f"distance-to-B_only {row['simple_distance_to_b_only']} -> {row['reinforced_distance_to_b_only']}, "
            f"weakened={row['rq3_weakened']}."
        )
    return "\n".join(lines) + "\n"


def _record_key(record: dict[str, Any]) -> str:
    return json.dumps(
        {
            "run_id": str(record.get("run_id", "")),
            "sample_id": str(record.get("sample_id", "")),
            "trial_id": str(record.get("trial_id", "")),
        },
        sort_keys=True,
    )


if __name__ == "__main__":
    main()
