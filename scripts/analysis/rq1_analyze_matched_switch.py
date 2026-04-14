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


SWITCH_TO_CONTROL = {
    "A_history_to_B": "B_history_to_B",
    "A_summary_to_B": "B_summary_to_B",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze RQ1 matched-switch results by comparing A->B against matched B->B controls.")
    parser.add_argument("--persona-a", required=True, help="Warm-up persona A to analyze.")
    parser.add_argument("--persona-b", required=True, help="Evaluation persona B to analyze.")
    parser.add_argument(
        "--task-types",
        nargs="+",
        default=["mbti_mcq", "machine_mindset", "ifeval"],
        help="Task types to include.",
    )
    parser.add_argument("--model-name", default=None, help="Optional model name filter.")
    parser.add_argument("--source-dataset", default=None, help="Optional source dataset filter.")
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    run_metadata = build_run_metadata(raw_records)
    scored_run_ids = {str(record["run_id"]) for record in scored_records}

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
    selection_rows: list[dict[str, Any]] = []
    for task_type in args.task_types:
        task_runs = selected_runs.get(task_type, {})
        if not task_runs:
            continue

        for selection_role, run_id in sorted(task_runs.items()):
            selection_rows.append(
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
                raw_records=raw_records,
                scored_records=scored_records,
                persona_a=args.persona_a,
                persona_b=args.persona_b,
            )
        )
        summary_rows.extend(
            _build_switch_rows(
                task_type=task_type,
                run_ids=task_runs,
                raw_records=raw_records,
                scored_records=scored_records,
                persona_a=args.persona_a,
                persona_b=args.persona_b,
            )
        )

    if not summary_rows:
        raise SystemExit("No complete task groups found for the requested filters.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or _default_prefix(args.persona_a, args.persona_b)
    csv_path = args.output_dir / f"{prefix}_summary.csv"
    md_path = args.output_dir / f"{prefix}_report.md"
    runs_path = args.output_dir / f"{prefix}_selected_runs.csv"
    _write_csv(csv_path, summary_rows)
    _write_csv(runs_path, selection_rows)
    md_path.write_text(_render_report(args.persona_a, args.persona_b, summary_rows, selection_rows), encoding="utf-8")

    print(f"wrote summary -> {csv_path}")
    print(f"wrote selected runs -> {runs_path}")
    print(f"wrote report -> {md_path}")


def _load_scored_records(scored_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(scored_dir.glob("*_scores.jsonl")):
        records.extend(read_jsonl(path))
    return records


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
        history_switch = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="A_history_to_B",
            persona_a=persona_a,
            persona_b=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        summary_switch = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="A_summary_to_B",
            persona_a=persona_a,
            persona_b=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        history_control = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="B_history_to_B",
            persona_a=persona_a,
            persona_b=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        summary_control = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type=task_type,
            condition="B_summary_to_B",
            persona_a=persona_a,
            persona_b=persona_b,
            model_name=model_name,
            source_dataset=source_dataset,
        )
        if all([premise_a_run, premise_b_run, history_switch, history_control, summary_switch, summary_control]):
            selected[task_type] = {
                "A_only": premise_a_run,
                "B_only": premise_b_run,
                "A_history_to_B": history_switch,
                "B_history_to_B": history_control,
                "A_summary_to_B": summary_switch,
                "B_summary_to_B": summary_control,
            }
    return selected


def _build_premise_rows(
    *,
    task_type: str,
    run_ids: dict[str, str],
    raw_records: list[dict[str, Any]],
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
            profile = aggregates[0]
            final_type = str(profile.get("final_type", ""))
            rows.append(
                {
                    "row_type": "premise_check",
                    "persona_a": persona_a,
                    "persona_b": persona_b,
                    "pair_id": f"{persona_a}_to_{persona_b}",
                    "task_type": task_type,
                    "premise_condition": condition,
                    "target_persona": target_persona,
                    "items_scored": profile.get("items_scored", 0),
                    "premise_final_type": final_type,
                    "premise_osr_final_type_match_target": int(final_type == target_persona),
                    "premise_osr_letter_match_rate": round(_letter_match_rate(final_type, target_persona), 4),
                }
            )
        return rows

    records_by_run = _records_by_run_id(scored_records, task_type)
    for condition, target_persona in [("A_only", persona_a), ("B_only", persona_b)]:
        records = records_by_run.get(run_ids[condition], [])
        summary = _summarize_open_task(task_type, records)
        rows.append(
            {
                "row_type": "premise_check",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": task_type,
                "premise_condition": condition,
                "target_persona": target_persona,
                "n_records": len(records),
                "primary_metric_name": summary["primary_name"],
                "primary_metric": summary["primary_value"],
                "secondary_metric_name": summary["secondary_name"],
                "secondary_metric": summary["secondary_value"],
            }
        )
    return rows


def _build_switch_rows(
    *,
    task_type: str,
    run_ids: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    if task_type == "mbti_mcq":
        return _build_mbti_switch_rows(run_ids, scored_records, persona_a, persona_b)
    if task_type == "machine_mindset":
        return _build_machine_mindset_switch_rows(run_ids, scored_records, persona_a, persona_b)
    return _build_ifeval_switch_rows(run_ids, raw_records, scored_records, persona_a, persona_b)


def _build_mbti_switch_rows(
    run_ids: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "mbti_mcq")
    profiles: dict[str, dict[str, Any]] = {}
    labels: dict[str, dict[str, str | None]] = {}
    for condition, run_id in run_ids.items():
        run_records = records_by_run.get(run_id, [])
        aggregates = aggregate_profiles(run_records)
        if not aggregates:
            continue
        profiles[condition] = aggregates[0]
        labels[condition] = {str(item["sample_id"]): item.get("predicted_label") for item in run_records}

    rows: list[dict[str, Any]] = []
    for switch_condition, matched_control in SWITCH_TO_CONTROL.items():
        common_ids = sorted(
            set(labels.get("A_only", {}))
            & set(labels.get("B_only", {}))
            & set(labels.get(switch_condition, {}))
            & set(labels.get(matched_control, {}))
        )
        if not common_ids:
            continue
        agreement_with_control = mean(
            1.0 if labels[switch_condition][sample_id] == labels[matched_control][sample_id] else 0.0
            for sample_id in common_ids
        )
        agreement_with_a = mean(
            1.0 if labels[switch_condition][sample_id] == labels["A_only"][sample_id] else 0.0
            for sample_id in common_ids
        )
        switch_type = str(profiles[switch_condition]["final_type"])
        control_type = str(profiles[matched_control]["final_type"])
        switch_osr = _letter_match_rate(switch_type, persona_b)
        control_osr = _letter_match_rate(control_type, persona_b)
        rows.append(
            {
                "row_type": "switch_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "mbti_mcq",
                "switch_condition": switch_condition,
                "matched_control_condition": matched_control,
                "retain_mechanism": "history" if "history" in switch_condition else "summary",
                "n_common_samples": len(common_ids),
                "final_type_switch": switch_type,
                "final_type_matched_b_control": control_type,
                "target_persona_b": persona_b,
                "osr_final_type_match_target_b": int(switch_type == persona_b),
                "osr_letter_match_rate": round(switch_osr, 4),
                "matched_control_osr_letter_match_rate": round(control_osr, 4),
                "osr_gap_vs_matched_b_control": round(switch_osr - control_osr, 4),
                "scs_item_agreement_with_matched_b_control": round(agreement_with_control, 4),
                "agreement_with_a_premise": round(agreement_with_a, 4),
                "rai_item_agreement_gap": round(agreement_with_a - agreement_with_control, 4),
                "notes": "Positive RAI means the switched run stayed closer to the A premise than to the matched B->B control.",
            }
        )
    return rows


def _build_machine_mindset_switch_rows(
    run_ids: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, "machine_mindset")
    rows: list[dict[str, Any]] = []
    for switch_condition, matched_control in SWITCH_TO_CONTROL.items():
        switch_rows = _sample_map(records_by_run.get(run_ids[switch_condition], []))
        control_rows = _sample_map(records_by_run.get(run_ids[matched_control], []))
        a_rows = _sample_map(records_by_run.get(run_ids["A_only"], []))
        b_rows = records_by_run.get(run_ids["B_only"], [])
        common_ids = sorted(set(switch_rows) & set(control_rows) & set(a_rows))
        if not common_ids:
            continue

        switch_summary = _summarize_open_task("machine_mindset", list(switch_rows.values()))
        control_summary = _summarize_open_task("machine_mindset", list(control_rows.values()))
        premise_a_summary = _summarize_open_task("machine_mindset", list(a_rows.values()))
        premise_b_summary = _summarize_open_task("machine_mindset", b_rows)
        predicted_key = "predicted_type" if "predicted_type" in next(iter(switch_rows.values()), {}) else "predicted_code"
        agreement_with_control = mean(
            1.0 if switch_rows[sample_id].get(predicted_key) == control_rows[sample_id].get(predicted_key) else 0.0
            for sample_id in common_ids
        )
        agreement_with_a = mean(
            1.0 if switch_rows[sample_id].get(predicted_key) == a_rows[sample_id].get(predicted_key) else 0.0
            for sample_id in common_ids
        )
        rai_margin = mean(float(switch_rows[sample_id].get("rai_margin_a_minus_target", 0.0) or 0.0) for sample_id in common_ids)
        rows.append(
            {
                "row_type": "switch_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "machine_mindset",
                "switch_condition": switch_condition,
                "matched_control_condition": matched_control,
                "retain_mechanism": "history" if "history" in switch_condition else "summary",
                "n_common_samples": len(common_ids),
                "primary_outcome_name": switch_summary["primary_name"],
                "primary_outcome_A_premise": premise_a_summary["primary_value"],
                "primary_outcome_B_premise": premise_b_summary["primary_value"],
                "primary_outcome_switch": switch_summary["primary_value"],
                "primary_outcome_matched_b_control": control_summary["primary_value"],
                "primary_outcome_gap_vs_matched_b_control": round(switch_summary["primary_value"] - control_summary["primary_value"], 4),
                "secondary_outcome_name": switch_summary["secondary_name"],
                "secondary_outcome_switch": switch_summary["secondary_value"],
                "secondary_outcome_matched_b_control": control_summary["secondary_value"],
                "secondary_outcome_gap_vs_matched_b_control": round(switch_summary["secondary_value"] - control_summary["secondary_value"], 4),
                "scs_predicted_agreement_with_matched_b_control": round(agreement_with_control, 4),
                "agreement_with_a_premise": round(agreement_with_a, 4),
                "mean_rai_margin_a_minus_target": round(rai_margin, 4),
                "notes": "Positive mean RAI margin means the response stayed closer to A than to the target B reference bank.",
            }
        )
    return rows


def _build_ifeval_switch_rows(
    run_ids: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    persona_a: str,
    persona_b: str,
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, "ifeval")
    scored_by_run = _records_by_run_id(scored_records, "ifeval")
    rows: list[dict[str, Any]] = []
    for switch_condition, matched_control in SWITCH_TO_CONTROL.items():
        switch_texts = _sample_to_text(raw_by_run.get(run_ids[switch_condition], []))
        control_texts = _sample_to_text(raw_by_run.get(run_ids[matched_control], []))
        a_texts = _sample_to_text(raw_by_run.get(run_ids["A_only"], []))
        common_ids = sorted(set(switch_texts) & set(control_texts) & set(a_texts))
        lexical_to_control = [_lexical_f1(switch_texts[sample_id], control_texts[sample_id]) for sample_id in common_ids]
        lexical_to_a = [_lexical_f1(switch_texts[sample_id], a_texts[sample_id]) for sample_id in common_ids]
        switch_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[switch_condition], []))
        control_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids[matched_control], []))
        a_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids["A_only"], []))
        b_summary = _summarize_open_task("ifeval", scored_by_run.get(run_ids["B_only"], []))
        rows.append(
            {
                "row_type": "switch_comparison",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "task_type": "ifeval",
                "switch_condition": switch_condition,
                "matched_control_condition": matched_control,
                "retain_mechanism": "history" if "history" in switch_condition else "summary",
                "n_common_samples": len(common_ids),
                "primary_outcome_name": switch_summary["primary_name"],
                "primary_outcome_A_premise": a_summary["primary_value"],
                "primary_outcome_B_premise": b_summary["primary_value"],
                "primary_outcome_switch": switch_summary["primary_value"],
                "primary_outcome_matched_b_control": control_summary["primary_value"],
                "primary_outcome_gap_vs_matched_b_control": round(switch_summary["primary_value"] - control_summary["primary_value"], 4),
                "secondary_outcome_name": switch_summary["secondary_name"],
                "secondary_outcome_switch": switch_summary["secondary_value"],
                "secondary_outcome_matched_b_control": control_summary["secondary_value"],
                "secondary_outcome_gap_vs_matched_b_control": round(switch_summary["secondary_value"] - control_summary["secondary_value"], 4),
                "scs_lexical_similarity_to_matched_b_control": round(mean(lexical_to_control), 4) if lexical_to_control else 0.0,
                "lexical_similarity_to_a_premise": round(mean(lexical_to_a), 4) if lexical_to_a else 0.0,
                "rai_lexical_gap": round(mean(lexical_to_a) - mean(lexical_to_control), 4) if lexical_to_control else 0.0,
                "notes": "Positive RAI means the switched run stayed closer to the A premise than to the matched B->B control.",
            }
        )
    return rows


