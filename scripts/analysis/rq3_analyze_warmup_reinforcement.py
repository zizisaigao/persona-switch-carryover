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
        "simple_switch": "A_history_to_B",
        "simple_control": "B_history_to_B",
        "reinforced_conditions": [
            ("A3_history_to_B", "B3_history_to_B", 3),
        ],
    },
    "summary": {
        "simple_switch": "A_summary_to_B",
        "simple_control": "B_summary_to_B",
        "reinforced_conditions": [
            ("A3_summary_to_B", "B3_summary_to_B", 3),
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze RQ3 by comparing simple matched-switch gaps against 9-turn reinforced-warmup matched-switch gaps.")
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
    _validate_required_classification(_load_classification_map(args.classification_file), args.required_overall_classification)
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


def _validate_required_classification(classification_map: dict[str, str], required_classification: str) -> None:
    if required_classification == "none" or not classification_map:
        return
    overall_labels = set(classification_map.values())
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
        if not all([premise_a_run, premise_b_run]):
            continue
        task_selection["A_only"] = premise_a_run
        task_selection["B_only"] = premise_b_run
        complete = True
        for track_name, track in TRACKS.items():
            for role_key in ["simple_switch", "simple_control"]:
                condition = track[role_key]
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
                task_selection[f"{track_name}:{role_key}"] = run_id
            if not complete:
                break
            for switch_condition, control_condition, repeats in track["reinforced_conditions"]:
                switch_run = select_latest_pair_run(
                    run_metadata=run_metadata,
                    scored_run_ids=scored_run_ids,
                    task_type=task_type,
                    condition=switch_condition,
                    persona_a=persona_a,
                    persona_b=persona_b,
                    model_name=model_name,
                    source_dataset=source_dataset,
                )
                control_run = select_latest_pair_run(
                    run_metadata=run_metadata,
                    scored_run_ids=scored_run_ids,
                    task_type=task_type,
                    condition=control_condition,
                    persona_a=persona_a,
                    persona_b=persona_b,
                    model_name=model_name,
                    source_dataset=source_dataset,
                )
                if not all([switch_run, control_run]):
                    complete = False
                    break
                task_selection[f"{track_name}:switch:{repeats}"] = switch_run
                task_selection[f"{track_name}:control:{repeats}"] = control_run
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
        for condition, target_persona in [("A_only", persona_a), ("B_only", persona_b)]:
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
    for condition, target_persona in [("A_only", persona_a), ("B_only", persona_b)]:
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
        simple_switch = track["simple_switch"]
        simple_control = track["simple_control"]
        simple_switch_key = f"{track_name}:simple_switch"
        simple_control_key = f"{track_name}:simple_control"
        simple_common = sorted(set(labels[simple_switch_key]) & set(labels[simple_control_key]) & set(labels["A_only"]))
        simple_scs = mean(1.0 if labels[simple_switch_key][sid] == labels[simple_control_key][sid] else 0.0 for sid in simple_common)
        simple_a = mean(1.0 if labels[simple_switch_key][sid] == labels["A_only"][sid] else 0.0 for sid in simple_common)
        simple_osr = _letter_match_rate(str(profiles[simple_switch_key]["final_type"]), persona_b)
        simple_control_osr = _letter_match_rate(str(profiles[simple_control_key]["final_type"]), persona_b)
        for reinforced_condition, control_condition, repeats in track["reinforced_conditions"]:
            reinforced_switch_key = f"{track_name}:switch:{repeats}"
            reinforced_control_key = f"{track_name}:control:{repeats}"
            reinforced_common = sorted(set(labels[reinforced_switch_key]) & set(labels[reinforced_control_key]) & set(labels["A_only"]))
            reinforced_scs = mean(1.0 if labels[reinforced_switch_key][sid] == labels[reinforced_control_key][sid] else 0.0 for sid in reinforced_common)
            reinforced_a = mean(1.0 if labels[reinforced_switch_key][sid] == labels["A_only"][sid] else 0.0 for sid in reinforced_common)
            reinforced_osr = _letter_match_rate(str(profiles[reinforced_switch_key]["final_type"]), persona_b)
            reinforced_control_osr = _letter_match_rate(str(profiles[reinforced_control_key]["final_type"]), persona_b)
            row = {
                "row_type": "reinforcement_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "mbti_mcq",
                "retain_mechanism": track_name,
                "simple_condition": simple_switch,
                "simple_matched_control_condition": simple_control,
                "reinforced_condition": reinforced_condition,
                "reinforced_matched_control_condition": control_condition,
                "reinforcement_repeats": repeats,
                "simple_osr_gap_abs_vs_matched_b_control": round(abs(simple_osr - simple_control_osr), 4),
                "reinforced_osr_gap_abs_vs_matched_b_control": round(abs(reinforced_osr - reinforced_control_osr), 4),
                "simple_scs_item_agreement_with_matched_b_control": round(simple_scs, 4),
                "reinforced_scs_item_agreement_with_matched_b_control": round(reinforced_scs, 4),
                "simple_distance_to_matched_b_control": round(1.0 - simple_scs, 4),
                "reinforced_distance_to_matched_b_control": round(1.0 - reinforced_scs, 4),
                "simple_rai_item_agreement_gap": round(simple_a - simple_scs, 4),
                "reinforced_rai_item_agreement_gap": round(reinforced_a - reinforced_scs, 4),
            }
            row["weakened_distance_to_matched_b_control"] = row["reinforced_distance_to_matched_b_control"] > row["simple_distance_to_matched_b_control"]
            row["weakened_osr_gap"] = row["reinforced_osr_gap_abs_vs_matched_b_control"] > row["simple_osr_gap_abs_vs_matched_b_control"]
            row["increased_a_influence"] = row["reinforced_rai_item_agreement_gap"] > row["simple_rai_item_agreement_gap"]
            row["rq3_weakened"] = _majority_true([row["weakened_distance_to_matched_b_control"], row["weakened_osr_gap"], row["increased_a_influence"]])
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
        simple_switch = track["simple_switch"]
        simple_control = track["simple_control"]
        simple_switch_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:simple_switch"], []))
        simple_control_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:simple_control"], []))
        a_rows = _sample_map(records_by_run.get(run_ids["A_only"], []))
        simple_common = sorted(set(simple_switch_rows) & set(simple_control_rows) & set(a_rows))
        predicted_key = "predicted_type" if "predicted_type" in next(iter(simple_switch_rows.values()), {}) else "predicted_code"
        simple_scs = mean(1.0 if simple_switch_rows[sid].get(predicted_key) == simple_control_rows[sid].get(predicted_key) else 0.0 for sid in simple_common)
        simple_a = mean(1.0 if simple_switch_rows[sid].get(predicted_key) == a_rows[sid].get(predicted_key) else 0.0 for sid in simple_common)
        simple_summary = _summarize_open_task("machine_mindset", list(simple_switch_rows.values()))
        simple_control_summary = _summarize_open_task("machine_mindset", list(simple_control_rows.values()))
        simple_rai = mean(float(simple_switch_rows[sid].get("rai_margin_a_minus_target", 0.0) or 0.0) for sid in simple_common)
        for reinforced_condition, control_condition, repeats in track["reinforced_conditions"]:
            reinforced_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:switch:{repeats}"], []))
            control_rows = _sample_map(records_by_run.get(run_ids[f"{track_name}:control:{repeats}"], []))
            reinforced_common = sorted(set(reinforced_rows) & set(control_rows) & set(a_rows))
            reinforced_scs = mean(1.0 if reinforced_rows[sid].get(predicted_key) == control_rows[sid].get(predicted_key) else 0.0 for sid in reinforced_common)
            reinforced_a = mean(1.0 if reinforced_rows[sid].get(predicted_key) == a_rows[sid].get(predicted_key) else 0.0 for sid in reinforced_common)
            reinforced_summary = _summarize_open_task("machine_mindset", list(reinforced_rows.values()))
            control_summary = _summarize_open_task("machine_mindset", list(control_rows.values()))
            reinforced_rai = mean(float(reinforced_rows[sid].get("rai_margin_a_minus_target", 0.0) or 0.0) for sid in reinforced_common)
            row = {
                "row_type": "reinforcement_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "machine_mindset",
                "retain_mechanism": track_name,
                "simple_condition": simple_switch,
                "simple_matched_control_condition": simple_control,
                "reinforced_condition": reinforced_condition,
                "reinforced_matched_control_condition": control_condition,
                "reinforcement_repeats": repeats,
                "simple_primary_gap_abs_vs_matched_b_control": round(abs(simple_summary["primary_value"] - simple_control_summary["primary_value"]), 4),
                "reinforced_primary_gap_abs_vs_matched_b_control": round(abs(reinforced_summary["primary_value"] - control_summary["primary_value"]), 4),
                "simple_scs_predicted_agreement_with_matched_b_control": round(simple_scs, 4),
                "reinforced_scs_predicted_agreement_with_matched_b_control": round(reinforced_scs, 4),
                "simple_distance_to_matched_b_control": round(1.0 - simple_scs, 4),
                "reinforced_distance_to_matched_b_control": round(1.0 - reinforced_scs, 4),
                "simple_rai_margin_a_minus_target": round(simple_rai, 4),
                "reinforced_rai_margin_a_minus_target": round(reinforced_rai, 4),
                "simple_rai_item_agreement_gap": round(simple_a - simple_scs, 4),
                "reinforced_rai_item_agreement_gap": round(reinforced_a - reinforced_scs, 4),
            }
            row["weakened_distance_to_matched_b_control"] = row["reinforced_distance_to_matched_b_control"] > row["simple_distance_to_matched_b_control"]
            row["weakened_primary_gap"] = row["reinforced_primary_gap_abs_vs_matched_b_control"] > row["simple_primary_gap_abs_vs_matched_b_control"]
            row["increased_a_influence"] = row["reinforced_rai_margin_a_minus_target"] > row["simple_rai_margin_a_minus_target"]
            row["rq3_weakened"] = _majority_true([row["weakened_distance_to_matched_b_control"], row["weakened_primary_gap"], row["increased_a_influence"]])
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
        simple_switch_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:simple_switch"], []))
        simple_control_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:simple_control"], []))
        a_texts = _sample_to_text(raw_by_run.get(run_ids["A_only"], []))
        simple_common = sorted(set(simple_switch_texts) & set(simple_control_texts) & set(a_texts))
        simple_scs = _mean_or_zero(_lexical_f1(simple_switch_texts[sid], simple_control_texts[sid]) for sid in simple_common)
        simple_a = _mean_or_zero(_lexical_f1(simple_switch_texts[sid], a_texts[sid]) for sid in simple_common)
        simple_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:simple_switch"], []))
        simple_control_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:simple_control"], []))
        for reinforced_condition, control_condition, repeats in track["reinforced_conditions"]:
            reinforced_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:switch:{repeats}"], []))
            control_texts = _sample_to_text(raw_by_run.get(run_ids[f"{track_name}:control:{repeats}"], []))
            reinforced_common = sorted(set(reinforced_texts) & set(control_texts) & set(a_texts))
            reinforced_scs = _mean_or_zero(_lexical_f1(reinforced_texts[sid], control_texts[sid]) for sid in reinforced_common)
            reinforced_a = _mean_or_zero(_lexical_f1(reinforced_texts[sid], a_texts[sid]) for sid in reinforced_common)
            reinforced_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:switch:{repeats}"], []))
            control_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[f"{track_name}:control:{repeats}"], []))
            row = {
                "row_type": "reinforcement_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "ifeval",
                "retain_mechanism": track_name,
                "simple_condition": track["simple_switch"],
                "simple_matched_control_condition": track["simple_control"],
                "reinforced_condition": reinforced_condition,
                "reinforced_matched_control_condition": control_condition,
                "reinforcement_repeats": repeats,
                "simple_primary_gap_abs_vs_matched_b_control": round(abs(simple_summary["primary_value"] - simple_control_summary["primary_value"]), 4),
                "reinforced_primary_gap_abs_vs_matched_b_control": round(abs(reinforced_summary["primary_value"] - control_summary["primary_value"]), 4),
                "simple_scs_lexical_similarity_to_matched_b_control": round(simple_scs, 4),
                "reinforced_scs_lexical_similarity_to_matched_b_control": round(reinforced_scs, 4),
                "simple_rai_lexical_gap": round(simple_a - simple_scs, 4),
                "reinforced_rai_lexical_gap": round(reinforced_a - reinforced_scs, 4),
            }
            row["weakened_distance_to_matched_b_control"] = row["reinforced_primary_gap_abs_vs_matched_b_control"] > row["simple_primary_gap_abs_vs_matched_b_control"]
            row["weakened_lexical_scs"] = row["reinforced_scs_lexical_similarity_to_matched_b_control"] < row["simple_scs_lexical_similarity_to_matched_b_control"]
            row["increased_a_influence"] = row["reinforced_rai_lexical_gap"] > row["simple_rai_lexical_gap"]
            row["rq3_weakened"] = _majority_true([row["weakened_distance_to_matched_b_control"], row["weakened_lexical_scs"], row["increased_a_influence"]])
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
    premise_rows = [row for row in summary_rows if row.get("row_type") == "premise_check"]
    compare_rows = [row for row in summary_rows if row.get("row_type") == "reinforcement_comparison"]
    lines = ["# RQ3 Reinforcement Comparison", "", "## Selected Runs", ""]
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
            f"- {row['task_type']} / {row['retain_mechanism']} / repeats={row['reinforcement_repeats']}: weakened={row['rq3_weakened']}"
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
