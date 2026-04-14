from __future__ import annotations

import argparse
import csv
from pathlib import Path
from statistics import mean, median
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full-run RQ3 report tables from pair-level warmup-reinforcement summaries.")
    parser.add_argument("--input-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--summary-glob", default="rq3_*_summary.csv")
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default="rq3_full_run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _load_rows(args.input_dir, args.summary_glob)
    if not rows:
        raise SystemExit("No RQ3 reinforcement_comparison rows found for the requested glob.")

    pair_table = [_normalize_row(row) for row in rows]
    overall_table = _aggregate_pair_table(pair_table)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / f"{args.output_prefix}_pair_reinforcement_table.csv"
    overall_path = args.output_dir / f"{args.output_prefix}_overall_by_task_track.csv"
    report_path = args.output_dir / f"{args.output_prefix}_report.md"

    _write_csv(pair_path, pair_table)
    _write_csv(overall_path, overall_table)
    report_path.write_text(_render_report(pair_table, overall_table), encoding="utf-8")

    print(f"wrote pair reinforcement table -> {pair_path}")
    print(f"wrote overall table -> {overall_path}")
    print(f"wrote report -> {report_path}")


def _load_rows(input_dir: Path, summary_glob: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(input_dir.glob(summary_glob)):
        for row in _read_csv(path):
            if row.get("row_type") == "reinforcement_comparison":
                rows.append(row)
    return rows


def _normalize_row(row: dict[str, str]) -> dict[str, Any]:
    task_type = str(row.get("task_type", ""))
    if task_type == "mbti_mcq":
        primary_name = "osr_gap_abs_vs_matched_b_control"
        simple_primary_gap_abs = _to_float(row.get("simple_osr_gap_abs_vs_matched_b_control"))
        reinforced_primary_gap_abs = _to_float(row.get("reinforced_osr_gap_abs_vs_matched_b_control"))
        simple_scs = _to_float(row.get("simple_scs_item_agreement_with_matched_b_control"))
        reinforced_scs = _to_float(row.get("reinforced_scs_item_agreement_with_matched_b_control"))
        simple_rai = _to_float(row.get("simple_rai_item_agreement_gap"))
        reinforced_rai = _to_float(row.get("reinforced_rai_item_agreement_gap"))
    elif task_type == "machine_mindset":
        primary_name = "primary_gap_abs_vs_matched_b_control"
        simple_primary_gap_abs = _to_float(row.get("simple_primary_gap_abs_vs_matched_b_control"))
        reinforced_primary_gap_abs = _to_float(row.get("reinforced_primary_gap_abs_vs_matched_b_control"))
        simple_scs = _to_float(row.get("simple_scs_predicted_agreement_with_matched_b_control"))
        reinforced_scs = _to_float(row.get("reinforced_scs_predicted_agreement_with_matched_b_control"))
        simple_rai = _to_float(row.get("simple_rai_margin_a_minus_target"))
        reinforced_rai = _to_float(row.get("reinforced_rai_margin_a_minus_target"))
    else:
        primary_name = "primary_gap_abs_vs_matched_b_control"
        simple_primary_gap_abs = _to_float(row.get("simple_primary_gap_abs_vs_matched_b_control"))
        reinforced_primary_gap_abs = _to_float(row.get("reinforced_primary_gap_abs_vs_matched_b_control"))
        simple_scs = _to_float(row.get("simple_scs_lexical_similarity_to_matched_b_control"))
        reinforced_scs = _to_float(row.get("reinforced_scs_lexical_similarity_to_matched_b_control"))
        simple_rai = _to_float(row.get("simple_rai_lexical_gap"))
        reinforced_rai = _to_float(row.get("reinforced_rai_lexical_gap"))
    return {
        "persona_a": str(row.get("persona_a", "")),
        "persona_b": str(row.get("persona_b", "")),
        "pair_id": str(row.get("pair_id", "")),
        "task_type": task_type,
        "retain_mechanism": str(row.get("retain_mechanism", "")),
        "simple_condition": str(row.get("simple_condition", "")),
        "simple_matched_control_condition": str(row.get("simple_matched_control_condition", "")),
        "reinforced_condition": str(row.get("reinforced_condition", "")),
        "reinforced_matched_control_condition": str(row.get("reinforced_matched_control_condition", "")),
        "reinforcement_repeats": _to_int(row.get("reinforcement_repeats")),
        "primary_gap_metric_name": primary_name,
        "simple_primary_gap_abs": simple_primary_gap_abs,
        "reinforced_primary_gap_abs": reinforced_primary_gap_abs,
        "primary_gap_change": round(reinforced_primary_gap_abs - simple_primary_gap_abs, 4),
        "simple_scs": simple_scs,
        "reinforced_scs": reinforced_scs,
        "scs_change": round(reinforced_scs - simple_scs, 4),
        "simple_rai": simple_rai,
        "reinforced_rai": reinforced_rai,
        "rai_change": round(reinforced_rai - simple_rai, 4),
        "weakened_distance_to_matched_b_control": _to_bool(row.get("weakened_distance_to_matched_b_control")),
        "weakened_primary_gap": _to_bool(row.get("weakened_primary_gap", row.get("weakened_osr_gap"))),
        "increased_a_influence": _to_bool(row.get("increased_a_influence")),
        "rq3_weakened": _to_bool(row.get("rq3_weakened")),
    }


def _aggregate_pair_table(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, int], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["task_type"]), str(row["retain_mechanism"]), int(row["reinforcement_repeats"])), []).append(row)

    aggregates: list[dict[str, Any]] = []
    for (task_type, retain_mechanism, repeats), items in sorted(grouped.items()):
        aggregates.append(
            {
                "task_type": task_type,
                "retain_mechanism": retain_mechanism,
                "reinforcement_repeats": repeats,
                "n_pairs": len(items),
                "share_rq3_weakened": round(mean(1.0 if bool(item["rq3_weakened"]) else 0.0 for item in items), 4),
                "mean_simple_primary_gap_abs": round(mean(float(item["simple_primary_gap_abs"]) for item in items), 4),
                "mean_reinforced_primary_gap_abs": round(mean(float(item["reinforced_primary_gap_abs"]) for item in items), 4),
                "mean_primary_gap_change": round(mean(float(item["primary_gap_change"]) for item in items), 4),
                "median_primary_gap_change": round(median(float(item["primary_gap_change"]) for item in items), 4),
                "mean_simple_scs": round(mean(float(item["simple_scs"]) for item in items), 4),
                "mean_reinforced_scs": round(mean(float(item["reinforced_scs"]) for item in items), 4),
                "mean_scs_change": round(mean(float(item["scs_change"]) for item in items), 4),
                "mean_simple_rai": round(mean(float(item["simple_rai"]) for item in items), 4),
                "mean_reinforced_rai": round(mean(float(item["reinforced_rai"]) for item in items), 4),
                "mean_rai_change": round(mean(float(item["rai_change"]) for item in items), 4),
            }
        )
    return aggregates


def _render_report(pair_table: list[dict[str, Any]], overall_table: list[dict[str, Any]]) -> str:
    lines = ["# RQ3 Full-Run Report Tables", "", "## Coverage", ""]
    lines.append(f"- pair-task-track rows: {len(pair_table)}")
    lines.extend(["", "## Overall By Task, Track, And Reinforcement Level", ""])
    for row in overall_table:
        lines.append(
            f"- {row['task_type']} / {row['retain_mechanism']} / repeats={row['reinforcement_repeats']}: "
            f"n={row['n_pairs']}, share_rq3_weakened={row['share_rq3_weakened']}, "
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


def _to_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    return int(float(value))


def _to_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


if __name__ == "__main__":
    main()
