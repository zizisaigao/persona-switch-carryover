from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Classify RQ1 switch outcomes as failed or successful.")
    parser.add_argument("--summary-file", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    parser.add_argument("--min-mbti-osr-letter-match", type=float, default=0.75)
    parser.add_argument("--min-mbti-scs", type=float, default=0.75)
    parser.add_argument("--max-mbti-rai-gap", type=float, default=0.0)
    parser.add_argument("--min-open-scs", type=float, default=0.6)
    parser.add_argument("--max-open-rai-gap", type=float, default=0.0)
    parser.add_argument("--max-open-primary-delta-abs", type=float, default=0.15)
    parser.add_argument(
        "--overall-rule",
        choices=["any_failed", "majority_failed", "all_failed"],
        default="any_failed",
        help="How to aggregate row-level classifications into a pair-level failed/successful label.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _read_csv(args.summary_file)
    if not rows:
        raise SystemExit(f"No rows found in {args.summary_file}")

    classified_rows = [
        _classify_row(
            row,
            min_mbti_osr_letter_match=args.min_mbti_osr_letter_match,
            min_mbti_scs=args.min_mbti_scs,
            max_mbti_rai_gap=args.max_mbti_rai_gap,
            min_open_scs=args.min_open_scs,
            max_open_rai_gap=args.max_open_rai_gap,
            max_open_primary_delta_abs=args.max_open_primary_delta_abs,
        )
        for row in rows
    ]
    overall_rows = _summarize_overall(classified_rows, args.overall_rule)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or args.summary_file.stem.replace("_summary", "_classification")
    row_path = args.output_dir / f"{prefix}_rows.csv"
    overall_path = args.output_dir / f"{prefix}_overall.csv"
    _write_csv(row_path, classified_rows)
    _write_csv(overall_path, overall_rows)

    print(f"wrote row classifications -> {row_path}")
    print(f"wrote overall classifications -> {overall_path}")


def _classify_row(
    row: dict[str, str],
    *,
    min_mbti_osr_letter_match: float,
    min_mbti_scs: float,
    max_mbti_rai_gap: float,
    min_open_scs: float,
    max_open_rai_gap: float,
    max_open_primary_delta_abs: float,
) -> dict[str, Any]:
    task_type = row.get("task_type", "")
    result = dict(row)

    if task_type == "mbti_mcq":
        osr = _to_float(row.get("osr_letter_match_rate"))
        scs = _to_float(row.get("scs_item_agreement_with_b_only"))
        rai = _to_float(row.get("rai_item_agreement_gap"))
        checks = {
            "osr_ok": osr >= min_mbti_osr_letter_match,
            "scs_ok": scs >= min_mbti_scs,
            "rai_ok": rai <= max_mbti_rai_gap,
        }
        result.update(
            {
                "classification_basis": "mbti",
                "osr_ok": checks["osr_ok"],
                "scs_ok": checks["scs_ok"],
                "rai_ok": checks["rai_ok"],
                "classification": "successful" if all(checks.values()) else "failed",
            }
        )
        return result

    primary_delta = abs(_to_float(row.get("primary_outcome_delta_vs_b_only")))
    scs = _to_float(row.get("scs_lexical_similarity_to_b_only"))
    rai = _to_float(row.get("rai_lexical_gap"))
    checks = {
        "primary_delta_ok": primary_delta <= max_open_primary_delta_abs,
        "scs_ok": scs >= min_open_scs,
        "rai_ok": rai <= max_open_rai_gap,
    }
    result.update(
        {
            "classification_basis": "open_or_constrained",
            "primary_delta_ok": checks["primary_delta_ok"],
            "scs_ok": checks["scs_ok"],
            "rai_ok": checks["rai_ok"],
            "classification": "successful" if all(checks.values()) else "failed",
        }
    )
    return result


def _summarize_overall(rows: list[dict[str, Any]], overall_rule: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        switch_condition = str(row.get("switch_condition", ""))
        grouped.setdefault(switch_condition, []).append(row)

    overall_rows: list[dict[str, Any]] = []
    for switch_condition, items in sorted(grouped.items()):
        failed_count = sum(1 for item in items if item.get("classification") == "failed")
        successful_count = sum(1 for item in items if item.get("classification") == "successful")
        total = len(items)
        if overall_rule == "all_failed":
            overall = "failed" if failed_count == total else "successful"
        elif overall_rule == "majority_failed":
            overall = "failed" if failed_count > successful_count else "successful"
        else:
            overall = "failed" if failed_count > 0 else "successful"

        overall_rows.append(
            {
                "switch_condition": switch_condition,
                "overall_rule": overall_rule,
                "failed_rows": failed_count,
                "successful_rows": successful_count,
                "total_rows": total,
                "overall_classification": overall,
            }
        )
    return overall_rows


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


if __name__ == "__main__":
    main()
