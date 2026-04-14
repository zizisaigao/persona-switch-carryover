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

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analysis.run_selection import (
    build_run_metadata,
    build_selection_row,
    select_latest_pair_run,
    select_latest_premise_mbti_only_run,
)
from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


TRACKS = {
    "history": {
        "default_switch": "A_history_to_B",
        "default_control": "B_history_to_B",
        "strong_switch": "A_history_to_B_strong",
        "strong_control": "B_history_to_B_strong",
    },
    "summary": {
        "default_switch": "A_summary_to_B",
        "default_control": "B_summary_to_B",
        "strong_switch": "A_summary_to_B_strong",
        "strong_control": "B_summary_to_B_strong",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze RQ2 by comparing default matched-switch gaps against strong-update matched-switch gaps.")
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
        choices=["none", "failed", "successful"],
        default="none",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    _validate_required_classification(_load_optional_csv(args.classification_file), args.required_overall_classification)
    run_metadata = build_run_metadata(raw_records)
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
        for selection_role, run_id in sorted(task_runs.items()):
            selected_rows.append(
                build_selection_row(
                    task_type=task_type,
                    selection_role=selection_role,
                    condition_label=selection_role,
                    run_id=run_id,
                    run_metadata=run_metadata,
                )
            )

        summary_rows.extend(
            _build_premise_rows(
                task_type=task_type,
                run_ids=task_runs,
                scored_records=scored_records,
                persona_a=args.persona_a,
                persona_b=args.persona_b,
            )
        )
        summary_rows.extend(
            _build_comparison_rows(
                task_type=task_type,
                run_ids=task_runs,
                raw_records=raw_records,
                scored_records=scored_records,
                success_keys=success_keys,
                persona_a=args.persona_a,
                persona_b=args.persona_b,
            )
        )

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
    if required_classification == "none" or not rows:
        return
    overall_labels = {row.get("overall_classification", "") for row in rows}
    if required_classification not in overall_labels:
        raise SystemExit(
            f"Classification file does not contain overall_classification={required_classification!r}. Found: {sorted(label for label in overall_labels if label)}"
        )


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
    selected: dict[str, dict[str, str]] = {}
    for task_type in task_types:
        task_selection: dict[str, str] = {}
        premise_a_run = select_latest_premise_mbti_only_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            premise_persona=persona_a,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        premise_b_run = select_latest_premise_mbti_only_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            premise_persona=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        strong_premise_a_run = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="MBTI_only_strong",
            persona_a=persona_a,
            persona_b=persona_a,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        strong_premise_b_run = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="MBTI_only_strong",
            persona_a=persona_b,
            persona_b=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        if not all([premise_a_run, premise_b_run, strong_premise_a_run, strong_premise_b_run]):
            continue
        task_selection["A_only"] = premise_a_run
        task_selection["B_only"] = premise_b_run
        task_selection["A_only_strong"] = strong_premise_a_run
        task_selection["B_only_strong"] = strong_premise_b_run
        complete = True
        for track_name, track in TRACKS.items():
            for role, condition in track.items():
                run_id = select_latest_pair_run(
                    run_metadata=run_metadata,
                    scored_run_ids=scored_run_ids,
                    task_type=task_type,
                    condition=condition,
                    persona_a=persona_a,
                    persona_b=persona_b,
                    model_name=model_name,
                    source_dataset=source_dataset,
                )
                if not run_id:
                    complete = False
                    break
                task_selection[f"{track_name}:{role}"] = run_id
            if not complete:
                break
        if complete:
            selected[task_type] = task_selection
    return selected


def _build_premise_rows(
    *,
    task_type: str,
    run_ids: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if task_type == "mbti_mcq":
        records_by_run = _records_by_run_id(scored_records, task_type)
        for condition, target_persona in [
            ("A_only", persona_a),
            ("B_only", persona_b),
            ("A_only_strong", persona_a),
            ("B_only_strong", persona_b),
        ]:
            aggregates = aggregate_profiles(records_by_run.get(run_ids[condition], []))
            if not aggregates:
                continue
            final_type = str(aggregates[0].get("final_type", ""))
            rows.append(
                {
                    "row_type": "premise_check",
                    "persona_a": persona_a,
                    "persona_b": persona_b,
                    "pair_id": f"{persona_a}_to_{persona_b}",
                    "task_type": task_type,
                    "premise_condition": condition,
                    "target_persona": target_persona,
                    "premise_final_type": final_type,
                    "premise_osr_letter_match_rate": round(_letter_match_rate(final_type, target_persona), 4),
                }
            )
        return rows

    records_by_run = _records_by_run_id(scored_records, task_type)
    for condition, target_persona in [
        ("A_only", persona_a),
        ("B_only", persona_b),
        ("A_only_strong", persona_a),
        ("B_only_strong", persona_b),
    ]:
        summary = _summarize_open_task(task_type, records_by_run.get(run_ids[condition], []))
        rows.append(
            {
                "row_type": "premise_check",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": task_type,
                "premise_condition": condition,
                "target_persona": target_persona,
                "primary_metric_name": summary["primary_name"],
                "primary_metric": summary["primary_value"],
                "secondary_metric_name": summary["secondary_name"],
                "secondary_metric": summary["secondary_value"],
            }
        )
    return rows


def _build_comparison_rows(
    *,
    task_type: str,
    run_ids: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    if task_type == "mbti_mcq":
        return _build_mbti_rows(run_ids, scored_records, persona_a, persona_b)
    if task_type == "machine_mindset":
        return _build_machine_mindset_rows(run_ids, scored_records, persona_a, persona_b)
    return _build_ifeval_rows(run_ids, raw_records, scored_records, success_keys, persona_a, persona_b)


def _build_mbti_rows(
    run_ids: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "mbti_mcq")
    labels: dict[str, dict[str, str | None]] = {}
    profiles: dict[str, dict[str, Any]] = {}
    for label, run_id in run_ids.items():
        run_records = records_by_run.get(run_id, [])
        labels[label] = {str(item["sample_id"]): item.get("predicted_label") for item in run_records}
        aggregates = aggregate_profiles(run_records)
        if aggregates:
            profiles[label] = aggregates[0]

    rows: list[dict[str, Any]] = []
    for track_name, track in TRACKS.items():
        default_switch = track["default_switch"]
        default_control = track["default_control"]
        strong_switch = track["strong_switch"]
        strong_control = track["strong_control"]
        default_switch_key = f"{track_name}:default_switch"
        default_control_key = f"{track_name}:default_control"
        strong_switch_key = f"{track_name}:strong_switch"
        strong_control_key = f"{track_name}:strong_control"
        common_default = sorted(set(labels[default_switch_key]) & set(labels[default_control_key]) & set(labels["A_only"]))
        common_strong = sorted(set(labels[strong_switch_key]) & set(labels[strong_control_key]) & set(labels["A_only_strong"]))
        default_scs = mean(1.0 if labels[default_switch_key][sid] == labels[default_control_key][sid] else 0.0 for sid in common_default)
        strong_scs = mean(1.0 if labels[strong_switch_key][sid] == labels[strong_control_key][sid] else 0.0 for sid in common_strong)
        default_a = mean(1.0 if labels[default_switch_key][sid] == labels["A_only"][sid] else 0.0 for sid in common_default)
        strong_a = mean(1.0 if labels[strong_switch_key][sid] == labels["A_only_strong"][sid] else 0.0 for sid in common_strong)
        default_osr = _letter_match_rate(str(profiles[default_switch_key]["final_type"]), persona_b)
        strong_osr = _letter_match_rate(str(profiles[strong_switch_key]["final_type"]), persona_b)
        default_control_osr = _letter_match_rate(str(profiles[default_control_key]["final_type"]), persona_b)
        strong_control_osr = _letter_match_rate(str(profiles[strong_control_key]["final_type"]), persona_b)
        row = {
            "row_type": "strength_comparison",
            "persona_a": persona_a,
            "persona_b": persona_b,
            "pair_id": f"{persona_a}_to_{persona_b}",
            "task_type": "mbti_mcq",
            "retain_mechanism": track_name,
            "default_switch_condition": default_switch,
            "default_matched_control_condition": default_control,
            "strong_switch_condition": strong_switch,
            "strong_matched_control_condition": strong_control,
            "default_osr_letter_match_rate": round(default_osr, 4),
            "strong_osr_letter_match_rate": round(strong_osr, 4),
            "default_osr_gap_abs_vs_matched_b_control": round(abs(default_osr - default_control_osr), 4),
            "strong_osr_gap_abs_vs_matched_b_control": round(abs(strong_osr - strong_control_osr), 4),
            "default_scs_item_agreement_with_matched_b_control": round(default_scs, 4),
            "strong_scs_item_agreement_with_matched_b_control": round(strong_scs, 4),
            "default_distance_to_matched_b_control": round(1.0 - default_scs, 4),
            "strong_distance_to_matched_b_control": round(1.0 - strong_scs, 4),
            "default_rai_item_agreement_gap": round(default_a - default_scs, 4),
            "strong_rai_item_agreement_gap": round(strong_a - strong_scs, 4),
        }
        row["improved_distance_to_matched_b_control"] = row["strong_distance_to_matched_b_control"] < row["default_distance_to_matched_b_control"]
        row["improved_osr_gap"] = row["strong_osr_gap_abs_vs_matched_b_control"] < row["default_osr_gap_abs_vs_matched_b_control"]
        row["reduced_a_influence"] = row["strong_rai_item_agreement_gap"] < row["default_rai_item_agreement_gap"]
        row["rq2_improved"] = _majority_true([row["improved_distance_to_matched_b_control"], row["improved_osr_gap"], row["reduced_a_influence"]])
        rows.append(row)
    return rows


def _build_machine_mindset_rows(
    run_ids: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "machine_mindset")
    rows: list[dict[str, Any]] = []
    for track_name, track in TRACKS.items():
        default_switch_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:default_switch"], []))
        default_control_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:default_control"], []))
        strong_switch_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:strong_switch"], []))
        strong_control_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:strong_control"], []))
        a_rows = _sample_map(records_by_run.get(run_ids["A_only"], []))
        a_rows_strong = _sample_map(records_by_run.get(run_ids["A_only_strong"], []))
        common_default = sorted(set(default_switch_rows) & set(default_control_rows) & set(a_rows))
        common_strong = sorted(set(strong_switch_rows) & set(strong_control_rows) & set(a_rows_strong))
        predicted_key = "predicted_type" if "predicted_type" in next(iter(default_switch_rows.values()), {}) else "predicted_code"
        default_scs = mean(1.0 if default_switch_rows[sid].get(predicted_key) == default_control_rows[sid].get(predicted_key) else 0.0 for sid in common_default)
        strong_scs = mean(1.0 if strong_switch_rows[sid].get(predicted_key) == strong_control_rows[sid].get(predicted_key) else 0.0 for sid in common_strong)
        default_a = mean(1.0 if default_switch_rows[sid].get(predicted_key) == a_rows[sid].get(predicted_key) else 0.0 for sid in common_default)
        strong_a = mean(1.0 if strong_switch_rows[sid].get(predicted_key) == a_rows_strong[sid].get(predicted_key) else 0.0 for sid in common_strong)
        default_summary = _summarize_open_task("machine_mindset", list(default_switch_rows.values()))
        default_control_summary = _summarize_open_task("machine_mindset", list(default_control_rows.values()))
        strong_summary = _summarize_open_task("machine_mindset", list(strong_switch_rows.values()))
        strong_control_summary = _summarize_open_task("machine_mindset", list(strong_control_rows.values()))
        default_rai = mean(float(default_switch_rows[sid].get("rai_margin_a_minus_target", 0.0) or 0.0) for sid in common_default)
        strong_rai = mean(float(strong_switch_rows[sid].get("rai_margin_a_minus_target", 0.0) or 0.0) for sid in common_strong)
        row = {
            "row_type": "strength_comparison",
            "persona_a": persona_a,
            "persona_b": persona_b,
            "pair_id": f"{persona_a}_to_{persona_b}",
            "task_type": "machine_mindset",
            "retain_mechanism": track_name,
            "default_switch_condition": track["default_switch"],
            "default_matched_control_condition": track["default_control"],
            "strong_switch_condition": track["strong_switch"],
            "strong_matched_control_condition": track["strong_control"],
            "primary_outcome_name": default_summary["primary_name"],
            "default_primary_outcome": default_summary["primary_value"],
            "strong_primary_outcome": strong_summary["primary_value"],
            "default_primary_gap_abs_vs_matched_b_control": round(abs(default_summary["primary_value"] - default_control_summary["primary_value"]), 4),
            "strong_primary_gap_abs_vs_matched_b_control": round(abs(strong_summary["primary_value"] - strong_control_summary["primary_value"]), 4),
            "default_scs_predicted_agreement_with_matched_b_control": round(default_scs, 4),
            "strong_scs_predicted_agreement_with_matched_b_control": round(strong_scs, 4),
            "default_distance_to_matched_b_control": round(1.0 - default_scs, 4),
            "strong_distance_to_matched_b_control": round(1.0 - strong_scs, 4),
            "default_rai_margin_a_minus_target": round(default_rai, 4),
            "strong_rai_margin_a_minus_target": round(strong_rai, 4),
            "default_rai_item_agreement_gap": round(default_a - default_scs, 4),
            "strong_rai_item_agreement_gap": round(strong_a - strong_scs, 4),
        }
        row["improved_distance_to_matched_b_control"] = row["strong_distance_to_matched_b_control"] < row["default_distance_to_matched_b_control"]
        row["improved_primary_gap"] = row["strong_primary_gap_abs_vs_matched_b_control"] < row["default_primary_gap_abs_vs_matched_b_control"]
        row["reduced_a_influence"] = row["strong_rai_margin_a_minus_target"] < row["default_rai_margin_a_minus_target"]
        row["rq2_improved"] = _majority_true([row["improved_distance_to_matched_b_control"], row["improved_primary_gap"], row["reduced_a_influence"]])
        rows.append(row)
    return rows


def _build_ifeval_rows(
    run_ids: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    success_keys: set[str],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, "ifeval", success_keys=success_keys)
    scored_by_run = _records_by_run_id(scored_records, "ifeval", success_keys=success_keys)
    rows: list[dict[str, Any]] = []
    for track_name, track in TRACKS.items():
        default_switch_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:default_switch"], []))
        default_control_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:default_control"], []))
        strong_switch_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:strong_switch"], []))
        strong_control_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:strong_control"], []))
        a_texts = _sample_to_text(raw_by_run.get(run_ids["A_only"], []))
        a_texts_strong = _sample_to_text(raw_by_run.get(run_ids["A_only_strong"], []))
        common_default = sorted(set(default_switch_texts) & set(default_control_texts) & set(a_texts))
        common_strong = sorted(set(strong_switch_texts) & set(strong_control_texts) & set(a_texts_strong))
        default_scs = _mean_or_zero(_lexical_f1(default_switch_texts[sid], default_control_texts[sid]) for sid in common_default)
        strong_scs = _mean_or_zero(_lexical_f1(strong_switch_texts[sid], strong_control_texts[sid]) for sid in common_strong)
        default_a = _mean_or_zero(_lexical_f1(default_switch_texts[sid], a_texts[sid]) for sid in common_default)
        strong_a = _mean_or_zero(_lexical_f1(strong_switch_texts[sid], a_texts_strong[sid]) for sid in common_strong)
        default_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:default_switch"], []))
        default_control_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:default_control"], []))
        strong_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:strong_switch"], []))
        strong_control_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:strong_control"], []))
        row = {
            "row_type": "strength_comparison",
            "persona_a": persona_a,
            "persona_b": persona_b,
            "pair_id": f"{persona_a}_to_{persona_b}",
            "task_type": "ifeval",
            "retain_mechanism": track_name,
            "default_switch_condition": track["default_switch"],
            "default_matched_control_condition": track["default_control"],
            "strong_switch_condition": track["strong_switch"],
            "strong_matched_control_condition": track["strong_control"],
            "primary_outcome_name": default_summary["primary_name"],
            "default_primary_outcome": default_summary["primary_value"],
            "strong_primary_outcome": strong_summary["primary_value"],
            "default_primary_gap_abs_vs_matched_b_control": round(abs(default_summary["primary_value"] - default_control_summary["primary_value"]), 4),
            "strong_primary_gap_abs_vs_matched_b_control": round(abs(strong_summary["primary_value"] - strong_control_summary["primary_value"]), 4),
            "default_scs_lexical_similarity_to_matched_b_control": round(default_scs, 4),
            "strong_scs_lexical_similarity_to_matched_b_control": round(strong_scs, 4),
            "default_rai_lexical_gap": round(default_a - default_scs, 4),
            "strong_rai_lexical_gap": round(strong_a - strong_scs, 4),
        }
        row["improved_distance_to_matched_b_control"] = row["strong_primary_gap_abs_vs_matched_b_control"] < row["default_primary_gap_abs_vs_matched_b_control"]
        row["improved_lexical_scs"] = row["strong_scs_lexical_similarity_to_matched_b_control"] > row["default_scs_lexical_similarity_to_matched_b_control"]
        row["reduced_a_influence"] = row["strong_rai_lexical_gap"] < row["default_rai_lexical_gap"]
        row["rq2_improved"] = _majority_true([row["improved_distance_to_matched_b_control"], row["improved_lexical_scs"], row["reduced_a_influence"]])
        rows.append(row)
    return rows


def _records_by_run_id(records: list[dict[str, Any]], task_type: str, *, success_keys: set[str] | None = None) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("task_type") != task_type:
            continue
        if success_keys is not None and _record_key(record) not in success_keys:
            continue
        grouped[str(record["run_id"])] .append(record)
    return grouped


def _sample_map(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(record["sample_id"]): record for record in records}


def _sample_to_text(records: list[dict[str, Any]]) -> dict[str, str]:
    return {str(record["sample_id"]): str(record.get("response_text", "")) for record in records}


def _summarize_open_task(task_type: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    if not records:
        return {"primary_name": "missing", "primary_value": 0.0, "secondary_name": "missing", "secondary_value": 0.0}
    if task_type == "machine_mindset":
        first = records[0]
        if "target_type_similarity" in first:
            return {
                "primary_name": "mean_target_similarity",
                "primary_value": round(mean(float(record.get("target_type_similarity", 0.0) or 0.0) for record in records), 4),
                "secondary_name": "osr_type_match_rate",
                "secondary_value": round(mean(float(bool(record.get("target_type_match"))) for record in records), 4),
            }
        return {
            "primary_name": "mean_target_similarity",
            "primary_value": round(mean(float(record.get("target_code_similarity", 0.0) or 0.0) for record in records), 4),
            "secondary_name": "osr_dimension_match_rate",
            "secondary_value": round(mean(float(bool(record.get("target_code_match"))) for record in records), 4),
        }
    official = any(record.get("checker_source") == "official_google_ifeval" for record in records)
    if not official:
        raise ValueError("IFEval scoring now requires official checker outputs. Fallback rule-based summaries are no longer supported.")
    strict_all = [1.0 if bool(record.get("strict_follow_all")) else 0.0 for record in records]
    strict_fraction = []
    for record in records:
        total = int(record.get("instruction_count", 0) or 0)
        passed = int(record.get("strict_checks_passed", 0) or 0)
        strict_fraction.append((passed / total) if total else 0.0)
    return {
        "primary_name": "strict_follow_all_rate",
        "primary_value": round(mean(strict_all), 4),
        "secondary_name": "mean_strict_instruction_fraction",
        "secondary_value": round(mean(strict_fraction), 4),
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


def _majority_true(votes: list[bool]) -> bool:
    return sum(1 for vote in votes if vote) >= 2


def _mean_or_zero(values: Any) -> float:
    collected = list(values)
    return mean(collected) if collected else 0.0


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
    premise_rows = [row for row in summary_rows if row.get("row_type") == "premise_check"]
    compare_rows = [row for row in summary_rows if row.get("row_type") == "strength_comparison"]
    lines = ["# RQ2 Strength Comparison", "", "## Selected Runs", ""]
    for row in sorted(selected_rows, key=lambda item: (item["task_type"], item["selection_role"])):
        lines.append(
            f"- {row['task_type']} | {row['selection_role']} | {row['run_id']} | {row['source_dataset']} | {row['model_name']} | n={row['sample_count']}"
        )
    lines.extend(["", "## Premise Checks", ""])
    for row in premise_rows:
        lines.append(
            f"- {row['task_type']} / {row['premise_condition']}: {row['primary_metric_name'] if 'primary_metric_name' in row else 'letter_match'}={row.get('primary_metric', row.get('premise_osr_letter_match_rate', ''))}"
        )
    lines.extend(["", "## Summary", ""])
    for row in compare_rows:
        lines.append(
            f"- {row['task_type']} / {row['retain_mechanism']}: improved={row['rq2_improved']}"
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
