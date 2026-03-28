from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from src.utils.schema import ExperimentSample


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def ensure_parent_dir(path: Path) -> None:
    ensure_dir(path.parent)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    ensure_parent_dir(path)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    ensure_parent_dir(path)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def load_samples_csv(path: Path) -> list[ExperimentSample]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if not rows:
        return []

    fieldnames = set(rows[0].keys())
    unified_fields = {
        "sample_id",
        "task_type",
        "source_dataset",
        "prompt_text",
        "question_text",
        "options_json",
        "target_label",
        "metadata_json",
    }
    mbti_raw_fields = {
        "question_id",
        "section",
        "prompt_zh",
        "option_a_zh",
        "option_b_zh",
        "option_a_dimension",
        "option_b_dimension",
        "prompt_en",
        "option_a_en",
        "option_b_en",
    }

    if unified_fields.issubset(fieldnames):
        return [ExperimentSample.from_row(row) for row in rows]
    if mbti_raw_fields.issubset(fieldnames):
        return _load_mbti_questionnaire_rows(rows)

    raise ValueError(f"Unsupported CSV schema for file: {path}")


def _load_mbti_questionnaire_rows(rows: list[dict[str, str]]) -> list[ExperimentSample]:
    samples: list[ExperimentSample] = []
    for row in rows:
        options = [
            {"label": "A", "text": row["option_a_en"].strip()},
            {"label": "B", "text": row["option_b_en"].strip()},
        ]
        metadata = {
            "section": row["section"],
            "question_id": row["question_id"],
            "prompt_zh": row["prompt_zh"],
            "option_a_zh": row["option_a_zh"],
            "option_b_zh": row["option_b_zh"],
            "option_dimensions": {
                "A": row["option_a_dimension"].strip(),
                "B": row["option_b_dimension"].strip(),
            },
        }
        samples.append(
            ExperimentSample(
                sample_id=f"mbti_{int(row['question_id']):03d}",
                task_type="mbti_mcq",
                source_dataset="mbti_questions",
                prompt_text="Choose exactly one option. Answer with the option label first, then give a brief reason.",
                question_text=row["prompt_en"].strip(),
                options_json=json.dumps(options, ensure_ascii=False),
                target_label="",
                metadata_json=json.dumps(metadata, ensure_ascii=False),
                options=options,
                metadata=metadata,
            )
        )
    return samples
