from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Route pairs after RQ1 using MBTI final-type switching only: A->B is successful iff the final MBTI type equals B."
    )
    parser.add_argument("--summary-file", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = _read_csv(args.summary_file)
    rows = [
        row
        for row in rows
        if row.get("row_type") == "switch_comparison" and row.get("task_type") == "mbti_mcq"
    ]
    if not rows:
        raise SystemExit(f"No mbti_mcq switch_comparison rows found in {args.summary_file}")
    classified_rows = [_classify_row(row) for row in rows]
    overall_rows = _summarize_overall(classified_rows)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or args.summary_file.stem.replace("_summary", "_classification")
    row_path = args.output_dir / f"{prefix}_rows.csv"
    overall_path = args.output_dir / f"{prefix}_overall.csv"
    _write_csv(row_path, classified_rows)
    _write_csv(overall_path, overall_rows)
    print(f"wrote row classifications -> {row_path}")
    print(f"wrote overall classifications -> {overall_path}")


def _classify_row(row: dict[str, str]) -> dict[str, Any]:
    result = dict(row)
    final_type_switch = str(row.get("final_type_switch", ""))
    target_persona_b = str(row.get("target_persona_b", ""))
    is_successful = final_type_switch == target_persona_b and bool(target_persona_b)
    result.update(
        {
            "classification_basis": "mbti_final_type_equals_target_b",
            "final_type_switch_equals_b": is_successful,
            "classification": "successful" if is_successful else "failed",
        }
    )
    return result


def _summarize_overall(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for row in rows:
        persona_a = str(row.get("persona_a", ""))
        persona_b = str(row.get("persona_b", ""))
        pair_id = str(row.get("pair_id", ""))
        switch_condition = str(row.get("switch_condition", ""))
        grouped.setdefault((persona_a, persona_b, pair_id, switch_condition), []).append(row)
    overall_rows: list[dict[str, Any]] = []
    for (persona_a, persona_b, pair_id, switch_condition), items in sorted(grouped.items()):
        failed_count = sum(1 for item in items if item.get("classification") == "failed")
        successful_count = sum(1 for item in items if item.get("classification") == "successful")
        total = len(items)
        overall = "successful" if successful_count == total else "failed"
        overall_rows.append(
            {
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": pair_id,
                "switch_condition": switch_condition,
                "overall_rule": "all_mbti_rows_final_type_equals_b",
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


if __name__ == "__main__":
    main()