def _records_by_run_id(records: list[dict[str, Any]], task_type: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("task_type") != task_type:
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


def _default_prefix(persona_a: str, persona_b: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rq1_triplet_{persona_a}_to_{persona_b}_{now}"


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


def _render_report(persona_a: str, persona_b: str, summary_rows: list[dict[str, Any]], selection_rows: list[dict[str, Any]]) -> str:
    premise_rows = [row for row in summary_rows if row.get("row_type") == "premise_check"]
    switch_rows = [row for row in summary_rows if row.get("row_type") == "switch_comparison"]
    lines = [
        f"# RQ1 Summary: {persona_a} -> {persona_b}",
        "",
        "## Selected Runs",
        "",
    ]
    for row in sorted(selection_rows, key=lambda item: (item["task_type"], item["selection_role"])):
        lines.append(
            f"- {row['task_type']} | {row['selection_role']} | {row['run_id']} | "
            f"{row['source_dataset']} | {row['model_name']} | n={row['sample_count']}"
        )

    lines.extend(["", "## Premise Checks", ""])
    for row in premise_rows:
        if row["task_type"] == "mbti_mcq":
            lines.append(
                f"- {row['task_type']} / {row['premise_condition']}: final_type={row['premise_final_type']}, "
                f"letter-match={row['premise_osr_letter_match_rate']}."
            )
        else:
            lines.append(
                f"- {row['task_type']} / {row['premise_condition']}: "
                f"{row['primary_metric_name']}={row['primary_metric']}, {row['secondary_metric_name']}={row['secondary_metric']}."
            )

    lines.extend(["", "## Switch Comparisons", ""])
    for row in switch_rows:
        if row["task_type"] == "mbti_mcq":
            lines.append(
                f"- {row['switch_condition']} vs {row['matched_control_condition']}: "
                f"OSR={row['osr_letter_match_rate']} vs control={row['matched_control_osr_letter_match_rate']}, "
                f"SCS={row['scs_item_agreement_with_matched_b_control']}, RAI={row['rai_item_agreement_gap']}."
            )
        elif row["task_type"] == "machine_mindset":
            lines.append(
                f"- {row['switch_condition']} vs {row['matched_control_condition']}: "
                f"{row['primary_outcome_name']}={row['primary_outcome_switch']} vs control={row['primary_outcome_matched_b_control']}, "
                f"predicted-agreement={row['scs_predicted_agreement_with_matched_b_control']}, "
                f"RAI={row['mean_rai_margin_a_minus_target']}."
            )
        else:
            lines.append(
                f"- {row['switch_condition']} vs {row['matched_control_condition']}: "
                f"{row['primary_outcome_name']}={row['primary_outcome_switch']} vs control={row['primary_outcome_matched_b_control']}, "
                f"lexical-SCS={row['scs_lexical_similarity_to_matched_b_control']}, RAI={row['rai_lexical_gap']}."
            )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
