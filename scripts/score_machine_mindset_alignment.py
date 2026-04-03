from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.scoring.machine_mindset_alignment import (
    DEFAULT_EMBEDDING_MODEL,
    active_persona_for_condition,
    build_reference_bank,
    load_eval_sample_map,
    score_dimension_response,
    score_self_awareness_response,
)
from src.utils.io import read_jsonl, write_jsonl


CONDITIONS = ["B_only", "A_history_to_B", "A_summary_to_B", "B_history_to_B", "B_summary_to_B"]
SUMMARY_CONDITIONS = ["A_history_to_B", "A_summary_to_B", "B_history_to_B", "B_summary_to_B"]
MATCHED_CONTROL = {
    "A_history_to_B": "B_history_to_B",
    "A_summary_to_B": "B_summary_to_B",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score Machine Mindset runs against the labeled MBTI reference bank."
    )
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument(
        "--eval-samples-file",
        type=Path,
        required=True,
        help="Prompt-aligned eval JSONL built from build_machine_mindset_eval_sets.py.",
    )
    parser.add_argument(
        "--labeled-dataset",
        type=Path,
        default=Path("data/processed/machine_mindset_labeled.parquet"),
    )
    parser.add_argument("--persona-a", required=True)
    parser.add_argument("--persona-b", required=True)
    parser.add_argument("--model-name", default=None)
    parser.add_argument(
        "--trial-id",
        default=None,
        help="Optional trial_id filter. Leave unset to score and summarize every trial present in the selected runs.",
    )
    parser.add_argument(
        "--similarity-backend",
        choices=["embedding", "tfidf"],
        default="embedding",
        help="Similarity backend used for reference-bank matching.",
    )
    parser.add_argument(
        "--embedding-model",
        default=DEFAULT_EMBEDDING_MODEL,
        help="Transformer model used when --similarity-backend=embedding.",
    )
    parser.add_argument(
        "--embedding-cache-dir",
        type=Path,
        default=Path("outputs/embedding_cache"),
        help="Cache directory for text embeddings.",
    )
    parser.add_argument(
        "--output-prefix",
        default=None,
        help="Prefix for scored/summary outputs. Defaults to machine_mindset_alignment_<eval_source>_<persona_a>_to_<persona_b>.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/tables"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    eval_samples = load_eval_sample_map(args.eval_samples_file)
    eval_source_dataset = _detect_source_dataset(eval_samples)
    reference_bank = build_reference_bank(args.labeled_dataset)

    selected_runs = _select_latest_runs(
        raw_records=raw_records,
        eval_sample_ids=set(eval_samples.keys()),
        eval_source_dataset=eval_source_dataset,
        persona_a=args.persona_a,
        persona_b=args.persona_b,
        model_name=args.model_name,
    )
    missing = [condition for condition in CONDITIONS if condition not in selected_runs]
    if missing:
        raise SystemExit(f"Missing runs for conditions: {', '.join(missing)}")

    per_record_rows: list[dict[str, Any]] = []
    run_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for condition, run_id in selected_runs.items():
        relevant_raw = [
            record for record in raw_records
            if record.get("run_id") == run_id and record.get("sample_id") in eval_samples
            and (args.trial_id is None or record.get("trial_id") == args.trial_id)
        ]
        for raw_record in relevant_raw:
            sample = eval_samples[raw_record["sample_id"]]
            prompt_key = str(sample.metadata.get("prompt_key", ""))
            source_group = str(sample.metadata.get("source_group", ""))
            active_persona = active_persona_for_condition(
                str(raw_record["condition"]),
                str(raw_record["persona_a"]),
                str(raw_record["persona_b"]),
            )
            if source_group == "self_awareness":
                score = score_self_awareness_response(
                    response_text=str(raw_record.get("response_text", "")),
                    prompt_key=prompt_key,
                    target_mbti_type=active_persona,
                    reference_bank=reference_bank,
                    persona_a=str(raw_record["persona_a"]),
                    similarity_backend=args.similarity_backend,
                    similarity_model_name=args.embedding_model,
                    embedding_cache_dir=args.embedding_cache_dir,
                )
            else:
                score = score_dimension_response(
                    response_text=str(raw_record.get("response_text", "")),
                    prompt_key=prompt_key,
                    dimension=str(sample.metadata["mbti_dimension"]),
                    target_mbti_type=active_persona,
                    reference_bank=reference_bank,
                    persona_a=str(raw_record["persona_a"]),
                    similarity_backend=args.similarity_backend,
                    similarity_model_name=args.embedding_model,
                    embedding_cache_dir=args.embedding_cache_dir,
                )
            row = {
                "run_id": run_id,
                "condition": condition,
                "persona_a": raw_record["persona_a"],
                "persona_b": raw_record["persona_b"],
                "model_name": raw_record["model_name"],
                "trial_id": raw_record.get("trial_id", ""),
                "sample_id": raw_record["sample_id"],
                "response_text": raw_record["response_text"],
                "eval_source_dataset": eval_source_dataset,
                "similarity_backend": args.similarity_backend,
                "embedding_model": args.embedding_model if args.similarity_backend == "embedding" else "",
                **score,
            }
            per_record_rows.append(row)
            run_records[condition].append(row)

    summary_rows = _build_summary_rows(run_records)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_prefix = args.output_prefix or (
        f"machine_mindset_alignment_{eval_source_dataset}_{args.persona_a}_to_{args.persona_b}"
    )
    scored_path = args.output_dir / f"{output_prefix}_scored.jsonl"
    summary_path = args.output_dir / f"{output_prefix}_summary.csv"
    write_jsonl(scored_path, per_record_rows)
    _write_csv(summary_path, summary_rows)

    print(f"selected runs -> {json.dumps(selected_runs, ensure_ascii=False)}")
    print(f"wrote per-record scores -> {scored_path}")
    print(f"wrote summary -> {summary_path}")


def _detect_source_dataset(eval_samples: dict[str, Any]) -> str:
    source_datasets = {sample.source_dataset for sample in eval_samples.values()}
    if len(source_datasets) != 1:
        raise ValueError(f"Expected one source_dataset in eval samples, got: {sorted(source_datasets)}")
    return next(iter(source_datasets))


def _select_latest_runs(
    *,
    raw_records: list[dict[str, Any]],
    eval_sample_ids: set[str],
    eval_source_dataset: str,
    persona_a: str,
    persona_b: str,
    model_name: str | None,
) -> dict[str, str]:
    candidates = [
        record
        for record in raw_records
        if str(record.get("meta_json", {}).get("source_dataset", "")) == eval_source_dataset
        and record.get("persona_a") == persona_a
        and record.get("persona_b") == persona_b
        and (model_name is None or record.get("model_name") == model_name)
    ]
    overlap_by_run: dict[str, int] = defaultdict(int)
    for record in candidates:
        run_id = str(record["run_id"])
        if str(record.get("sample_id", "")) in eval_sample_ids:
            overlap_by_run[run_id] += 1
    selected: dict[str, str] = {}
    for condition in CONDITIONS:
        condition_records = [record for record in candidates if record.get("condition") == condition]
        if not condition_records:
            continue
        run_ids = {str(record["run_id"]) for record in condition_records}
        best_run_id = max(
            run_ids,
            key=lambda run_id: (
                overlap_by_run.get(run_id, 0),
                max(str(record.get("timestamp", "")) for record in condition_records if str(record["run_id"]) == run_id),
            ),
        )
        selected[condition] = best_run_id
    return selected


def _build_summary_rows(run_records: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not run_records:
        return rows

    first_row = next(iter(next(iter(run_records.values()))))
    source_group = first_row["source_group"]
    if source_group == "self_awareness":
        rows.extend(_build_self_awareness_summary(run_records))
    else:
        rows.extend(_build_dimension_summary(run_records))
    return rows


def _build_self_awareness_summary(run_records: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for trial_id in _common_trial_ids(run_records):
        by_condition = {
            condition: {
                row["sample_id"]: row
                for row in rows
                if row.get("trial_id", "") == trial_id
            }
            for condition, rows in run_records.items()
        }
        common_ids = _common_sample_ids(by_condition)
        if not common_ids:
            continue

        for switch_condition in SUMMARY_CONDITIONS:
            switch_rows = [by_condition[switch_condition][sample_id] for sample_id in common_ids]
            b_rows = [by_condition["B_only"][sample_id] for sample_id in common_ids]
            matched_control = MATCHED_CONTROL.get(switch_condition, "")
            matched_rows = (
                [by_condition[matched_control][sample_id] for sample_id in common_ids]
                if matched_control
                else []
            )
            rows.append(
                {
                    "source_group": "self_awareness",
                    "trial_id": trial_id,
                    "switch_condition": switch_condition,
                    "matched_control_condition": matched_control,
                    "n_common_samples": len(common_ids),
                    "osr_type_match_rate": round(mean(float(row["target_type_match"]) for row in switch_rows), 4),
                    "mean_target_rank": round(mean(float(row["target_type_rank"] or 0) for row in switch_rows), 4),
                    "mean_target_similarity": round(mean(float(row["target_type_similarity"]) for row in switch_rows), 4),
                    "scs_predicted_type_agreement_with_b_only": round(
                        mean(1.0 if switch["predicted_type"] == b_only["predicted_type"] else 0.0 for switch, b_only in zip(switch_rows, b_rows)),
                        4,
                    ),
                    "agreement_with_matched_b_control": round(
                        mean(
                            1.0 if switch["predicted_type"] == control["predicted_type"] else 0.0
                            for switch, control in zip(switch_rows, matched_rows)
                        ),
                        4,
                    ) if matched_rows else "",
                    "mean_rai_margin_a_minus_target": round(mean(float(row["rai_margin_a_minus_target"]) for row in switch_rows), 4),
                }
            )
    return rows


def _build_dimension_summary(run_records: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for trial_id in _common_trial_ids(run_records):
        by_condition = {
            condition: {
                row["sample_id"]: row
                for row in rows
                if row.get("trial_id", "") == trial_id
            }
            for condition, rows in run_records.items()
        }
        common_ids = _common_sample_ids(by_condition)
        if not common_ids:
            continue

        for switch_condition in SUMMARY_CONDITIONS:
            switch_rows = [by_condition[switch_condition][sample_id] for sample_id in common_ids]
            b_rows = [by_condition["B_only"][sample_id] for sample_id in common_ids]
            matched_control = MATCHED_CONTROL.get(switch_condition, "")
            matched_rows = (
                [by_condition[matched_control][sample_id] for sample_id in common_ids]
                if matched_control
                else []
            )
            rows.append(
                {
                    "source_group": "dimension_pole",
                    "trial_id": trial_id,
                    "switch_condition": switch_condition,
                    "matched_control_condition": matched_control,
                    "n_common_samples": len(common_ids),
                    "osr_dimension_match_rate": round(mean(float(row["target_code_match"]) for row in switch_rows), 4),
                    "mean_target_similarity": round(mean(float(row["target_code_similarity"]) for row in switch_rows), 4),
                    "scs_predicted_code_agreement_with_b_only": round(
                        mean(1.0 if switch["predicted_code"] == b_only["predicted_code"] else 0.0 for switch, b_only in zip(switch_rows, b_rows)),
                        4,
                    ),
                    "agreement_with_matched_b_control": round(
                        mean(
                            1.0 if switch["predicted_code"] == control["predicted_code"] else 0.0
                            for switch, control in zip(switch_rows, matched_rows)
                        ),
                        4,
                    ) if matched_rows else "",
                    "mean_rai_margin_a_minus_target": round(mean(float(row["rai_margin_a_minus_target"]) for row in switch_rows), 4),
                }
            )
    return rows


def _common_trial_ids(run_records: dict[str, list[dict[str, Any]]]) -> list[str]:
    trial_sets = []
    for condition in CONDITIONS:
        rows = run_records.get(condition, [])
        trial_sets.append({str(row.get("trial_id", "")) for row in rows})
    if not trial_sets:
        return []
    return sorted(set.intersection(*trial_sets))


def _common_sample_ids(by_condition: dict[str, dict[str, dict[str, Any]]]) -> list[str]:
    sample_sets = [set(items.keys()) for items in by_condition.values()]
    if not sample_sets:
        return []
    return sorted(set.intersection(*sample_sets))


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
