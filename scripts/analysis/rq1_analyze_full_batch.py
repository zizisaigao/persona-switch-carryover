from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from rq1_analyze_matched_switch import (  # type: ignore
    _build_premise_rows,
    _build_switch_rows,
    _load_scored_records,
    _render_report as _render_pair_report,
    _select_runs,
)
from rq1_build_full_report_tables import (  # type: ignore
    _aggregate_pair_table,
    _normalize_route_rows,
    _normalize_switch_row,
    _render_report,
    _write_csv,
)
from src.analysis.run_selection import build_run_metadata, build_selection_row
from src.utils.io import read_jsonl

MBTI_ORDER = [
    "INTJ", "ESFP", "INFJ", "ENFJ",
    "ISFJ", "ENTJ", "ENTP", "ESTP",
    "ISTP", "ISFP", "ENFP", "ISTJ",
    "INTP", "INFP", "ESFJ", "ESTJ",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full-batch RQ1 tables for all ordered MBTI pairs from raw/scored outputs in one pass.")
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--task-types", nargs="+", default=["mbti_mcq", "machine_mindset", "ifeval"])
    parser.add_argument("--output-prefix", default="rq1_twoway240_full_run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    run_metadata = build_run_metadata(raw_records)
    scored_run_ids = {str(record["run_id"]) for record in scored_records}

    pair_switch_rows: list[dict[str, Any]] = []
    pair_route_rows: list[dict[str, Any]] = []
    pair_selection_rows: list[dict[str, Any]] = []

    for persona_a in MBTI_ORDER:
        for persona_b in MBTI_ORDER:
            if persona_a == persona_b:
                continue
            selected_runs = _select_runs(
                run_metadata=run_metadata,
                scored_run_ids=scored_run_ids,
                persona_a=persona_a,
                persona_b=persona_b,
                task_types=args.task_types,
                model_name=args.model_name,
                source_dataset=None,
            )
            if not selected_runs:
                continue

            summary_rows: list[dict[str, Any]] = []
            for task_type in args.task_types:
                task_runs = selected_runs.get(task_type, {})
                if not task_runs:
                    continue
                for selection_role, run_id in sorted(task_runs.items()):
                    pair_selection_rows.append(
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
                        persona_a=persona_a,
                        persona_b=persona_b,
                    )
                )
                summary_rows.extend(
                    _build_switch_rows(
                        task_type=task_type,
                        run_ids=task_runs,
                        raw_records=raw_records,
                        scored_records=scored_records,
                        persona_a=persona_a,
                        persona_b=persona_b,
                    )
                )

            switch_rows = [row for row in summary_rows if row.get("row_type") == "switch_comparison"]
            pair_switch_rows.extend(_normalize_switch_rows(switch_rows))
            pair_route_rows.extend(_build_route_rows(switch_rows))

    if not pair_switch_rows:
        raise SystemExit("No RQ1 switch rows could be built from the available raw/scored outputs.")

    overall_table = _aggregate_pair_table(pair_switch_rows)
    route_table = _normalize_route_rows(pair_route_rows)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / f"{args.output_prefix}_pair_switch_table.csv"
    overall_path = args.output_dir / f"{args.output_prefix}_overall_by_task_track.csv"
    route_path = args.output_dir / f"{args.output_prefix}_pair_routing.csv"
    report_path = args.output_dir / f"{args.output_prefix}_report.md"
    selection_path = args.output_dir / f"{args.output_prefix}_selected_runs.csv"

    _write_csv(pair_path, pair_switch_rows)
    _write_csv(overall_path, overall_table)
    _write_csv(route_path, route_table)
    _write_csv(selection_path, pair_selection_rows)
    report_path.write_text(_render_report(pair_switch_rows, overall_table, route_table), encoding="utf-8")

    print(f"wrote pair switch table -> {pair_path}")
    print(f"wrote overall table -> {overall_path}")
    print(f"wrote routing table -> {route_path}")
    print(f"wrote selected runs -> {selection_path}")
    print(f"wrote report -> {report_path}")


def _normalize_switch_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [_normalize_switch_row(row) for row in rows]


def _build_route_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    mbti_rows = [
        row for row in rows
        if row.get("task_type") == "mbti_mcq" and row.get("row_type") == "switch_comparison"
    ]
    route_rows: list[dict[str, Any]] = []
    for row in mbti_rows:
        final_type_switch = str(row.get("final_type_switch", ""))
        target_persona_b = str(row.get("target_persona_b", ""))
        is_successful = final_type_switch == target_persona_b and bool(target_persona_b)
        route_rows.append(
            {
                "persona_a": str(row.get("persona_a", "")),
                "persona_b": str(row.get("persona_b", "")),
                "pair_id": str(row.get("pair_id", "")),
                "switch_condition": str(row.get("switch_condition", "")),
                "failed_rows": 0 if is_successful else 1,
                "successful_rows": 1 if is_successful else 0,
                "total_rows": 1,
                "overall_classification": "successful" if is_successful else "failed",
            }
        )
    return route_rows


if __name__ == "__main__":
    main()
