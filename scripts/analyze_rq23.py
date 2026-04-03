from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


CONDITIONS = ["A_only", "B_only", "A_history_to_B", "A_summary_to_B"]
SWITCH_CONDITIONS = ["A_history_to_B", "A_summary_to_B"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate persona-switch outputs for proposal RQ2/RQ3.")
    parser.add_argument("--persona-a", required=True, help="Warm-up persona A to analyze.")
    parser.add_argument("--persona-b", required=True, help="Evaluation persona B to analyze.")
    parser.add_argument(
        "--task-types",
        nargs="+",
        default=["mbti_mcq", "machine_mindset", "ifeval"],
        help="Task types to include.",
    )
    parser.add_argument("--model-name", default=None, help="Optional model name filter.")
    parser.add_argument(
        "--source-dataset",
        default=None,
        help="Optional source dataset filter. Leave unset to use the latest matching run per task/condition.",
    )
    parser.add_argument("--raw-file", type=Path, default=Path("outputs/raw_generations/generations.jsonl"))
    parser.add_argument("--scored-dir", type=Path, default=Path("outputs/scored"))
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/tables"))
    parser.add_argument(
        "--output-prefix",
        default=None,
        help="Optional output file prefix. Defaults to rq23_<persona_a>_to_<persona_b>_<timestamp>.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_records = read_jsonl(args.raw_file)
    scored_records = _load_scored_records(args.scored_dir)
    run_metadata = _build_run_metadata(raw_records)
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

    rows: list[dict[str, Any]] = []
    selection_rows: list[dict[str, Any]] = []
    for task_type in args.task_types:
        condition_runs = selected_runs.get(task_type, {})
        if not condition_runs:
            continue

        for condition, run_id in condition_runs.items():
            meta = run_metadata[run_id]
            selection_rows.append(
                {
                    "task_type": task_type,
                    "condition": condition,
                    "run_id": run_id,
                    "source_dataset": meta["source_dataset"],
                    "model_name": meta["model_name"],
                    "sample_count": meta["sample_count"],
                    "timestamp": meta["timestamp"],
                }
            )

        if task_type == "mbti_mcq":
            rows.extend(_analyze_mbti(task_type, condition_runs, scored_records, args.persona_b, run_metadata))
        else:
            rows.extend(_analyze_open_task(task_type, condition_runs, raw_records, scored_records, run_metadata))

    if not rows:
        raise SystemExit("No complete task groups found for the requested filters.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or _default_prefix(args.persona_a, args.persona_b)
    csv_path = args.output_dir / f"{prefix}_summary.csv"
    md_path = args.output_dir / f"{prefix}_report.md"
    runs_path = args.output_dir / f"{prefix}_selected_runs.csv"

    _write_csv(csv_path, rows)
    _write_csv(runs_path, selection_rows)
    md_path.write_text(_render_report(args.persona_a, args.persona_b, rows, selection_rows), encoding="utf-8")

    print(f"wrote summary -> {csv_path}")
    print(f"wrote selected runs -> {runs_path}")
    print(f"wrote report -> {md_path}")


def _load_scored_records(scored_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(scored_dir.glob("*_scores.jsonl")):
        records.extend(read_jsonl(path))
    return records


def _build_run_metadata(raw_records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in raw_records:
        by_run[record["run_id"]].append(record)

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
            "sample_count": len(items),
            "timestamp": max(timestamps) if timestamps else "",
        }
    return metadata


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
        candidates = [
            meta
            for meta in run_metadata.values()
            if meta["run_id"] in scored_run_ids
            and meta["task_type"] == task_type
            and meta["persona_a"] == persona_a
            and meta["persona_b"] == persona_b
            and (model_name is None or meta["model_name"] == model_name)
            and (source_dataset is None or meta["source_dataset"] == source_dataset)
        ]
        by_condition: dict[str, str] = {}
        for condition in CONDITIONS:
            condition_candidates = [meta for meta in candidates if meta["condition"] == condition]
            if not condition_candidates:
                continue
            latest = max(condition_candidates, key=lambda item: item["timestamp"])
            by_condition[condition] = latest["run_id"]
        if set(CONDITIONS).issubset(by_condition):
            selected[task_type] = by_condition
    return selected


def _analyze_mbti(
    task_type: str,
    condition_runs: dict[str, str],
    scored_records: list[dict[str, Any]],
    persona_b: str,
    run_metadata: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    records_by_run = _records_by_run_id(scored_records, task_type)
    profiles: dict[str, dict[str, Any]] = {}
    labels_by_condition: dict[str, dict[str, str | None]] = {}
    for condition, run_id in condition_runs.items():
        run_records = records_by_run.get(run_id, [])
        aggregates = aggregate_profiles(run_records)
        if not aggregates:
            raise ValueError(f"No MBTI profile records found for {condition} / {run_id}")
        profiles[condition] = aggregates[0]
        labels_by_condition[condition] = {
            item["sample_id"]: item.get("predicted_label")
            for item in run_records
        }

    rows: list[dict[str, Any]] = []
    for switch_condition in SWITCH_CONDITIONS:
        common_ids = sorted(
            set(labels_by_condition["A_only"])
            & set(labels_by_condition["B_only"])
            & set(labels_by_condition[switch_condition])
        )
        if not common_ids:
            continue

        agreement_with_b = mean(
            1.0
            if labels_by_condition[switch_condition][sample_id] == labels_by_condition["B_only"][sample_id]
            else 0.0
            for sample_id in common_ids
        )
        agreement_with_a = mean(
            1.0
            if labels_by_condition[switch_condition][sample_id] == labels_by_condition["A_only"][sample_id]
            else 0.0
            for sample_id in common_ids
        )
        final_type = str(profiles[switch_condition]["final_type"])
        rows.append(
            {
                "task_type": task_type,
                "source_dataset": run_metadata[condition_runs[switch_condition]]["source_dataset"],
                "switch_condition": switch_condition,
                "n_common_samples": len(common_ids),
                "final_type_A_only": profiles["A_only"]["final_type"],
                "final_type_B_only": profiles["B_only"]["final_type"],
                "final_type_switch": final_type,
                "target_persona_b": persona_b,
                "osr_final_type_match_target_b": int(final_type == persona_b),
                "osr_letter_match_rate": round(_letter_match_rate(final_type, persona_b), 4),
                "scs_item_agreement_with_b_only": round(agreement_with_b, 4),
                "agreement_with_a_only": round(agreement_with_a, 4),
                "rai_item_agreement_gap": round(agreement_with_a - agreement_with_b, 4),
                "notes": "Positive RAI means the switched run stayed closer to A_only than to B_only.",
            }
        )
    return rows


def _analyze_open_task(
    task_type: str,
    condition_runs: dict[str, str],
    raw_records: list[dict[str, Any]],
    scored_records: list[dict[str, Any]],
    run_metadata: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    raw_by_run = _records_by_run_id(raw_records, task_type)
    scored_by_run = _records_by_run_id(scored_records, task_type)
    outcome_summaries = {
        condition: _summarize_task_outcome(task_type, scored_by_run.get(run_id, []))
        for condition, run_id in condition_runs.items()
    }

    rows: list[dict[str, Any]] = []
    for switch_condition in SWITCH_CONDITIONS:
        switch_texts = _sample_to_text(raw_by_run.get(condition_runs[switch_condition], []))
        a_texts = _sample_to_text(raw_by_run.get(condition_runs["A_only"], []))
        b_texts = _sample_to_text(raw_by_run.get(condition_runs["B_only"], []))
        common_ids = sorted(set(switch_texts) & set(a_texts) & set(b_texts))
        if not common_ids:
            continue

        lexical_to_b = []
        lexical_to_a = []
        style_to_b = []
        style_to_a = []
        for sample_id in common_ids:
            switch_text = switch_texts[sample_id]
            a_text = a_texts[sample_id]
            b_text = b_texts[sample_id]
            lexical_to_b.append(_lexical_f1(switch_text, b_text))
            lexical_to_a.append(_lexical_f1(switch_text, a_text))
            style_to_b.append(_style_similarity(switch_text, b_text))
            style_to_a.append(_style_similarity(switch_text, a_text))

        switch_outcome = outcome_summaries[switch_condition]
        b_outcome = outcome_summaries["B_only"]
        a_outcome = outcome_summaries["A_only"]
        rows.append(
            {
                "task_type": task_type,
                "source_dataset": run_metadata[condition_runs[switch_condition]]["source_dataset"],
                "switch_condition": switch_condition,
                "n_common_samples": len(common_ids),
                "primary_outcome_name": switch_outcome["primary_name"],
                "primary_outcome_A_only": a_outcome["primary_value"],
                "primary_outcome_B_only": b_outcome["primary_value"],
                "primary_outcome_switch": switch_outcome["primary_value"],
                "primary_outcome_delta_vs_b_only": round(switch_outcome["primary_value"] - b_outcome["primary_value"], 4),
                "secondary_outcome_name": switch_outcome["secondary_name"],
                "secondary_outcome_A_only": a_outcome["secondary_value"],
                "secondary_outcome_B_only": b_outcome["secondary_value"],
                "secondary_outcome_switch": switch_outcome["secondary_value"],
                "secondary_outcome_delta_vs_b_only": round(switch_outcome["secondary_value"] - b_outcome["secondary_value"], 4),
                "scs_lexical_similarity_to_b_only": round(mean(lexical_to_b), 4),
                "lexical_similarity_to_a_only": round(mean(lexical_to_a), 4),
                "rai_lexical_gap": round(mean(lexical_to_a) - mean(lexical_to_b), 4),
                "style_similarity_to_b_only": round(mean(style_to_b), 4),
                "style_similarity_to_a_only": round(mean(style_to_a), 4),
                "rai_style_gap": round(mean(style_to_a) - mean(style_to_b), 4),
                "notes": "Positive RAI means the switched run stayed closer to A_only than to B_only.",
            }
        )
    return rows


def _records_by_run_id(records: list[dict[str, Any]], task_type: str) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        if record.get("task_type") != task_type:
            continue
        grouped[str(record["run_id"])].append(record)
    return grouped


def _sample_to_text(records: list[dict[str, Any]]) -> dict[str, str]:
    return {
        str(record["sample_id"]): str(record.get("response_text", ""))
        for record in records
    }


def _summarize_task_outcome(task_type: str, scored_records: list[dict[str, Any]]) -> dict[str, Any]:
    if not scored_records:
        return {
            "primary_name": "missing",
            "primary_value": 0.0,
            "secondary_name": "missing",
            "secondary_value": 0.0,
        }

    if task_type == "machine_mindset":
        scores = [float(record.get("score", 0.0) or 0.0) for record in scored_records]
        keyword_recalls = [float(record.get("keyword_recall", 0.0) or 0.0) for record in scored_records]
        return {
            "primary_name": "mean_task_score",
            "primary_value": round(mean(scores), 4),
            "secondary_name": "mean_keyword_recall",
            "secondary_value": round(mean(keyword_recalls), 4),
        }

    official = any(record.get("checker_source") == "official_google_ifeval" for record in scored_records)
    if official:
        strict_all = [
            1.0 if bool(record.get("strict_follow_all")) else 0.0
            for record in scored_records
        ]
        strict_fraction = []
        for record in scored_records:
            total = int(record.get("instruction_count", 0) or 0)
            passed = int(record.get("strict_checks_passed", 0) or 0)
            strict_fraction.append((passed / total) if total else 0.0)
        return {
            "primary_name": "strict_follow_all_rate",
            "primary_value": round(mean(strict_all), 4),
            "secondary_name": "mean_strict_instruction_fraction",
            "secondary_value": round(mean(strict_fraction), 4),
        }

    meets_constraint = [
        1.0 if bool(record.get("meets_constraint")) else 0.0
        for record in scored_records
    ]
    check_fraction = []
    for record in scored_records:
        total = int(record.get("checks_total", 0) or 0)
        passed = int(record.get("checks_passed", 0) or 0)
        check_fraction.append((passed / total) if total else 1.0)
    return {
        "primary_name": "meets_constraint_rate",
        "primary_value": round(mean(meets_constraint), 4),
        "secondary_name": "mean_checks_pass_fraction",
        "secondary_value": round(mean(check_fraction), 4),
    }


def _letter_match_rate(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    pairs = zip(left, right)
    return sum(1 for ltr_left, ltr_right in pairs if ltr_left == ltr_right) / min(len(left), len(right))


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


def _style_similarity(left: str, right: str) -> float:
    left_features = _style_features(left)
    right_features = _style_features(right)
    distances = []
    for key in left_features:
        left_value = left_features[key]
        right_value = right_features[key]
        scale = max(1.0, abs(left_value), abs(right_value))
        distances.append(abs(left_value - right_value) / scale)
    return max(0.0, 1.0 - mean(distances))


def _style_features(text: str) -> dict[str, float]:
    words = re.findall(r"[A-Za-z0-9']+", text)
    sentences = [item for item in re.split(r"(?<=[.!?])\s+|\n+", text.strip()) if item.strip()]
    bullet_count = len([line for line in text.splitlines() if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line)])
    exclamations = text.count("!")
    questions = text.count("?")
    first_person = len(re.findall(r"\b(i|me|my|mine|myself)\b", text, flags=re.IGNORECASE))
    word_count = len(words)
    sentence_count = len(sentences)
    return {
        "word_count": float(word_count),
        "sentence_count": float(sentence_count),
        "avg_sentence_length": float(word_count / sentence_count) if sentence_count else 0.0,
        "bullet_count": float(bullet_count),
        "exclamations_per_100_words": float(exclamations * 100 / word_count) if word_count else 0.0,
        "questions_per_100_words": float(questions * 100 / word_count) if word_count else 0.0,
        "first_person_per_100_words": float(first_person * 100 / word_count) if word_count else 0.0,
    }


def _default_prefix(persona_a: str, persona_b: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"rq23_{persona_a}_to_{persona_b}_{now}"


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


def _render_report(
    persona_a: str,
    persona_b: str,
    summary_rows: list[dict[str, Any]],
    selection_rows: list[dict[str, Any]],
) -> str:
    lines = [
        f"# RQ2/RQ3 Summary: {persona_a} -> {persona_b}",
        "",
        "## Selected Runs",
        "",
    ]
    for row in sorted(selection_rows, key=lambda item: (item["task_type"], item["condition"])):
        lines.append(
            f"- {row['task_type']} | {row['condition']} | {row['run_id']} | "
            f"{row['source_dataset']} | {row['model_name']} | n={row['sample_count']}"
        )

    lines.extend(["", "## RQ2", ""])
    for row in summary_rows:
        task_type = row["task_type"]
        switch_condition = row["switch_condition"]
        if task_type == "mbti_mcq":
            lines.append(
                f"- {task_type} / {switch_condition}: final_type={row['final_type_switch']} "
                f"vs B_only={row['final_type_B_only']}, OSR={row['osr_final_type_match_target_b']}, "
                f"SCS={row['scs_item_agreement_with_b_only']}, RAI={row['rai_item_agreement_gap']}."
            )
            continue
        lines.append(
            f"- {task_type} / {switch_condition}: {row['primary_outcome_name']}={row['primary_outcome_switch']} "
            f"(delta vs B_only={row['primary_outcome_delta_vs_b_only']}), "
            f"lexical SCS={row['scs_lexical_similarity_to_b_only']}, lexical RAI={row['rai_lexical_gap']}, "
            f"style RAI={row['rai_style_gap']}."
        )

    open_rows = [row for row in summary_rows if row["task_type"] == "machine_mindset"]
    ifeval_rows = [row for row in summary_rows if row["task_type"] == "ifeval"]
    lines.extend(["", "## RQ3", ""])
    if open_rows and ifeval_rows:
        for switch_condition in SWITCH_CONDITIONS:
            open_row = next((row for row in open_rows if row["switch_condition"] == switch_condition), None)
            ifeval_row = next((row for row in ifeval_rows if row["switch_condition"] == switch_condition), None)
            if not open_row or not ifeval_row:
                continue
            lines.append(
                f"- {switch_condition}: Machine Mindset lexical RAI={open_row['rai_lexical_gap']} "
                f"vs IFEval lexical RAI={ifeval_row['rai_lexical_gap']}; "
                f"Machine Mindset style RAI={open_row['rai_style_gap']} "
                f"vs IFEval style RAI={ifeval_row['rai_style_gap']}."
            )
            lines.append(
                f"- {switch_condition}: Machine Mindset outcome delta={open_row['primary_outcome_delta_vs_b_only']} "
                f"vs IFEval outcome delta={ifeval_row['primary_outcome_delta_vs_b_only']}."
            )
    else:
        lines.append("- Machine Mindset and IFEval runs were not both available, so the task-level comparison is incomplete.")

    lines.append("")
    lines.append("Positive RAI means the switched run remained closer to A_only than to B_only.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
