from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.io import read_jsonl


CONDITIONS = ["B_only", "A_history_to_B", "A_summary_to_B", "B_history_to_B", "B_summary_to_B"]
SUMMARY_CONDITIONS = ["A_history_to_B", "A_summary_to_B", "B_history_to_B", "B_summary_to_B"]
MATCHED_CONTROL = {
    "A_history_to_B": "B_history_to_B",
    "A_summary_to_B": "B_summary_to_B",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize IFEval switch results with repeat-aware trial handling."
    )
    parser.add_argument("--persona-a", required=True)
    parser.add_argument("--persona-b", required=True)
    parser.add_argument("--model-name", default=None)
    parser.add_argument("--trial-id", default=None, help="Optional single trial_id to summarize.")
    parser.add_argument("--source-dataset", default="ifeval")
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument("--output-prefix", default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)

    run_metadata = _build_run_metadata(raw_records)
    selected_runs = _select_latest_runs(
        run_metadata=run_metadata,
        persona_a=args.persona_a,
        persona_b=args.persona_b,
        model_name=args.model_name,
        source_dataset=args.source_dataset,
    )
    missing = [condition for condition in CONDITIONS if condition not in selected_runs]
    if missing:
        raise SystemExit(f"Missing IFEval runs for conditions: {', '.join(missing)}")

    rows = _build_summary_rows(scored_records, selected_runs, args.trial_id)
    if not rows:
        raise SystemExit("No common scored IFEval samples found for the requested filters.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or f"ifeval_switch_{args.persona_a}_to_{args.persona_b}"
    summary_path = args.output_dir / f"{prefix}_summary.csv"
    runs_path = args.output_dir / f"{prefix}_selected_runs.csv"
    _write_csv(summary_path, rows)
    _write_csv(
        runs_path,
        [
            {
                "condition": condition,
                "run_id": run_id,
                "model_name": run_metadata[run_id]["model_name"],
                "source_dataset": run_metadata[run_id]["source_dataset"],
                "timestamp": run_metadata[run_id]["timestamp"],
            }
            for condition, run_id in selected_runs.items()
        ],
    )
    print(f"wrote summary -> {summary_path}")
    print(f"wrote selected runs -> {runs_path}")


def _load_scored_records(scored_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(scored_dir.glob("*_scores.jsonl")):
        records.extend(read_jsonl(path))
    return records


def _build_run_metadata(raw_records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in raw_records:
        by_run[str(record["run_id"])].append(record)

    metadata: dict[str, dict[str, Any]] = {}
    for run_id, items in by_run.items():
        first = items[0]
        timestamps = [str(item.get("timestamp", "")) for item in items if item.get("timestamp")]
        metadata[run_id] = {
            "run_id": run_id,
            "task_type": first.get("task_type", ""),
            "condition": first.get("condition", ""),
            "persona_a": first.get("persona_a", ""),
            "persona_b": first.get("persona_b", ""),
            "model_name": first.get("model_name", ""),
            "source_dataset": str(first.get("meta_json", {}).get("source_dataset", "")),
            "timestamp": max(timestamps) if timestamps else "",
        }
    return metadata


def _select_latest_runs(
    *,
    run_metadata: dict[str, dict[str, Any]],
    persona_a: str,
    persona_b: str,
    model_name: str | None,
    source_dataset: str,
) -> dict[str, str]:
    candidates = [
        meta
        for meta in run_metadata.values()
        if meta["task_type"] == "ifeval"
        and meta["persona_a"] == persona_a
        and meta["persona_b"] == persona_b
        and meta["source_dataset"] == source_dataset
        and (model_name is None or meta["model_name"] == model_name)
    ]
    selected: dict[str, str] = {}
    for condition in CONDITIONS:
        condition_candidates = [meta for meta in candidates if meta["condition"] == condition]
        if not condition_candidates:
            continue
        latest = max(condition_candidates, key=lambda item: item["timestamp"])
        selected[condition] = str(latest["run_id"])
    return selected


def _build_summary_rows(
    scored_records: list[dict[str, Any]],
    selected_runs: dict[str, str],
    trial_filter: str | None,
) -> list[dict[str, Any]]:
    by_condition_and_trial: dict[str, dict[str, dict[str, dict[str, Any]]]] = {}
    for condition, run_id in selected_runs.items():
        condition_records = [
            record
            for record in scored_records
            if record.get("run_id") == run_id and record.get("task_type") == "ifeval"
        ]
        trial_map: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
        for record in condition_records:
            trial_id = str(record.get("trial_id", ""))
            if trial_filter is not None and trial_id != trial_filter:
                continue
            trial_map[trial_id][str(record["sample_id"])] = record
        by_condition_and_trial[condition] = dict(trial_map)

    common_trial_ids = sorted(
        set.intersection(*(set(trial_map.keys()) for trial_map in by_condition_and_trial.values()))
    )
    rows: list[dict[str, Any]] = []
    for trial_id in common_trial_ids:
        per_condition = {
            condition: by_condition_and_trial[condition][trial_id]
            for condition in CONDITIONS
        }
        common_sample_ids = sorted(set.intersection(*(set(items.keys()) for items in per_condition.values())))
        if not common_sample_ids:
            continue

        metrics = {
            condition: _summarize_ifeval_condition(
                [per_condition[condition][sample_id] for sample_id in common_sample_ids]
            )
            for condition in CONDITIONS
        }
        for switch_condition in SUMMARY_CONDITIONS:
            switch_metrics = metrics[switch_condition]
            b_metrics = metrics["B_only"]
            matched_control = MATCHED_CONTROL.get(switch_condition, "")
            matched_metrics = metrics.get(matched_control, {})
            rows.append(
                {
                    "trial_id": trial_id,
                    "switch_condition": switch_condition,
                    "matched_control_condition": matched_control,
                    "n_common_samples": len(common_sample_ids),
                    "strict_follow_all_rate_B_only": b_metrics["strict_follow_all_rate"],
                    "strict_follow_all_rate_switch": switch_metrics["strict_follow_all_rate"],
                    "strict_follow_all_delta_vs_b_only": round(
                        switch_metrics["strict_follow_all_rate"] - b_metrics["strict_follow_all_rate"], 4
                    ),
                    "strict_follow_all_delta_vs_matched_b_control": round(
                        switch_metrics["strict_follow_all_rate"] - float(matched_metrics.get("strict_follow_all_rate", 0.0)),
                        4,
                    ) if matched_control else "",
                    "mean_strict_instruction_fraction_B_only": b_metrics["mean_strict_instruction_fraction"],
                    "mean_strict_instruction_fraction_switch": switch_metrics["mean_strict_instruction_fraction"],
                    "mean_strict_instruction_fraction_delta_vs_b_only": round(
                        switch_metrics["mean_strict_instruction_fraction"] - b_metrics["mean_strict_instruction_fraction"], 4
                    ),
                    "mean_strict_instruction_fraction_delta_vs_matched_b_control": round(
                        switch_metrics["mean_strict_instruction_fraction"] - float(matched_metrics.get("mean_strict_instruction_fraction", 0.0)),
                        4,
                    ) if matched_control else "",
                    "loose_follow_all_rate_B_only": b_metrics["loose_follow_all_rate"],
                    "loose_follow_all_rate_switch": switch_metrics["loose_follow_all_rate"],
                    "loose_follow_all_delta_vs_b_only": round(
                        switch_metrics["loose_follow_all_rate"] - b_metrics["loose_follow_all_rate"], 4
                    ),
                    "loose_follow_all_delta_vs_matched_b_control": round(
                        switch_metrics["loose_follow_all_rate"] - float(matched_metrics.get("loose_follow_all_rate", 0.0)),
                        4,
                    ) if matched_control else "",
                    "mean_loose_instruction_fraction_B_only": b_metrics["mean_loose_instruction_fraction"],
                    "mean_loose_instruction_fraction_switch": switch_metrics["mean_loose_instruction_fraction"],
                    "mean_loose_instruction_fraction_delta_vs_b_only": round(
                        switch_metrics["mean_loose_instruction_fraction"] - b_metrics["mean_loose_instruction_fraction"], 4
                    ),
                    "mean_loose_instruction_fraction_delta_vs_matched_b_control": round(
                        switch_metrics["mean_loose_instruction_fraction"] - float(matched_metrics.get("mean_loose_instruction_fraction", 0.0)),
                        4,
                    ) if matched_control else "",
                }
            )
    return rows


def _summarize_ifeval_condition(records: list[dict[str, Any]]) -> dict[str, float]:
    if not records:
        return {
            "strict_follow_all_rate": 0.0,
            "mean_strict_instruction_fraction": 0.0,
            "loose_follow_all_rate": 0.0,
            "mean_loose_instruction_fraction": 0.0,
        }
    strict_all = [1.0 if bool(record.get("strict_follow_all")) else 0.0 for record in records]
    loose_all = [1.0 if bool(record.get("loose_follow_all")) else 0.0 for record in records]
    strict_fraction = []
    loose_fraction = []
    for record in records:
        instruction_count = int(record.get("instruction_count", 0) or 0)
        strict_passed = int(record.get("strict_checks_passed", 0) or 0)
        loose_passed = int(record.get("loose_checks_passed", 0) or 0)
        strict_fraction.append((strict_passed / instruction_count) if instruction_count else 0.0)
        loose_fraction.append((loose_passed / instruction_count) if instruction_count else 0.0)
    return {
        "strict_follow_all_rate": round(mean(strict_all), 4),
        "mean_strict_instruction_fraction": round(mean(strict_fraction), 4),
        "loose_follow_all_rate": round(mean(loose_all), 4),
        "mean_loose_instruction_fraction": round(mean(loose_fraction), 4),
    }


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
