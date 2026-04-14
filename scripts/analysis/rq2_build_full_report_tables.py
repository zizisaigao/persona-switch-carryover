from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean, median
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full-run RQ2 report tables from pair-level strong-update summaries.")
    parser.add_argument("--input-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--summary-glob", default="rq2_*_summary.csv")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default="rq2_full_run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _load_rows(args.input_dir, args.summary_glob)
    if not rows:
        raise SystemExit("No RQ2 strength_comparison rows found for the requested glob.")

    pair_table = [_normalize_row(row) for row in rows]
    overall_table = _aggregate_pair_table(pair_table)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / f"{args.output_prefix}_pair_update_table.csv"
    overall_path = args.output_dir / f"{args.output_prefix}_overall_by_task_track.csv"
    report_path = args.output_dir / f"{args.output_prefix}_report.md"

    _write_csv(pair_path, pair_table)
    _write_csv(overall_path, overall_table)
    report_path.write_text(_render_report(pair_table, overall_table), encoding="utf-8")

    print(f"wrote pair update table -> {pair_path}")
    print(f"wrote overall table -> {overall_path}")
    print(f"wrote report -> {report_path}")


def _load_rows(input_dir: Path, summary_glob: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(input_dir.glob(summary_glob)):
        for row in _read_csv(path):
            if row.get("row_type") == "strength_comparison":
                rows.append(row)
    return rows


def _normalize_row(row: dict[str, str]) -> dict[str, Any]:
    task_type = str(row.get("task_type", ""))
    if task_type == "mbti_mcq":
        primary_name = "osr_gap_abs_vs_matched_b_control"
        default_primary_gap_abs = _to_float(row.get("default_osr_gap_abs_vs_matched_b_control"))
        strong_primary_gap_abs = _to_float(row.get("strong_osr_gap_abs_vs_matched_b_control"))
        default_scs = _to_float(row.get("default_scs_item_agreement_with_matched_b_control"))
        strong_scs = _to_float(row.get("strong_scs_item_agreement_with_matched_b_control"))
        default_rai = _to_float(row.get("default_rai_item_agreement_gap"))
        strong_rai = _to_float(row.get("strong_rai_item_agreement_gap"))
    elif task_type == "machine_mindset":
        primary_name = "primary_gap_abs_vs_matched_b_control"
        default_primary_gap_abs = _to_float(row.get("default_primary_gap_abs_vs_matched_b_control"))
        strong_primary_gap_abs = _to_float(row.get("strong_primary_gap_abs_vs_matched_b_control"))
        default_scs = _to_float(row.get("default_scs_predicted_agreement_with_matched_b_control"))
        strong_scs = _to_float(row.get("strong_scs_predicted_agreement_with_matched_b_control"))
        default_rai = _to_float(row.get("default_rai_margin_a_minus_target"))
        strong_rai = _to_float(row.get("strong_rai_margin_a_minus_target"))
    else:
        primary_name = "primary_gap_abs_vs_matched_b_control"
        default_primary_gap_abs = _to_float(row.get("default_primary_gap_abs_vs_matched_b_control"))
        strong_primary_gap_abs = _to_float(row.get("strong_primary_gap_abs_vs_matched_b_control"))
        default_scs = _to_float(row.get("default_scs_lexical_similarity_to_matched_b_control"))
        strong_scs = _to_float(row.get("strong_scs_lexical_similarity_to_matched_b_control"))
        default_rai = _to_float(row.get("default_rai_lexical_gap"))
        strong_rai = _to_float(row.get("strong_rai_lexical_gap"))
    return {
        "persona_a": str(row.get("persona_a", "")),
        "persona_b": str(row.get("persona_b", "")),
        "pair_id": str(row.get("pair_id", "")),
        "task_type": task_type,
        "retain_mechanism": str(row.get("retain_mechanism", "")),
        "default_switch_condition": str(row.get("default_switch_condition", "")),
        "default_matched_control_condition": str(row.get("default_matched_control_condition", "")),
        "strong_switch_condition": str(row.get("strong_switch_condition", "")),
        "strong_matched_control_condition": str(row.get("strong_matched_control_condition", "")),
        "primary_gap_metric_name": primary_name,
        "default_primary_gap_abs": default_primary_gap_abs,
        "strong_primary_gap_abs": strong_primary_gap_abs,
        "primary_gap_change": round(strong_primary_gap_abs - default_primary_gap_abs, 4),
        "default_scs": default_scs,
        "strong_scs": strong_scs,
        "scs_change": round(strong_scs - default_scs, 4),
        "default_rai": default_rai,
        "strong_rai": strong_rai,
        "rai_change": round(strong_rai - default_rai, 4),
        "improved_distance_to_matched_b_control": _to_bool(row.get("improved_distance_to_matched_b_control")),
        "improved_primary_gap": _to_bool(row.get("improved_primary_gap", row.get("improved_osr_gap"))),
        "reduced_a_influence": _to_bool(row.get("reduced_a_influence")),
        "rq2_improved": _to_bool(row.get("rq2_improved")),
    }


def _aggregate_pair_table(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["task_type"]), str(row["retain_mechanism"])), []).append(row)

    aggregates: list[dict[str, Any]] = []
    for (task_type, retain_mechanism), items in sorted(grouped.items()):
        aggregates.append(
            {
                "task_type": task_type,
                "retain_mechanism": retain_mechanism,
                "n_pairs": len(items),
                "share_rq2_improved": round(mean(1.0 if bool(item["rq2_improved"]) else 0.0 for item in items), 4),
                "mean_default_primary_gap_abs": round(mean(float(item["default_primary_gap_abs"]) for item in items), 4),
                "mean_strong_primary_gap_abs": round(mean(float(item["strong_primary_gap_abs"]) for item in items), 4),
                "mean_primary_gap_change": round(mean(float(item["primary_gap_change"]) for item in items), 4),
                "median_primary_gap_change": round(median(float(item["primary_gap_change"]) for item in items), 4),
                "mean_default_scs": round(mean(float(item["default_scs"]) for item in items), 4),
                "mean_strong_scs": round(mean(float(item["strong_scs"]) for item in items), 4),
                "mean_scs_change": round(mean(float(item["scs_change"]) for item in items), 4),
                "mean_default_rai": round(mean(float(item["default_rai"]) for item in items), 4),
                "mean_strong_rai": round(mean(float(item["strong_rai"]) for item in items), 4),
                "mean_rai_change": round(mean(float(item["rai_change"]) for item in items), 4),
            }
        )
    return aggregates


def _render_report(pair_table: list[dict[str, Any]], overall_table: list[dict[str, Any]]) -> str:
    lines = ["# RQ2 Full-Run Report Tables", "", "## Coverage", ""]
    lines.append(f"- pair-task-track rows: {len(pair_table)}")
    lines.extend(["", "## Overall By Task And Track", ""])
    for row in overall_table:
        lines.append(
            f"- {row['task_type']} / {row['retain_mechanism']}: "
            f"n={row['n_pairs']}, share_rq2_improved={row['share_rq2_improved']}, "
            f"mean_gap_change={row['mean_primary_gap_change']}, mean_scs_change={row['mean_scs_change']}, mean_rai_change={row['mean_rai_change']}"
        )
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


def _to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


if __name__ == "__main__":
    main()
