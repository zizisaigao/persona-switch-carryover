from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean, median
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full-run RQ1 report tables from pair-level matched-switch summaries.")
    parser.add_argument("--input-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--summary-glob", default="rq1_*_summary.csv")
    parser.add_argument("--routes-glob", default="rq1_*_overall.csv")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default="rq1_full_run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    switch_rows = _load_switch_rows(args.input_dir, args.summary_glob)
    route_rows = _load_route_rows(args.input_dir, args.routes_glob)
    if not switch_rows:
        raise SystemExit("No RQ1 switch_comparison rows found for the requested glob.")

    pair_table = [_normalize_switch_row(row) for row in switch_rows]
    overall_table = _aggregate_pair_table(pair_table)
    route_table = _normalize_route_rows(route_rows)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / f"{args.output_prefix}_pair_switch_table.csv"
    overall_path = args.output_dir / f"{args.output_prefix}_overall_by_task_track.csv"
    route_path = args.output_dir / f"{args.output_prefix}_pair_routing.csv"
    report_path = args.output_dir / f"{args.output_prefix}_report.md"

    _write_csv(pair_path, pair_table)
    _write_csv(overall_path, overall_table)
    _write_csv(route_path, route_table)
    report_path.write_text(_render_report(pair_table, overall_table, route_table), encoding="utf-8")

    print(f"wrote pair switch table -> {pair_path}")
    print(f"wrote overall table -> {overall_path}")
    print(f"wrote routing table -> {route_path}")
    print(f"wrote report -> {report_path}")


def _load_switch_rows(input_dir: Path, summary_glob: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(input_dir.glob(summary_glob)):
        for row in _read_csv(path):
            if row.get("row_type") == "switch_comparison":
                rows.append(row)
    return rows


def _load_route_rows(input_dir: Path, routes_glob: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(input_dir.glob(routes_glob)):
        for row in _read_csv(path):
            if row.get("overall_classification"):
                rows.append(row)
    return rows


def _normalize_switch_row(row: dict[str, str]) -> dict[str, Any]:
    task_type = str(row.get("task_type", ""))
    retain_mechanism = str(row.get("retain_mechanism", ""))
    base = {
        "persona_a": str(row.get("persona_a", "")),
        "persona_b": str(row.get("persona_b", "")),
        "pair_id": str(row.get("pair_id", "")),
        "task_type": task_type,
        "retain_mechanism": retain_mechanism,
        "switch_condition": str(row.get("switch_condition", "")),
        "matched_control_condition": str(row.get("matched_control_condition", "")),
        "n_common_samples": _to_int(row.get("n_common_samples")),
        "primary_metric_name": "",
        "primary_switch_value": 0.0,
        "primary_control_value": 0.0,
        "primary_gap_abs": 0.0,
        "scs_metric_name": "",
        "scs_value": 0.0,
        "rai_metric_name": "",
        "rai_value": 0.0,
        "switch_reaches_target_b": "",
        "final_type_switch": str(row.get("final_type_switch", "")),
        "target_persona_b": str(row.get("target_persona_b", "")),
    }
    if task_type == "mbti_mcq":
        base.update(
            {
                "primary_metric_name": "osr_letter_match_rate",
                "primary_switch_value": _to_float(row.get("osr_letter_match_rate")),
                "primary_control_value": _to_float(row.get("matched_control_osr_letter_match_rate")),
                "primary_gap_abs": abs(_to_float(row.get("osr_gap_vs_matched_b_control"))),
                "scs_metric_name": "scs_item_agreement_with_matched_b_control",
                "scs_value": _to_float(row.get("scs_item_agreement_with_matched_b_control")),
                "rai_metric_name": "rai_item_agreement_gap",
                "rai_value": _to_float(row.get("rai_item_agreement_gap")),
                "switch_reaches_target_b": str(row.get("final_type_switch", "")) == str(row.get("target_persona_b", "")),
            }
        )
        return base
    if task_type == "machine_mindset":
        base.update(
            {
                "primary_metric_name": str(row.get("primary_outcome_name", "")),
                "primary_switch_value": _to_float(row.get("primary_outcome_switch")),
                "primary_control_value": _to_float(row.get("primary_outcome_matched_b_control")),
                "primary_gap_abs": abs(_to_float(row.get("primary_outcome_gap_vs_matched_b_control"))),
                "scs_metric_name": "scs_predicted_agreement_with_matched_b_control",
                "scs_value": _to_float(row.get("scs_predicted_agreement_with_matched_b_control")),
                "rai_metric_name": "mean_rai_margin_a_minus_target",
                "rai_value": _to_float(row.get("mean_rai_margin_a_minus_target")),
            }
        )
        return base
    base.update(
        {
            "primary_metric_name": str(row.get("primary_outcome_name", "")),
            "primary_switch_value": _to_float(row.get("primary_outcome_switch")),
            "primary_control_value": _to_float(row.get("primary_outcome_matched_b_control")),
            "primary_gap_abs": abs(_to_float(row.get("primary_outcome_gap_vs_matched_b_control"))),
            "scs_metric_name": "scs_lexical_similarity_to_matched_b_control",
            "scs_value": _to_float(row.get("scs_lexical_similarity_to_matched_b_control")),
            "rai_metric_name": "rai_lexical_gap",
            "rai_value": _to_float(row.get("rai_lexical_gap")),
        }
    )
    return base


def _aggregate_pair_table(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["task_type"]), str(row["retain_mechanism"])), []).append(row)

    aggregates: list[dict[str, Any]] = []
    for (task_type, retain_mechanism), items in sorted(grouped.items()):
        aggregate = {
            "task_type": task_type,
            "retain_mechanism": retain_mechanism,
            "n_pairs": len(items),
            "mean_primary_gap_abs": round(mean(float(item["primary_gap_abs"]) for item in items), 4),
            "median_primary_gap_abs": round(median(float(item["primary_gap_abs"]) for item in items), 4),
            "mean_scs": round(mean(float(item["scs_value"]) for item in items), 4),
            "median_scs": round(median(float(item["scs_value"]) for item in items), 4),
            "mean_rai": round(mean(float(item["rai_value"]) for item in items), 4),
            "median_rai": round(median(float(item["rai_value"]) for item in items), 4),
            "share_rai_positive": round(mean(1.0 if float(item["rai_value"]) > 0.0 else 0.0 for item in items), 4),
        }
        if task_type == "mbti_mcq":
            aggregate["share_switch_reaches_target_b"] = round(
                mean(1.0 if bool(item["switch_reaches_target_b"]) else 0.0 for item in items),
                4,
            )
        aggregates.append(aggregate)
    return aggregates


