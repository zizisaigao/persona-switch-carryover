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


DEFAULT_CONDITIONS = [
    "B_only",
    "A_history_to_B",
    "A_summary_to_B",
    "B_history_to_B",
    "B_summary_to_B",
]
CONDITION_PAIRS = [
    ("B_only", "B_only_strong"),
    ("A_history_to_B", "A_history_to_B_strong"),
    ("A_summary_to_B", "A_summary_to_B_strong"),
    ("B_history_to_B", "B_history_to_B_strong"),
    ("B_summary_to_B", "B_summary_to_B_strong"),
]
STRONG_CONDITIONS = [strong for _, strong in CONDITION_PAIRS]
OPTIONAL_REFERENCE_CONDITIONS = ["A_only"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare reusable RQ1 default runs against RQ2 strong-switch runs.")
    parser.add_argument("--persona-a", required=True)
    parser.add_argument("--persona-b", required=True)
    parser.add_argument(
        "--task-types",
        nargs="+",
        default=["mbti_mcq", "machine_mindset", "ifeval"],
    )
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--source-dataset", default=None)
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    parser.add_argument(
        "--classification-file",
        type=Path,
        default=None,
        help="Optional overall classification CSV from classify_rq1_pairs.py for filtering to failed pairs.",
    )
    parser.add_argument(
        "--required-overall-classification",
        choices=["failed", "successful"],
        default="failed",
        help="Used only when --classification-file is provided.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    classification_rows = _load_optional_csv(args.classification_file)
    _validate_required_classification(classification_rows, args.required_overall_classification)
    run_metadata = _build_run_metadata(raw_records)
    scored_run_ids = {str(record["run_id"]) for record in scored_records}
    success_keys = _build_success_key_set(raw_records)

    selected_runs = _select_runs(
        run_metadata=run_metadata,
        scored_run_ids=scored_run_ids,
        persona_a=args.persona_a,
        persona_b=args.persona_b,
        task_types=args.task_types,
        model_name=args.model_name,
        source_dataset=args.source_dataset,
    )

    summary_rows: list[dict[str, Any]] = []
    selected_rows: list[dict[str, Any]] = []
    for task_type in args.task_types:
        task_runs = selected_runs.get(task_type, {})
        if not task_runs:
            continue

        for condition, run_id in sorted(task_runs.items()):
            meta = run_metadata[run_id]
            selected_rows.append(
                {
                    "task_type": task_type,
                    "condition": condition,
                    "run_id": run_id,
                    "source_dataset": meta["source_dataset"],
                    "model_name": meta["model_name"],
                    "sample_count": meta["sample_count"],
                    "timestamp": meta["timestamp"],
                }
            )

        if task_type == "mbti_mcq":
            summary_rows.extend(_analyze_mbti(task_runs, scored_records, args.persona_b, success_keys))
        elif task_type == "machine_mindset":
            summary_rows.extend(_analyze_machine_mindset(task_runs, raw_records, scored_records, success_keys))
        elif task_type == "ifeval":
            summary_rows.extend(_analyze_ifeval(task_runs, scored_records, success_keys))

    if not summary_rows:
        raise SystemExit("No complete RQ2 default-vs-strong task groups were found.")

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


def _load_optional_csv(path: Path | None) -> list[dict[str, str]]:
    if path is None:
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _validate_required_classification(rows: list[dict[str, str]], required_classification: str) -> None:
    if not rows:
        return
    overall_labels = {row.get("overall_classification", "") for row in rows}
    if required_classification not in overall_labels:
        raise SystemExit(
            f"Classification file does not contain overall_classification={required_classification!r}. "
            f"Found: {sorted(label for label in overall_labels if label)}"
        )


def _build_run_metadata(raw_records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in raw_records:
        by_run[str(record["run_id"])].append(record)

    metadata: dict[str, dict[str, Any]] = {}
    for run_id, items in by_run.items():
        first = items[0]
        timestamps = [str(item.get("timestamp", "")) for item in items if item.get("timestamp")]
        metadata[run_id] = {
            "run_id": run_id,
            "task_type": first.get("task_type", ""),
            "condition": first.get("condition", ""),
            "persona_a": first.get("persona_a", ""),
            "persona_b": first.get("persona_b", ""),
            "model_name": first.get("model_name", ""),
            "source_dataset": str(first.get("meta_json", {}).get("source_dataset", "")),
            "sample_count": len(items),
            "timestamp": max(timestamps) if timestamps else "",
        }
    return metadata


def _build_success_key_set(raw_records: list[dict[str, Any]]) -> set[str]:
    success_keys: set[str] = set()
    for record in raw_records:
        if record.get("status") != "success":
            continue
        success_keys.add(_record_key(record))
    return success_keys


def _select_runs(
    *,
    run_metadata: dict[str, dict[str, Any]],
    scored_run_ids: set[str],
    persona_a: str,
    persona_b: str,
    task_types: list[str],
    model_name: str | None,
    source_dataset: str | None,
) -> dict[str, dict[str, str]]:
    required_conditions = set(DEFAULT_CONDITIONS + STRONG_CONDITIONS)
    selected: dict[str, dict[str, str]] = {}

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
        for condition in sorted(required_conditions | set(OPTIONAL_REFERENCE_CONDITIONS)):
            condition_candidates = [meta for meta in candidates if meta["condition"] == condition]
            if not condition_candidates:
                continue
            latest = max(condition_candidates, key=lambda item: item["timestamp"])
            by_condition[condition] = latest["run_id"]
        if required_conditions.issubset(by_condition):
            selected[task_type] = by_condition
    return selected


def _analyze_mbti(
    task_runs: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_b: str,
    success_keys: set[str],
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "mbti_mcq", success_keys=success_keys)
    profiles: dict[str, dict[str, Any]] = {}
    labels_by_condition: dict[str, dict[str, str | None]] = {}
    for condition, run_id in task_runs.items():
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

    a_only_labels = labels_by_condition.get("A_only", {})
    rows: list[dict[str, Any]] = []
    for default_condition, strong_condition in CONDITION_PAIRS:
        default_labels = labels_by_condition[default_condition]
        strong_labels = labels_by_condition[strong_condition]
        b_only_default = labels_by_condition["B_only"]
        b_only_strong = labels_by_condition["B_only_strong"]
        common_ids = sorted(set(default_labels) & set(strong_labels) & set(b_only_default) & set(b_only_strong))
        if not common_ids:
            continue

        row = {
            "task_type": "mbti_mcq",
            "default_condition": default_condition,
            "strong_condition": strong_condition,
            "n_common_samples": len(common_ids),
            "default_success_records": len(default_labels),
            "strong_success_records": len(strong_labels),
            "default_final_type": profiles.get(default_condition, {}).get("final_type", ""),
            "strong_final_type": profiles.get(strong_condition, {}).get("final_type", ""),
            "default_osr_final_type_match_target_b": int(profiles.get(default_condition, {}).get("final_type", "") == persona_b),
            "strong_osr_final_type_match_target_b": int(profiles.get(strong_condition, {}).get("final_type", "") == persona_b),
            "default_osr_letter_match_rate": round(_letter_match_rate(str(profiles.get(default_condition, {}).get("final_type", "")), persona_b), 4),
            "strong_osr_letter_match_rate": round(_letter_match_rate(str(profiles.get(strong_condition, {}).get("final_type", "")), persona_b), 4),
            "delta_osr_letter_match_rate": round(
                _letter_match_rate(str(profiles.get(strong_condition, {}).get("final_type", "")), persona_b)
                - _letter_match_rate(str(profiles.get(default_condition, {}).get("final_type", "")), persona_b),
                4,
            ),
        }
        default_scs = mean(
            1.0 if default_labels[sample_id] == b_only_default[sample_id] else 0.0
            for sample_id in common_ids
        )
        strong_scs = mean(
            1.0 if strong_labels[sample_id] == b_only_strong[sample_id] else 0.0
            for sample_id in common_ids
        )
        row["default_scs_vs_b_only"] = round(default_scs, 4)
        row["strong_scs_vs_b_only"] = round(strong_scs, 4)
        row["delta_scs_strong_minus_default"] = round(strong_scs - default_scs, 4)
        row["default_distance_to_b_only"] = round(1.0 - default_scs, 4)
        row["strong_distance_to_b_only"] = round(1.0 - strong_scs, 4)
        row["improved_distance_to_b_only"] = row["strong_distance_to_b_only"] < row["default_distance_to_b_only"]
        row["improved_osr"] = row["strong_osr_letter_match_rate"] > row["default_osr_letter_match_rate"]

        if a_only_labels:
            a_only_common = sorted(set(common_ids) & set(a_only_labels))
            if a_only_common:
                default_a_agreement = mean(
                    1.0 if default_labels[sample_id] == a_only_labels[sample_id] else 0.0
                    for sample_id in a_only_common
                )
                strong_a_agreement = mean(
                    1.0 if strong_labels[sample_id] == a_only_labels[sample_id] else 0.0
                    for sample_id in a_only_common
                )
                row["default_rai_item_agreement_gap"] = round(default_a_agreement - default_scs, 4)
                row["strong_rai_item_agreement_gap"] = round(strong_a_agreement - strong_scs, 4)
                row["delta_rai_strong_minus_default"] = round(
                    row["strong_rai_item_agreement_gap"] - row["default_rai_item_agreement_gap"],
                    4,
                )
                row["reduced_a_influence"] = row["strong_rai_item_agreement_gap"] < row["default_rai_item_agreement_gap"]
        improvement_votes = [
            bool(row["improved_distance_to_b_only"]),
            bool(row["improved_osr"]),
        ]
        if "reduced_a_influence" in row:
            improvement_votes.append(bool(row["reduced_a_influence"]))
        row["rq2_improved"] = sum(1 for vote in improvement_votes if vote) >= 2
        rows.append(row)
    return rows


def _analyze_machine_mindset(
    task_runs: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, "machine_mindset", success_keys=success_keys)
    scored_by_run = _records_by_run_id(scored_records, "machine_mindset", success_keys=success_keys)
    a_only_texts = _sample_to_text(raw_by_run.get(task_runs.get("A_only", ""), []))
    b_only_default_texts = _sample_to_text(raw_by_run.get(task_runs["B_only"], []))
    b_only_strong_texts = _sample_to_text(raw_by_run.get(task_runs["B_only_strong"], []))
    rows: list[dict[str, Any]] = []

    for default_condition, strong_condition in CONDITION_PAIRS:
        default_texts = _sample_to_text(raw_by_run.get(task_runs[default_condition], []))
        strong_texts = _sample_to_text(raw_by_run.get(task_runs[strong_condition], []))
        default_scores = scored_by_run.get(task_runs[default_condition], [])
        strong_scores = scored_by_run.get(task_runs[strong_condition], [])
        default_outcome = _summarize_machine_mindset_scores(default_scores)
        strong_outcome = _summarize_machine_mindset_scores(strong_scores)

        common_ids = sorted(set(default_texts) & set(strong_texts) & set(b_only_default_texts) & set(b_only_strong_texts))
        if not common_ids:
            continue

        default_scs = mean(_lexical_f1(default_texts[sample_id], b_only_default_texts[sample_id]) for sample_id in common_ids)
        strong_scs = mean(_lexical_f1(strong_texts[sample_id], b_only_strong_texts[sample_id]) for sample_id in common_ids)
        row = {
            "task_type": "machine_mindset",
            "default_condition": default_condition,
            "strong_condition": strong_condition,
            "n_common_samples": len(common_ids),
            "default_success_records": len(default_scores),
            "strong_success_records": len(strong_scores),
            "default_mean_task_score": default_outcome["mean_task_score"],
            "strong_mean_task_score": strong_outcome["mean_task_score"],
            "delta_mean_task_score": round(strong_outcome["mean_task_score"] - default_outcome["mean_task_score"], 4),
            "default_mean_keyword_recall": default_outcome["mean_keyword_recall"],
            "strong_mean_keyword_recall": strong_outcome["mean_keyword_recall"],
            "delta_mean_keyword_recall": round(strong_outcome["mean_keyword_recall"] - default_outcome["mean_keyword_recall"], 4),
            "default_scs_lexical_similarity_to_b_only": round(default_scs, 4),
            "strong_scs_lexical_similarity_to_b_only": round(strong_scs, 4),
            "delta_scs_lexical_similarity": round(strong_scs - default_scs, 4),
            "default_distance_to_b_only": round(1.0 - default_scs, 4),
            "strong_distance_to_b_only": round(1.0 - strong_scs, 4),
            "improved_distance_to_b_only": (1.0 - strong_scs) < (1.0 - default_scs),
            "improved_task_score": strong_outcome["mean_task_score"] > default_outcome["mean_task_score"],
        }
        if a_only_texts:
            a_only_common = sorted(set(common_ids) & set(a_only_texts))
            if a_only_common:
                default_a_similarity = mean(_lexical_f1(default_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common)
                strong_a_similarity = mean(_lexical_f1(strong_texts[sample_id], a_only_texts[sample_id]) for sample_id in a_only_common)
                row["default_rai_lexical_gap"] = round(default_a_similarity - default_scs, 4)
                row["strong_rai_lexical_gap"] = round(strong_a_similarity - strong_scs, 4)
                row["delta_rai_lexical_gap"] = round(row["strong_rai_lexical_gap"] - row["default_rai_lexical_gap"], 4)
                row["reduced_a_influence"] = row["strong_rai_lexical_gap"] < row["default_rai_lexical_gap"]
        improvement_votes = [
            bool(row["improved_distance_to_b_only"]),
            bool(row["improved_task_score"]),
        ]
        if "reduced_a_influence" in row:
            improvement_votes.append(bool(row["reduced_a_influence"]))
        row["rq2_improved"] = sum(1 for vote in improvement_votes if vote) >= 2
        rows.append(row)
    return rows


def _analyze_ifeval(
    task_runs: dict[str, str],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
) -> list[dict[str, Any]]:
    scored_by_run = _records_by_run_id(scored_records, "ifeval", success_keys=success_keys)
    rows: list[dict[str, Any]] = []
    b_default_metrics = _summarize_ifeval_scores(scored_by_run.get(task_runs["B_only"], []))
    b_strong_metrics = _summarize_ifeval_scores(scored_by_run.get(task_runs["B_only_strong"], []))
    for default_condition, strong_condition in CONDITION_PAIRS:
        default_metrics = _summarize_ifeval_scores(scored_by_run.get(task_runs[default_condition], []))
        strong_metrics = _summarize_ifeval_scores(scored_by_run.get(task_runs[strong_condition], []))
        rows.append(
            {
                "task_type": "ifeval",
                "default_condition": default_condition,
                "strong_condition": strong_condition,
                "default_success_records": len(scored_by_run.get(task_runs[default_condition], [])),
                "strong_success_records": len(scored_by_run.get(task_runs[strong_condition], [])),
                "default_primary_metric_name": default_metrics["primary_metric_name"],
                "strong_primary_metric_name": strong_metrics["primary_metric_name"],
                "default_primary_metric": default_metrics["primary_metric"],
                "strong_primary_metric": strong_metrics["primary_metric"],
                "delta_primary_metric": round(strong_metrics["primary_metric"] - default_metrics["primary_metric"], 4),
                "default_secondary_metric_name": default_metrics["secondary_metric_name"],
                "strong_secondary_metric_name": strong_metrics["secondary_metric_name"],
                "default_secondary_metric": default_metrics["secondary_metric"],
                "strong_secondary_metric": strong_metrics["secondary_metric"],
                "delta_secondary_metric": round(strong_metrics["secondary_metric"] - default_metrics["secondary_metric"], 4),
                "default_primary_delta_vs_b_only": round(default_metrics["primary_metric"] - b_default_metrics["primary_metric"], 4),
                "strong_primary_delta_vs_b_only": round(strong_metrics["primary_metric"] - b_strong_metrics["primary_metric"], 4),
                "delta_of_primary_deltas": round(
                    (strong_metrics["primary_metric"] - b_strong_metrics["primary_metric"])
                    - (default_metrics["primary_metric"] - b_default_metrics["primary_metric"]),
                    4,
                ),
                "default_distance_to_b_only": round(abs(default_metrics["primary_metric"] - b_default_metrics["primary_metric"]), 4),
                "strong_distance_to_b_only": round(abs(strong_metrics["primary_metric"] - b_strong_metrics["primary_metric"]), 4),
                "improved_distance_to_b_only": abs(strong_metrics["primary_metric"] - b_strong_metrics["primary_metric"])
                < abs(default_metrics["primary_metric"] - b_default_metrics["primary_metric"]),
                "improved_primary_metric": strong_metrics["primary_metric"] > default_metrics["primary_metric"],
                "rq2_improved": (
                    abs(strong_metrics["primary_metric"] - b_strong_metrics["primary_metric"])
                    < abs(default_metrics["primary_metric"] - b_default_metrics["primary_metric"])
                ) or (strong_metrics["primary_metric"] > default_metrics["primary_metric"]),
            }
        )
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
    return {
        str(record["sample_id"]): str(record.get("response_text", ""))
        for record in records
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


def _default_prefix(persona_a: str, persona_b: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rq2_strength_{persona_a}_to_{persona_b}_{now}"


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
    lines = [
        "# RQ2 Strength Comparison",
        "",
        "## Selected Runs",
        "",
    ]
    for row in sorted(selected_rows, key=lambda item: (item["task_type"], item["condition"])):
        lines.append(
            f"- {row['task_type']} | {row['condition']} | {row['run_id']} | "
            f"{row['source_dataset']} | {row['model_name']} | n={row['sample_count']}"
        )

    lines.extend(["", "## Summary", ""])
    for row in summary_rows:
        task_type = row["task_type"]
        if task_type == "mbti_mcq":
            lines.append(
                f"- {row['default_condition']} vs {row['strong_condition']}: "
                f"OSR letter match {row['default_osr_letter_match_rate']} -> {row['strong_osr_letter_match_rate']}, "
                f"SCS {row['default_scs_vs_b_only']} -> {row['strong_scs_vs_b_only']}, "
                f"improved={row['rq2_improved']}."
            )
            continue
        if task_type == "machine_mindset":
            lines.append(
                f"- {row['default_condition']} vs {row['strong_condition']}: "
                f"mean_task_score {row['default_mean_task_score']} -> {row['strong_mean_task_score']}, "
                f"lexical SCS {row['default_scs_lexical_similarity_to_b_only']} -> {row['strong_scs_lexical_similarity_to_b_only']}, "
                f"improved={row['rq2_improved']}."
            )
            continue
        lines.append(
            f"- {row['default_condition']} vs {row['strong_condition']}: "
            f"{row['default_primary_metric_name']} {row['default_primary_metric']} -> {row['strong_primary_metric']}, "
            f"delta-vs-B_only {row['default_primary_delta_vs_b_only']} -> {row['strong_primary_delta_vs_b_only']}, "
            f"improved={row['rq2_improved']}."
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
