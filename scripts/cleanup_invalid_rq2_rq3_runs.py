from __future__ import annotations

import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.rq2_rq3_selected_60_plan import (
    RQ2_CONDITIONS,
    RQ2_PAIRS,
    RQ2_STRONG_PREMISE_RERUN_13,
    RQ3_CONDITIONS,
    RQ3_PAIRS,
)


def iter_jsonl(path: Path):
    if not path.exists():
        return
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def write_jsonl(path: Path, records: list[dict]) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    tmp_path.replace(path)


RQ2_PAIR_SET = {(pair["A"], pair["B"]) for pair in RQ2_PAIRS}
RQ3_PAIR_SET = {(pair["A"], pair["B"]) for pair in RQ3_PAIRS}
RERUN_13_SET = set(RQ2_STRONG_PREMISE_RERUN_13)
RQ2_CONDITION_SET = set(RQ2_CONDITIONS)
RQ3_CONDITION_SET = set(RQ3_CONDITIONS)


def should_purge(record: dict) -> bool:
    condition = record.get("condition")
    persona_a = record.get("persona_a")
    persona_b = record.get("persona_b")

    if condition == "MBTI_only_strong":
        return persona_a == persona_b and persona_a in RERUN_13_SET

    if condition in RQ2_CONDITION_SET:
        return (persona_a, persona_b) in RQ2_PAIR_SET

    if condition in RQ3_CONDITION_SET:
        return (persona_a, persona_b) in RQ3_PAIR_SET

    return False


def main() -> None:
    raw_path = PROJECT_ROOT / "outputs" / "raw_generations" / "generations.jsonl"
    usage_path = PROJECT_ROOT / "outputs" / "logs" / "api_usage.jsonl"
    scored_dir = PROJECT_ROOT / "outputs" / "scored"
    tables_dir = PROJECT_ROOT / "outputs" / "tables"

    raw_records = list(iter_jsonl(raw_path))
    kept_raw: list[dict] = []
    purge_run_ids: set[str] = set()

    for record in raw_records:
        if should_purge(record):
            run_id = record.get("run_id")
            if run_id:
                purge_run_ids.add(run_id)
            continue
        kept_raw.append(record)

    write_jsonl(raw_path, kept_raw)

    usage_records = list(iter_jsonl(usage_path))
    kept_usage = [record for record in usage_records if record.get("run_id") not in purge_run_ids]
    write_jsonl(usage_path, kept_usage)

    removed_scored = 0
    removed_profiles = 0
    for run_id in purge_run_ids:
        scored_path = scored_dir / f"{run_id}_scores.jsonl"
        if scored_path.exists():
            scored_path.unlink()
            removed_scored += 1

        profile_path = tables_dir / f"{run_id}_mbti_profiles.jsonl"
        if profile_path.exists():
            profile_path.unlink()
            removed_profiles += 1

    print(
        json.dumps(
            {
                "purged_run_ids": len(purge_run_ids),
                "remaining_raw_records": len(kept_raw),
                "remaining_usage_records": len(kept_usage),
                "removed_scored_files": removed_scored,
                "removed_profile_files": removed_profiles,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
