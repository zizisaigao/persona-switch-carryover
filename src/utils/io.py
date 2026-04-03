from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import pandas as pd

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


def load_samples(path: Path) -> list[ExperimentSample]:
    suffix = path.suffix.lower()
    if suffix == ".jsonl":
        return _load_rows(path, read_jsonl(path))
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return _load_rows(path, list(reader))
    if suffix == ".parquet":
        dataframe = pd.read_parquet(path)
        return _load_rows(path, dataframe.to_dict(orient="records"))
    raise ValueError(f"Unsupported sample file type: {path.suffix}")


def load_samples_csv(path: Path) -> list[ExperimentSample]:
    return load_samples(path)


def _load_rows(path: Path, rows: list[dict[str, Any]]) -> list[ExperimentSample]:
    if not rows:
        return []

    fieldnames = {key for row in rows for key in row.keys()}
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
    if _looks_like_machine_mindset_rows(fieldnames):
        return _load_machine_mindset_rows(rows)
    if _looks_like_ifeval_rows(fieldnames):
        return _load_ifeval_rows(rows)

    raise ValueError(f"Unsupported sample schema for file: {path}")


def _looks_like_ifeval_rows(fieldnames: set[str]) -> bool:
    return bool(
        {"instruction_id_list", "kwargs", "checks"} & fieldnames
    ) or (
        {"prompt", "instruction", "input"} & fieldnames and "question" not in fieldnames
    )


def _looks_like_machine_mindset_rows(fieldnames: set[str]) -> bool:
    machine_fields = {
        "reference_answer",
        "reference_answers",
        "expected_keywords",
        "rubric",
        "mindset_axis",
    }
    return (
        "question" in fieldnames and bool(machine_fields & fieldnames)
    ) or {"instruction", "output"}.issubset(fieldnames)


def _load_mbti_questionnaire_rows(rows: list[dict[str, Any]]) -> list[ExperimentSample]:
    samples: list[ExperimentSample] = []
    for row in rows:
        options = [
            {"label": "A", "text": str(row["option_a_en"]).strip()},
            {"label": "B", "text": str(row["option_b_en"]).strip()},
        ]
        metadata = {
            "section": row["section"],
            "question_id": row["question_id"],
            "prompt_zh": row["prompt_zh"],
            "option_a_zh": row["option_a_zh"],
            "option_b_zh": row["option_b_zh"],
            "option_dimensions": {
                "A": str(row["option_a_dimension"]).strip(),
                "B": str(row["option_b_dimension"]).strip(),
            },
        }
        samples.append(
            ExperimentSample(
                sample_id=f"mbti_{int(row['question_id']):03d}",
                task_type="mbti_mcq",
                source_dataset="mbti_questions",
                prompt_text="Choose exactly one option. Answer with the option label first, then give a brief reason.",
                question_text=str(row["prompt_en"]).strip(),
                options_json=json.dumps(options, ensure_ascii=False),
                target_label="",
                metadata_json=json.dumps(metadata, ensure_ascii=False),
                options=options,
                metadata=metadata,
            )
        )
    return samples


def _load_ifeval_rows(rows: list[dict[str, Any]]) -> list[ExperimentSample]:
    samples: list[ExperimentSample] = []
    for index, row in enumerate(rows, start=1):
        instruction_text = _first_non_empty(
            row.get("question_text"),
            row.get("prompt"),
            row.get("instruction"),
            row.get("input"),
        )
        checks = _collect_explicit_checks(row)
        metadata = {
            "checks": checks,
            "instruction_id_list": _normalize_json_field(row.get("instruction_id_list"), []),
            "kwargs": _sanitize_ifeval_kwargs(_normalize_json_field(row.get("kwargs"), {})),
            "split": row.get("split", ""),
            "source_record": {
                key: value
                for key, value in row.items()
                if key
                not in {
                    "sample_id",
                    "prompt_text",
                    "question_text",
                    "prompt",
                    "instruction",
                    "input",
                    "target_label",
                    "checks",
                    "required_substrings",
                    "forbidden_substrings",
                    "required_regexes",
                    "forbidden_regexes",
                    "response_must_start_with",
                    "response_must_end_with",
                    "bullet_count_equals",
                    "line_count_equals",
                    "word_count_equals",
                    "min_word_count",
                    "max_word_count",
                    "sentence_count_equals",
                    "min_sentences",
                    "max_sentences",
                    "must_be_json",
                }
            },
        }
        metadata = _json_safe(metadata)
        sample = ExperimentSample(
            sample_id=str(row.get("sample_id") or f"ifeval_{index:04d}"),
            task_type="ifeval",
            source_dataset=str(row.get("source_dataset") or "ifeval"),
            prompt_text=str(row.get("prompt_text") or "Follow the instruction exactly."),
            question_text=instruction_text,
            options_json="",
            target_label=str(row.get("target_label") or "ifeval_rules"),
            metadata_json=json.dumps(metadata, ensure_ascii=False),
            options=[],
            metadata=metadata,
        )
        samples.append(sample)
    return samples


