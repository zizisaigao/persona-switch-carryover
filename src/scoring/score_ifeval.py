from __future__ import annotations

from pathlib import Path
from typing import Any

import nltk

from instruction_following_eval import evaluation_lib

from src.utils.schema import ExperimentSample


def score_response(sample: ExperimentSample, response_text: str) -> dict[str, Any]:
    if not _has_official_ifeval_metadata(sample):
        raise ValueError(
            "IFEval samples must provide official instruction_id_list and kwargs metadata. "
            "The custom fallback scoring route has been removed."
        )
    return _score_with_official_checker(sample, response_text)


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
