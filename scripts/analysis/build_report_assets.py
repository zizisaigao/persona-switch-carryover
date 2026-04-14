from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.analysis.run_selection import build_run_metadata, select_latest_pair_run, select_latest_premise_mbti_only_run
from src.scoring.score_mbti import aggregate_profiles
from src.utils.io import read_jsonl


TABLES_DIR = PROJECT_ROOT / "outputs" / "tables"
SCORED_DIR = PROJECT_ROOT / "outputs" / "scored"
RAW_FILE = PROJECT_ROOT / "outputs" / "raw_generations" / "generations.jsonl"
REPORT_DIR = PROJECT_ROOT / "reports" / "final_report_assets"

DIMENSIONS = [
    ("E", "I", "EI"),
    ("S", "N", "SN"),
    ("T", "F", "TF"),
    ("J", "P", "JP"),
]


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    rq1_pairs = pd.read_csv(TABLES_DIR / "rq1_twoway240_full_run_pair_switch_table.csv")
    rq1_overall = pd.read_csv(TABLES_DIR / "rq1_twoway240_full_run_overall_by_task_track.csv")
    rq2_overall = pd.read_csv(TABLES_DIR / "rq2_selected66_stable_control_full_run_overall_by_task_track.csv")
    rq3_overall = pd.read_csv(TABLES_DIR / "rq3_selected66_stable_control_full_run_overall_by_task_track.csv")
    filtered_pairs = _load_filtered_pairs(PROJECT_ROOT / "reports" / "rq1_filtered_pair_groups.md")
    premise_summary = _build_premise_summary()
    symmetry_summary = _build_symmetry_summary(rq1_pairs, filtered_pairs)
    distance_summary = _build_distance_summary(rq1_pairs, filtered_pairs)
    dimension_summary = _build_dimension_summary(rq1_pairs, filtered_pairs)
    drift_summary = _build_drift_summary(filtered_pairs)
    rq1_task_summary = _build_rq1_task_summary(rq1_overall)

    premise_summary.to_csv(REPORT_DIR / "premise_summary.csv", index=False)
    symmetry_summary.to_csv(REPORT_DIR / "rq1_symmetry_summary.csv", index=False)
    distance_summary.to_csv(REPORT_DIR / "rq1_distance_summary.csv", index=False)
    dimension_summary.to_csv(REPORT_DIR / "rq1_dimension_summary.csv", index=False)
    drift_summary.to_csv(REPORT_DIR / "matched_control_drift_summary.csv", index=False)
    rq1_task_summary.to_csv(REPORT_DIR / "rq1_task_summary.csv", index=False)
    rq2_overall.to_csv(REPORT_DIR / "rq2_selected66_stable_control_overall.csv", index=False)
    rq3_overall.to_csv(REPORT_DIR / "rq3_selected66_stable_control_overall.csv", index=False)

    _plot_rq1_track_summary(rq1_task_summary)
    _plot_rq1_distance(distance_summary)
    _plot_rq1_dimension(dimension_summary)
    _plot_rq2_rq3(rq2_overall, rq3_overall)


def _load_filtered_pairs(path: Path) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("- `") or " -> " not in line:
            continue
        content = line.removeprefix("- `").removesuffix("`")
        left, right = content.split(" -> ")
        pair = (left.strip(), right.strip())
        if pair not in pairs:
            pairs.append(pair)
    return pairs