def _load_machine_mindset_rows(rows: list[dict[str, Any]]) -> list[ExperimentSample]:
    samples: list[ExperimentSample] = []
    for index, row in enumerate(rows, start=1):
        metadata = {
            "reference_answer": row.get("reference_answer") or row.get("output", ""),
            "reference_answers": _normalize_json_field(row.get("reference_answers"), []),
            "expected_keywords": _normalize_json_field(row.get("expected_keywords"), []),
            "rubric": row.get("rubric", ""),
            "mindset_axis": row.get("mindset_axis", ""),
            "difficulty": row.get("difficulty", ""),
            "topic": row.get("topic", ""),
            "language": row.get("language", ""),
            "source_file": row.get("source_file", ""),
            "source_group": row.get("source_group", ""),
            "mbti_type": row.get("mbti_type", ""),
            "mbti_dimension": row.get("mbti_dimension", ""),
            "mbti_pole": row.get("mbti_pole", ""),
            "mbti_code": row.get("mbti_code", ""),
        }
        metadata = _json_safe(metadata)
        sample = ExperimentSample(
            sample_id=str(row.get("sample_id") or f"machine_mindset_{index:04d}"),
            task_type="machine_mindset",
            source_dataset=str(row.get("source_dataset") or "machine_mindset"),
            prompt_text=str(row.get("prompt_text") or "Answer as if you are giving practical advice."),
            question_text=_first_non_empty(
                row.get("question_text"),
                row.get("question"),
                row.get("prompt"),
                _merge_instruction_input(row.get("instruction"), row.get("input")),
            ),
            options_json="",
            target_label=str(row.get("target_label") or ""),
            metadata_json=json.dumps(metadata, ensure_ascii=False),
            options=[],
            metadata=metadata,
        )
        samples.append(sample)
    return samples


def _collect_explicit_checks(row: dict[str, Any]) -> list[dict[str, Any]]:
    if "checks" in row and row["checks"] not in (None, "", []):
        existing = _normalize_json_field(row["checks"], [])
        if isinstance(existing, dict):
            return [existing]
        if isinstance(existing, list):
            return [item for item in existing if isinstance(item, dict)]

    checks: list[dict[str, Any]] = []
    direct_mappings = {
        "required_substrings": "required_substrings",
        "forbidden_substrings": "forbidden_substrings",
        "required_regexes": "required_regexes",
        "forbidden_regexes": "forbidden_regexes",
        "response_must_start_with": "response_must_start_with",
        "response_must_end_with": "response_must_end_with",
        "bullet_count_equals": "bullet_count_equals",
        "line_count_equals": "line_count_equals",
        "word_count_equals": "word_count_equals",
        "min_word_count": "min_word_count",
        "max_word_count": "max_word_count",
        "sentence_count_equals": "sentence_count_equals",
        "min_sentences": "min_sentences",
        "max_sentences": "max_sentences",
        "must_be_json": "must_be_json",
        "exact_match": "exact_match",
    }
    for field_name, check_type in direct_mappings.items():
        value = row.get(field_name)
        if value in (None, "", []):
            continue
        checks.append({"type": check_type, "value": _normalize_json_field(value, value)})
    return checks


def _normalize_json_field(value: Any, default: Any) -> Any:
    if value is None:
        return default
    if hasattr(value, "tolist"):
        value = value.tolist()
    if isinstance(value, (list, dict, int, float, bool)):
        return value
    if isinstance(value, str):
        if value == "":
            return default
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value


def _json_safe(value: Any) -> Any:
    if hasattr(value, "tolist"):
        value = value.tolist()
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    return value


def _sanitize_ifeval_kwargs(value: Any) -> list[dict[str, Any]]:
    value = _json_safe(value)
    if isinstance(value, dict):
        value = [value]
    if not isinstance(value, list):
        return []

    cleaned: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        cleaned.append(
            {
                str(key): subvalue
                for key, subvalue in item.items()
                if subvalue is not None and subvalue != ""
            }
        )
    return cleaned


def _first_non_empty(*values: Any) -> str:
    for value in values:
        if value not in (None, ""):
            return str(value).strip()
    return ""


def _merge_instruction_input(instruction: Any, model_input: Any) -> str:
    instruction_text = "" if instruction in (None, "") else str(instruction).strip()
    input_text = "" if model_input in (None, "") else str(model_input).strip()
    if instruction_text and input_text:
        return f"{instruction_text}\n\nAdditional input:\n{input_text}"
    return instruction_text or input_text
