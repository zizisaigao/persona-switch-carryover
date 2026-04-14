from __future__ import annotations

from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[2]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from src.analysis.run_selection import build_run_metadata, select_latest_pair_run, select_latest_premise_mbti_only_run
from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


MBTI = [
    "INTJ", "ESFP", "INFJ", "ENFJ",
    "ISFJ", "ENTJ", "ENTP", "ESTP",
    "ISTP", "ISFP", "ENFP", "ISTJ",
    "INTP", "INFP", "ESFJ", "ESTJ",
]


def final_type_for(run_id: str, scored_by_run: dict[str, list[dict]]) -> str:
    aggs = aggregate_profiles(scored_by_run.get(run_id, []))
    return str(aggs[0].get("final_type", "")) if aggs else ""


def main() -> None:
    raw_records = read_jsonl(REPO / "outputs" / "raw_generations" / "generations.jsonl")
    scored_records: list[dict] = []
    for path in sorted((REPO / "outputs" / "scored").glob("*_scores.jsonl")):
        scored_records.extend(read_jsonl(path))

    run_metadata = build_run_metadata(raw_records)
    scored_run_ids = {str(r["run_id"]) for r in scored_records}
    mbti_by_run: dict[str, list[dict]] = {}
    for rec in scored_records:
        if rec.get("task_type") != "mbti_mcq":
            continue
        mbti_by_run.setdefault(str(rec["run_id"]), []).append(rec)

    both_failed: list[tuple[str, str]] = []
    both_success: list[tuple[str, str]] = []
    missing: list[tuple[str, str, bool, bool]] = []

    for a in MBTI:
        for b in MBTI:
            if a == b:
                continue
            hist = select_latest_pair_run(
                run_metadata=run_metadata,
                scored_run_ids=scored_run_ids,
                task_type="mbti_mcq",
                condition="A_history_to_B",
                persona_a=a,
                persona_b=b,
                model_name=None,
                source_dataset=None,
            )
            summ = select_latest_pair_run(
                run_metadata=run_metadata,
                scored_run_ids=scored_run_ids,
                task_type="mbti_mcq",
                condition="A_summary_to_B",
                persona_a=a,
                persona_b=b,
                model_name=None,
                source_dataset=None,
            )
            if not hist or not summ:
                missing.append((a, b, bool(hist), bool(summ)))
                continue
            hist_ok = final_type_for(hist, mbti_by_run) == b
            summ_ok = final_type_for(summ, mbti_by_run) == b
            if (not hist_ok) and (not summ_ok):
                both_failed.append((a, b))
            if hist_ok and summ_ok:
                both_success.append((a, b))

    premise_mismatch: list[tuple[str, str, str]] = []
    for p in MBTI:
        run_id = select_latest_premise_mbti_only_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type="mbti_mcq",
            premise_persona=p,
            model_name=None,
            source_dataset=None,
        )
        final_type = final_type_for(run_id, mbti_by_run) if run_id else ""
        if final_type != p:
            premise_mismatch.append((p, final_type, run_id or ""))

    excluded_mbti = {p for p, _, _ in premise_mismatch}
    eligible_pairs = [
        (a, b)
        for a in MBTI
        for b in MBTI
        if a != b and a not in excluded_mbti and b not in excluded_mbti
    ]
    filtered_failed = [pair for pair in both_failed if pair[0] not in excluded_mbti and pair[1] not in excluded_mbti]
    filtered_success = [pair for pair in both_success if pair[0] not in excluded_mbti and pair[1] not in excluded_mbti]
    filtered_mixed = [
        pair
        for pair in eligible_pairs
        if pair not in filtered_failed and pair not in filtered_success
    ]

    print("TOTAL_PAIRS_ANALYZED", 240 - len(missing))
    print("MISSING_PAIRS", len(missing))
    print("BOTH_FAILED", len(both_failed))
    print("BOTH_SUCCESS", len(both_success))
    print("BOTH_FAILED_LIST", both_failed)
    print("BOTH_SUCCESS_LIST", both_success)
    print("PREMISE_TOTAL", len(MBTI))
    print("PREMISE_FAILED", len(premise_mismatch))
    print("PREMISE_MISMATCH_LIST", premise_mismatch)
    print("FILTERED_ELIGIBLE_PAIRS", len(eligible_pairs))
    print("FILTERED_BOTH_FAILED", len(filtered_failed))
    print("FILTERED_BOTH_SUCCESS", len(filtered_success))
    print("FILTERED_MIXED", len(filtered_mixed))
    print("FILTERED_BOTH_FAILED_LIST", filtered_failed)
    print("FILTERED_BOTH_SUCCESS_LIST", filtered_success)
    print("FILTERED_MIXED_LIST", filtered_mixed)


if __name__ == "__main__":
    main()