def _build_premise_summary() -> pd.DataFrame:
    raw_records = read_jsonl(RAW_FILE)
    run_metadata = build_run_metadata(raw_records)
    scored_records: list[dict[str, object]] = []
    for path in sorted(SCORED_DIR.glob("*_scores.jsonl")):
        scored_records.extend(read_jsonl(path))
    scored_run_ids = {str(record["run_id"]) for record in scored_records}
    by_run: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in scored_records:
        if record.get("task_type") != "mbti_mcq":
            continue
        by_run[str(record["run_id"])].append(record)

    rows: list[dict[str, object]] = []
    for persona in [
        "INTJ",
        "INFJ",
        "ENFJ",
        "ISFJ",
        "ENTJ",
        "ENTP",
        "ESTP",
        "ISTP",
        "ESFP",
        "ISFP",
        "ENFP",
        "ISTJ",
        "INTP",
        "INFP",
        "ESFJ",
        "ESTJ",
    ]:
        default_run = select_latest_premise_mbti_only_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type="mbti_mcq",
            premise_persona=persona,
            model_name="gemini-2.5-flash-lite",
            source_dataset=None,
        )
        strong_run = select_latest_pair_run(
            run_metadata=run_metadata,
            scored_run_ids=scored_run_ids,
            task_type="mbti_mcq",
            condition="MBTI_only_strong",
            persona_a=persona,
            persona_b=persona,
            model_name="gemini-2.5-flash-lite",
            source_dataset=None,
        )
        default_final = _final_type_from_run(by_run.get(default_run or "", []))
        strong_final = _final_type_from_run(by_run.get(strong_run or "", []))
        rows.append(
            {
                "persona": persona,
                "rq1_premise_final_type": default_final,
                "rq1_self_match": default_final == persona,
                "rq2_strong_premise_final_type": strong_final,
                "rq2_strong_self_match": strong_final == persona,
                "stable_in_both": default_final == persona and strong_final == persona,
            }
        )
    return pd.DataFrame(rows)


def _final_type_from_run(records: list[dict[str, object]]) -> str:
    aggregates = aggregate_profiles(records)
    if not aggregates:
        return ""
    return str(aggregates[0].get("final_type", ""))


def _build_symmetry_summary(rq1_pairs: pd.DataFrame, filtered_pairs: list[tuple[str, str]]) -> pd.DataFrame:
    mbti = rq1_pairs[(rq1_pairs["task_type"] == "mbti_mcq")].copy()
    filtered_set = {f"{a}_to_{b}" for a, b in filtered_pairs}
    mbti = mbti[mbti["pair_id"].isin(filtered_set)].copy()
    lookup = {
        (row["persona_a"], row["persona_b"], row["retain_mechanism"]): bool(row["switch_reaches_target_b"])
        for _, row in mbti.iterrows()
    }
    rows: list[dict[str, object]] = []
    stable_personas = sorted({left for left, _ in filtered_pairs} | {right for _, right in filtered_pairs})
    for track in ["history", "summary"]:
        symmetric = 0
        asymmetric = 0
        both_success = 0
        both_fail = 0
        for i, left in enumerate(stable_personas):
            for right in stable_personas[i + 1 :]:
                forward = lookup.get((left, right, track))
                backward = lookup.get((right, left, track))
                if forward is None or backward is None:
                    continue
                if forward == backward:
                    symmetric += 1
                else:
                    asymmetric += 1
                if forward and backward:
                    both_success += 1
                if (not forward) and (not backward):
                    both_fail += 1
        total = symmetric + asymmetric
        rows.append(
            {
                "retain_mechanism": track,
                "unordered_pairs": total,
                "symmetric_pairs": symmetric,
                "asymmetric_pairs": asymmetric,
                "symmetry_rate": round(symmetric / total, 4) if total else 0.0,
                "both_success_pairs": both_success,
                "both_fail_pairs": both_fail,
            }
        )
    return pd.DataFrame(rows)


def _build_distance_summary(rq1_pairs: pd.DataFrame, filtered_pairs: list[tuple[str, str]]) -> pd.DataFrame:
    mbti = rq1_pairs[(rq1_pairs["task_type"] == "mbti_mcq")].copy()
    filtered_set = {f"{a}_to_{b}" for a, b in filtered_pairs}
    mbti = mbti[mbti["pair_id"].isin(filtered_set)].copy()
    rows: list[dict[str, object]] = []
    for track in ["history", "summary"]:
        subset = mbti[mbti["retain_mechanism"] == track].copy()
        subset["distance"] = subset.apply(lambda row: _mbti_distance(str(row["persona_a"]), str(row["persona_b"])), axis=1)
        for distance in [1, 2, 3, 4]:
            group = subset[subset["distance"] == distance]
            rows.append(
                {
                    "retain_mechanism": track,
                    "distance": distance,
                    "n_pairs": int(len(group)),
                    "share_switch_reaches_target_b": round(group["switch_reaches_target_b"].astype(float).mean(), 4),
                    "mean_primary_gap_abs": round(group["primary_gap_abs"].astype(float).mean(), 4),
                    "mean_scs": round(group["scs_value"].astype(float).mean(), 4),
                    "mean_rai": round(group["rai_value"].astype(float).mean(), 4),
                }
            )
    return pd.DataFrame(rows)