def _normalize_route_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()
    for row in rows:
        item = {
            "persona_a": str(row.get("persona_a", "")),
            "persona_b": str(row.get("persona_b", "")),
            "pair_id": str(row.get("pair_id", "")),
            "switch_condition": str(row.get("switch_condition", "")),
            "failed_rows": _to_int(row.get("failed_rows")),
            "successful_rows": _to_int(row.get("successful_rows")),
            "total_rows": _to_int(row.get("total_rows")),
            "overall_classification": str(row.get("overall_classification", "")),
        }
        key = (item["pair_id"], item["switch_condition"], item["overall_classification"], str(item["total_rows"]))
        if key in seen:
            continue
        seen.add(key)
        normalized.append(item)
    normalized.sort(key=lambda item: (item["pair_id"], item["switch_condition"]))
    return normalized


def _render_report(
    pair_table: list[dict[str, Any]],
    overall_table: list[dict[str, Any]],
    route_table: list[dict[str, Any]],
) -> str:
    lines = ["# RQ1 Full-Run Report Tables", "", "## Coverage", ""]
    lines.append(f"- pair-task-track rows: {len(pair_table)}")
    lines.append(f"- routed pair rows: {len(route_table)}")
    lines.extend(["", "## Overall By Task And Track", ""])
    for row in overall_table:
        line = (
            f"- {row['task_type']} / {row['retain_mechanism']}: "
            f"n={row['n_pairs']}, mean_gap={row['mean_primary_gap_abs']}, "
            f"mean_scs={row['mean_scs']}, mean_rai={row['mean_rai']}"
        )
        if "share_switch_reaches_target_b" in row:
            line += f", share_switch_reaches_target_b={row['share_switch_reaches_target_b']}"
        lines.append(line)
    return "\n".join(lines) + "\n"


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


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


def _to_float(value: Any) -> float:
    if value in (None, ""):
        return 0.0
    return float(value)


def _to_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    return int(float(value))


if __name__ == "__main__":
    main()
