from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.analysis import rq2_analyze_strong_update as rq2
from scripts.analysis import rq2_build_full_report_tables as rq2_tables
from scripts.analysis import rq3_analyze_warmup_reinforcement as rq3
from scripts.analysis import rq3_build_full_report_tables as rq3_tables
from scripts.rq2_rq3_selected_60_plan import RQ2_BATCH2_PAIRS, RQ2_PAIRS, RQ3_BATCH2_PAIRS, RQ3_PAIRS
from src.analysis.run_selection import build_run_metadata
from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


TASK_TYPES = ["mbti_mcq", "machine_mindset", "ifeval"]
MODEL_NAME = "gemini-2.5-flash-lite"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build stable-control full-run RQ2/RQ3 reports from the latest completed runs.")
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--rq2-prefix", default="rq2_selected66_stable_control_full_run")
    parser.add_argument("--rq3-prefix", default="rq3_selected66_stable_control_full_run")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    run_metadata = build_run_metadata(raw_records)
    scored_run_ids = {str(record["run_id"]) for record in scored_records}
    success_keys = rq2._build_success_key_set(raw_records)
    mbti_records_by_run = rq2._records_by_run_id(scored_records, "mbti_mcq")

    rq2_pair_rows: list[dict[str, Any]] = []
    rq2_audit_rows: list[dict[str, Any]] = []
    for pair in RQ2_PAIRS + RQ2_BATCH2_PAIRS:
        persona_a = str(pair["A"])
        persona_b = str(pair["B"])
        selected_runs = rq2._select_runs(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            persona_a=persona_a,
            persona_b=persona_b,
            task_types=TASK_TYPES,
            model_name=MODEL_NAME,
            source_dataset=None,
        )
        if not selected_runs:
            continue
        stable_map, audit_rows = _build_rq2_stability_map(
            persona_a=persona_a,
            persona_b=persona_b,
            selected_runs=selected_runs,
            mbti_records_by_run=mbti_records_by_run,
        )
        rq2_audit_rows.extend(audit_rows)
        for task_type in TASK_TYPES:
            task_runs = selected_runs.get(task_type, {})
            if not task_runs:
                continue
            for row in rq2._build_comparison_rows(
                task_type=task_type,
                run_ids=task_runs,
                raw_records=raw_records,
                scored_records=scored_records,
                success_keys=success_keys,
                persona_a=persona_a,
                persona_b=persona_b,
            ):
                track = str(row.get("retain_mechanism", ""))
                if stable_map.get(track):
                    rq2_pair_rows.append(rq2_tables._normalize_row(row))

    rq3_pair_rows: list[dict[str, Any]] = []
    rq3_audit_rows: list[dict[str, Any]] = []
    for pair in RQ3_PAIRS + RQ3_BATCH2_PAIRS:
        persona_a = str(pair["A"])
        persona_b = str(pair["B"])
        selected_runs = rq3._select_runs(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            persona_a=persona_a,
            persona_b=persona_b,
            task_types=TASK_TYPES,
            model_name=MODEL_NAME,
            source_dataset=None,
        )
        if not selected_runs:
            continue
        stable_map, audit_rows = _build_rq3_stability_map(
            persona_a=persona_a,
            persona_b=persona_b,
            selected_runs=selected_runs,
            mbti_records_by_run=mbti_records_by_run,
        )
        rq3_audit_rows.extend(audit_rows)
        for task_type in TASK_TYPES:
            task_runs = selected_runs.get(task_type, {})
            if not task_runs:
                continue
            for row in rq3._build_comparison_rows(
                task_type=task_type,
                run_ids=task_runs,
                raw_records=raw_records,
                scored_records=scored_records,
                success_keys=success_keys,
                persona_a=persona_a,
                persona_b=persona_b,
            ):
                track = str(row.get("retain_mechanism", ""))
                if stable_map.get(track):
                    rq3_pair_rows.append(rq3_tables._normalize_row(row))

    rq2_overall = rq2_tables._aggregate_pair_table(rq2_pair_rows)
    rq3_overall = rq3_tables._aggregate_pair_table(rq3_pair_rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    _write_csv(args.output_dir / f"{args.rq2_prefix}_pair_update_table.csv", rq2_pair_rows)
    _write_csv(args.output_dir / f"{args.rq2_prefix}_overall_by_task_track.csv", rq2_overall)
    _write_csv(args.output_dir / f"{args.rq2_prefix}_stability_audit.csv", rq2_audit_rows)
    (args.output_dir / f"{args.rq2_prefix}_report.md").write_text(
        rq2_tables._render_report(rq2_pair_rows, rq2_overall),
        encoding="utf-8",
    )

    _write_csv(args.output_dir / f"{args.rq3_prefix}_pair_reinforcement_table.csv", rq3_pair_rows)
    _write_csv(args.output_dir / f"{args.rq3_prefix}_overall_by_task_track.csv", rq3_overall)
    _write_csv(args.output_dir / f"{args.rq3_prefix}_stability_audit.csv", rq3_audit_rows)
    (args.output_dir / f"{args.rq3_prefix}_report.md").write_text(
        rq3_tables._render_report(rq3_pair_rows, rq3_overall),
        encoding="utf-8",
    )

    print(f"wrote {args.rq2_prefix} rows={len(rq2_pair_rows)}")
    print(f"wrote {args.rq3_prefix} rows={len(rq3_pair_rows)}")


def _load_scored_records(scored_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(scored_dir.glob("*_scores.jsonl")):
        records.extend(read_jsonl(path))
    return records


def _final_type_for_run(run_id: str, mbti_records_by_run: dict[str, list[dict[str, Any]]]) -> str:
    aggregates = aggregate_profiles(mbti_records_by_run.get(run_id, []))
    if not aggregates:
        return ""
    return str(aggregates[0].get("final_type", ""))


def _build_rq2_stability_map(
    *,
    persona_a: str,
    persona_b: str,
    selected_runs: dict[str, dict[str, str]],
    mbti_records_by_run: dict[str, list[dict[str, Any]]],
) -> tuple[dict[str, bool], list[dict[str, Any]]]:
    mbti_runs = selected_runs.get("mbti_mcq", {})
    audit_rows: list[dict[str, Any]] = []
    stable_map: dict[str, bool] = {}
    for track in ["history", "summary"]:
        default_control_run = str(mbti_runs.get(f"{track}:default_control", ""))
        strong_control_run = str(mbti_runs.get(f"{track}:strong_control", ""))
        default_final = _final_type_for_run(default_control_run, mbti_records_by_run)
        strong_final = _final_type_for_run(strong_control_run, mbti_records_by_run)
        stable = default_final == persona_b and strong_final == persona_b
        stable_map[track] = stable
        audit_rows.append(
            {
                "rq": "RQ2",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "retain_mechanism": track,
                "default_control_run_id": default_control_run,
                "default_control_final_type": default_final,
                "strong_control_run_id": strong_control_run,
                "strong_control_final_type": strong_final,
                "target_persona_b": persona_b,
                "stable_control": stable,
            }
        )
    return stable_map, audit_rows


def _build_rq3_stability_map(
    *,
    persona_a: str,
    persona_b: str,
    selected_runs: dict[str, dict[str, str]],
    mbti_records_by_run: dict[str, list[dict[str, Any]]],
) -> tuple[dict[str, bool], list[dict[str, Any]]]:
    mbti_runs = selected_runs.get("mbti_mcq", {})
    audit_rows: list[dict[str, Any]] = []
    stable_map: dict[str, bool] = {}
    for track in ["history", "summary"]:
        simple_control_run = str(mbti_runs.get(f"{track}:simple_control", ""))
        reinforced_control_run = str(mbti_runs.get(f"{track}:control:3", ""))
        simple_final = _final_type_for_run(simple_control_run, mbti_records_by_run)
        reinforced_final = _final_type_for_run(reinforced_control_run, mbti_records_by_run)
        stable = simple_final == persona_b and reinforced_final == persona_b
        stable_map[track] = stable
        audit_rows.append(
            {
                "rq": "RQ3",
                "persona_a": persona_a,
                "persona_b": persona_b,
                "pair_id": f"{persona_a}_to_{persona_b}",
                "retain_mechanism": track,
                "simple_control_run_id": simple_control_run,
                "simple_control_final_type": simple_final,
                "reinforced_control_run_id": reinforced_control_run,
                "reinforced_control_final_type": reinforced_final,
                "target_persona_b": persona_b,
                "stable_control": stable,
            }
        )
    return stable_map, audit_rows


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