def _build_dimension_summary(rq1_pairs: pd.DataFrame, filtered_pairs: list[tuple[str, str]]) -> pd.DataFrame:
    mbti = rq1_pairs[(rq1_pairs["task_type"] == "mbti_mcq")].copy()
    filtered_set = {f"{a}_to_{b}" for a, b in filtered_pairs}
    mbti = mbti[mbti["pair_id"].isin(filtered_set)].copy()
    rows: list[dict[str, object]] = []
    for track in ["history", "summary"]:
        subset = mbti[mbti["retain_mechanism"] == track]
        for _, _, dim_name in DIMENSIONS:
            outcomes: list[str] = []
            success_flags: list[bool] = []
            for _, row in subset.iterrows():
                persona_a = str(row["persona_a"])
                persona_b = str(row["persona_b"])
                final_type = str(row["final_type_switch"])
                idx = _dimension_index(dim_name)
                if persona_a[idx] == persona_b[idx]:
                    continue
                success_flags.append(bool(row["switch_reaches_target_b"]))
                if len(final_type) != 4 or final_type[idx] == "X":
                    outcomes.append("other")
                elif final_type[idx] == persona_a[idx]:
                    outcomes.append("a_letter")
                elif final_type[idx] == persona_b[idx]:
                    outcomes.append("b_letter")
                else:
                    outcomes.append("other")
            counts = Counter(outcomes)
            total = sum(counts.values())
            rows.append(
                {
                    "retain_mechanism": track,
                    "dimension": dim_name,
                    "n_pairs": total,
                    "a_letter_rate": round(counts["a_letter"] / total, 4) if total else 0.0,
                    "b_letter_rate": round(counts["b_letter"] / total, 4) if total else 0.0,
                    "other_rate": round(counts["other"] / total, 4) if total else 0.0,
                    "share_switch_reaches_target_b": round(mean(1.0 if item else 0.0 for item in success_flags), 4)
                    if success_flags
                    else 0.0,
                }
            )
    return pd.DataFrame(rows)


def _build_drift_summary(filtered_pairs: list[tuple[str, str]]) -> pd.DataFrame:
    raw_records = read_jsonl(RAW_FILE)
    run_metadata = build_run_metadata(raw_records)
    profiles = {}
    for path in TABLES_DIR.glob("persona_*_mbti_profiles.jsonl"):
        rows = read_jsonl(path)
        if rows:
            profiles[str(rows[0]["run_id"])] = rows[0]
    scored_run_ids = set(profiles)

    rows: list[dict[str, object]] = []
    rq2_pairs = _load_pairs_from_command_doc(PROJECT_ROOT / "reports" / "rq2_selected_60_commands.md", 60)
    rq3_pairs = _load_pairs_from_command_doc(PROJECT_ROOT / "reports" / "rq3_selected_60_commands.md", 60)

    for rq_name, pair_source, history_condition, summary_condition in [
        ("RQ1", filtered_pairs, "B_history_to_B", "B_summary_to_B"),
        ("RQ2", rq2_pairs, "B_history_to_B_strong", "B_summary_to_B_strong"),
        ("RQ3", rq3_pairs, "B3_history_to_B", "B3_summary_to_B"),
    ]:
        for persona_a, persona_b in pair_source:
            history = _latest_profile(
                run_metadata,
                scored_run_ids,
                profiles,
                history_condition,
                persona_a,
                persona_b,
            )
            summary = _latest_profile(
                run_metadata,
                scored_run_ids,
                profiles,
                summary_condition,
                persona_a,
                persona_b,
            )
            rows.append(
                {
                    "rq": rq_name,
                    "pair_id": f"{persona_a}_to_{persona_b}",
                    "persona_a": persona_a,
                    "persona_b": persona_b,
                    "history_final_type": history.get("final_type", "") if history else "",
                    "summary_final_type": summary.get("final_type", "") if summary else "",
                    "history_drift": bool(history and history.get("final_type") != persona_b),
                    "summary_drift": bool(summary and summary.get("final_type") != persona_b),
                }
            )
    return pd.DataFrame(rows)


def _load_pairs_from_command_doc(path: Path, limit: int) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("- `") or " -> " not in line:
            continue
        content = line.removeprefix("- `").removesuffix("`")
        left, right = content.split(" -> ")
        pair = (left.strip(), right.strip())
        if pair not in pairs:
            pairs.append(pair)
        if len(pairs) == limit:
            break
    return pairs


