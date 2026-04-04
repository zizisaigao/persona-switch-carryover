from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import nltk

from instruction_following_eval import evaluation_lib

from src.utils.schema import ExperimentSample


def score_response(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    if _has_official_ifeval_metadata(sample):
        return _score_with_official_checker(sample, response_text)
    return _score_with_custom_checks(sample, response_text)


def _has_official_ifeval_metadata(sample: ExperimentSample) -> bool:
    instruction_ids = sample.metadata.get("instruction_id_list")
    kwargs_list = sample.metadata.get("kwargs")
    return isinstance(instruction_ids, list) and isinstance(kwargs_list, list) and bool(instruction_ids)


def _score_with_official_checker(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    _ensure_nltk_punkt()
    sanitized_kwargs = _normalize_official_kwargs(sample.metadata.get("kwargs", []))
    input_example = evaluation_lib.InputExample(
        key=int(sample.metadata.get("source_record", {}).get("key", 0) or 0),
        instruction_id_list=list(sample.metadata["instruction_id_list"]),
        prompt=sample.question_text,
        kwargs=sanitized_kwargs,
    )
    prompt_to_response = {sample.question_text: response_text}
    strict_output = evaluation_lib.test_instruction_following_strict(input_example, prompt_to_response)
    loose_output = evaluation_lib.test_instruction_following_loose(input_example, prompt_to_response)
    return {
        "sample_id": sample.sample_id,
        "score_type": "ifeval",
        "target_label": sample.target_label,
        "checker_source": "official_google_ifeval",
        "instruction_count": len(input_example.instruction_id_list),
        "strict_follow_all": strict_output.follow_all_instructions,
        "strict_follow_instruction_list": strict_output.follow_instruction_list,
        "strict_checks_passed": sum(strict_output.follow_instruction_list),
        "loose_follow_all": loose_output.follow_all_instructions,
        "loose_follow_instruction_list": loose_output.follow_instruction_list,
        "loose_checks_passed": sum(loose_output.follow_instruction_list),
        "meets_constraint": strict_output.follow_all_instructions,
    }


def _normalize_official_kwargs(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    normalized = [_normalize_official_value(item) for item in value]
    return [item for item in normalized if isinstance(item, dict)]


def _normalize_official_value(value: Any) -> Any:
    if isinstance(value, list):
        return [_normalize_official_value(item) for item in value]
    if isinstance(value, dict):
        return {
            str(key): _normalize_official_value(item)
            for key, item in value.items()
        }
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def _ensure_nltk_punkt() -> None:
    local_nltk_dir = Path(__file__).resolve().parents[2] / "outputs" / "nltk_data"
    local_nltk_dir.mkdir(parents=True, exist_ok=True)
    local_nltk_dir_str = str(local_nltk_dir)
    if local_nltk_dir_str not in nltk.data.path:
        nltk.data.path.insert(0, local_nltk_dir_str)
    try:
        nltk.data.find("tokenizers/punkt/english.pickle")
    except LookupError:
        nltk.download("punkt", download_dir=local_nltk_dir_str, quiet=True)


def _score_with_custom_checks(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    checks = _extract_checks(sample)
    check_results = [_evaluate_check(check, response_text) for check in checks]
    checks_failed = [result for result in check_results if not result["passed"]]
    passed_all = all(result["passed"] for result in check_results) if check_results else True
    return {
        "sample_id": sample.sample_id,
        "score_type": "ifeval",
        "target_label": sample.target_label,
        "checker_source": "custom_rules",
        "checks_total": len(check_results),
        "checks_passed": len(check_results) - len(checks_failed),
        "checks_failed": len(checks_failed),
        "meets_constraint": passed_all,
        "failed_checks": checks_failed,
    }


def _extract_checks(sample: ExperimentSample) -> list[dict[str, Any]]:
    metadata_checks = sample.metadata.get("checks", [])
    if isinstance(metadata_checks, dict):
        metadata_checks = [metadata_checks]

    checks = [check for check in metadata_checks if isinstance(check, dict)]
    if checks:
        return checks

    legacy_checks: list[dict[str, Any]] = []
    if sample.target_label == "format_two_bullets":
        legacy_checks.append({"type": "bullet_count_equals", "value": 2})
    return legacy_checks


def _evaluate_check(check: dict[str, Any], response_text: str) -> dict[str, Any]:
    check_type = str(check.get("type", "")).strip()
    value = check.get("value")
    normalized = response_text.strip()
    lowered = normalized.lower()

    if check_type == "required_substrings":
        missing = [item for item in _to_string_list(value) if item.lower() not in lowered]
        return _result(check_type, not missing, {"missing": missing})
    if check_type == "forbidden_substrings":
        present = [item for item in _to_string_list(value) if item.lower() in lowered]
        return _result(check_type, not present, {"present": present})
    if check_type == "required_regexes":
        missing = [pattern for pattern in _to_string_list(value) if not re.search(pattern, response_text, flags=re.MULTILINE)]
        return _result(check_type, not missing, {"missing": missing})
    if check_type == "forbidden_regexes":
        present = [pattern for pattern in _to_string_list(value) if re.search(pattern, response_text, flags=re.MULTILINE)]
        return _result(check_type, not present, {"present": present})
    if check_type == "response_must_start_with":
        prefix = str(value)
        return _result(check_type, normalized.startswith(prefix), {"expected": prefix})
    if check_type == "response_must_end_with":
        suffix = str(value)
        return _result(check_type, normalized.endswith(suffix), {"expected": suffix})
    if check_type == "exact_match":
        expected = str(value)
        return _result(check_type, normalized == expected, {"expected": expected})
    if check_type == "bullet_count_equals":
        bullet_count = len(_bullet_lines(response_text))
        expected = _to_int(value)
        return _result(check_type, bullet_count == expected, {"actual": bullet_count, "expected": expected})
    if check_type == "line_count_equals":
        actual = len(_non_empty_lines(response_text))
        expected = _to_int(value)
        return _result(check_type, actual == expected, {"actual": actual, "expected": expected})
    if check_type == "word_count_equals":
        actual = len(_words(response_text))
        expected = _to_int(value)
        return _result(check_type, actual == expected, {"actual": actual, "expected": expected})
    if check_type == "min_word_count":
        actual = len(_words(response_text))
        expected = _to_int(value)
        return _result(check_type, actual >= expected, {"actual": actual, "expected": expected})
    if check_type == "max_word_count":
        actual = len(_words(response_text))
        expected = _to_int(value)
        return _result(check_type, actual <= expected, {"actual": actual, "expected": expected})
    if check_type == "sentence_count_equals":
        actual = len(_sentences(response_text))
        expected = _to_int(value)
        return _result(check_type, actual == expected, {"actual": actual, "expected": expected})
    if check_type == "min_sentences":
        actual = len(_sentences(response_text))
        expected = _to_int(value)
        return _result(check_type, actual >= expected, {"actual": actual, "expected": expected})
    if check_type == "max_sentences":
        actual = len(_sentences(response_text))
        expected = _to_int(value)
        return _result(check_type, actual <= expected, {"actual": actual, "expected": expected})
    if check_type == "must_be_json":
        try:
            json.loads(response_text)
            is_valid_json = True
        except json.JSONDecodeError:
            is_valid_json = False
        return _result(check_type, is_valid_json, {})

    return _result(check_type or "unknown", False, {"error": "Unsupported check type"})


def _result(check_type: str, passed: bool, details: dict[str, Any]) -> dict[str, Any]:
    return {
        "check_type": check_type,
        "passed": passed,
        "details": details,
    }


def _to_string_list(value: Any) -> list[str]:
    if value in (None, ""):
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _to_int(value: Any) -> int:
    if isinstance(value, int):
        return value
    return int(str(value).strip())


def _bullet_lines(text: str) -> list[str]:
    return [
        line
        for line in text.splitlines()
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line)
    ]


def _non_empty_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip()]


def _words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9']+", text)


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|\n+", text.strip())
    return [part for part in parts if part.strip()]