def _latest_profile(
    run_metadata: dict[str, dict[str, object]],
    scored_run_ids: set[str],
    profiles: dict[str, dict[str, object]],
    condition: str,
    persona_a: str,
    persona_b: str,
) -> dict[str, object] | None:
    run_id = select_latest_pair_run(
        run_metadata=run_metadata,
        scored_run_ids=scored_run_ids,
        task_type="mbti_mcq",
        condition=condition,
        persona_a=persona_a,
        persona_b=persona_b,
        model_name="gemini-2.5-flash-lite",
        source_dataset=None,
    )
    if not run_id:
        return None
    return profiles.get(run_id)


def _build_rq1_task_summary(rq1_overall: pd.DataFrame) -> pd.DataFrame:
    subset = rq1_overall.copy()
    subset = subset.rename(columns={"mean_gap": "mean_primary_gap_abs"})
    return subset


def _mbti_distance(left: str, right: str) -> int:
    return sum(1 for ltr_left, ltr_right in zip(left, right) if ltr_left != ltr_right)


def _dimension_index(name: str) -> int:
    return {"EI": 0, "SN": 1, "TF": 2, "JP": 3}[name]


def _plot_rq1_track_summary(df: pd.DataFrame) -> None:
    mbti = df[df["task_type"] == "mbti_mcq"]
    fig, ax = plt.subplots(figsize=(7, 4))
    history = mbti[mbti["retain_mechanism"] == "history"]["share_switch_reaches_target_b"].tolist()
    summary = mbti[mbti["retain_mechanism"] == "summary"]["share_switch_reaches_target_b"].tolist()
    labels = ["history", "summary"]
    values = [history[0] if history else 0.0, summary[0] if summary else 0.0]
    ax.bar(labels, values, color=["#c44e52", "#4c72b0"])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Share")
    ax.set_title("RQ1 MBTI Target Reach by Retention Mechanism")
    fig.tight_layout()
    fig.savefig(REPORT_DIR / "rq1_mbti_target_reach.png", dpi=200)
    plt.close(fig)


def _plot_rq1_distance(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    for track, color in [("history", "#c44e52"), ("summary", "#4c72b0")]:
        subset = df[df["retain_mechanism"] == track]
        ax.plot(subset["distance"], subset["share_switch_reaches_target_b"], marker="o", label=track, color=color)
    ax.set_xlabel("Number of MBTI dimensions changed")
    ax.set_ylabel("MBTI target reach")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_ylim(0, 1)
    ax.set_title("RQ1 Success Rate by Persona Distance")
    ax.legend()
    fig.tight_layout()
    fig.savefig(REPORT_DIR / "rq1_distance_success.png", dpi=200)
    plt.close(fig)


def _plot_rq1_dimension(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for ax, track, color in zip(axes, ["history", "summary"], ["#c44e52", "#4c72b0"]):
        subset = df[df["retain_mechanism"] == track]
        ax.bar(subset["dimension"], subset["a_letter_rate"], color=color)
        ax.set_title(f"{track}: A-letter retention")
        ax.set_ylim(0, 1)
        ax.set_xlabel("MBTI dimension")
    axes[0].set_ylabel("Rate")
    fig.tight_layout()
    fig.savefig(REPORT_DIR / "rq1_dimension_carryover.png", dpi=200)
    plt.close(fig)


def _plot_rq2_rq3(rq2_overall: pd.DataFrame, rq3_overall: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    labels = [f"{row.task_type}\n{row.retain_mechanism}" for row in rq2_overall.itertuples()]
    axes[0].bar(labels, rq2_overall["share_rq2_improved"], color="#55a868")
    axes[0].set_ylim(0, 1)
    axes[0].set_title("RQ2: Share of Pairs Improved")
    axes[0].tick_params(axis="x", rotation=45)

    labels = [f"{row.task_type}\n{row.retain_mechanism}" for row in rq3_overall.itertuples()]
    axes[1].bar(labels, rq3_overall["share_rq3_weakened"], color="#8172b2")
    axes[1].set_ylim(0, 1)
    axes[1].set_title("RQ3: Share of Pairs Weakened")
    axes[1].tick_params(axis="x", rotation=45)

    fig.tight_layout()
    fig.savefig(REPORT_DIR / "rq2_rq3_overview.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
