from __future__ import annotations

from dataclasses import dataclass, field
import json
from typing import Any


Message = dict[str, str]


def _safe_json_loads(value: str | None, default: Any) -> Any:
    if value is None or value == "":
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


def _coerce_json_field(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False)


@dataclass(slots=True)
class ExperimentSample:
    sample_id: str
    task_type: str
    source_dataset: str
    prompt_text: str
    question_text: str
    options_json: str = ""
    target_label: str = ""
    metadata_json: str = ""
    options: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_row(cls, row: dict[str, Any]) -> "ExperimentSample":
        options_json = _coerce_json_field(row.get("options_json", ""))
        metadata_json = _coerce_json_field(row.get("metadata_json", ""))
        return cls(
            sample_id=row["sample_id"],
            task_type=row["task_type"],
            source_dataset=row["source_dataset"],
            prompt_text=row.get("prompt_text", ""),
            question_text=row.get("question_text", ""),
            options_json=options_json,
            target_label=row.get("target_label", ""),
            metadata_json=metadata_json,
            options=_safe_json_loads(options_json, []),
            metadata=_safe_json_loads(metadata_json, {}),
        )


@dataclass(slots=True)
class UsageStats:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0


@dataclass(slots=True)
class ModelResponse:
    text: str
    usage: UsageStats = field(default_factory=UsageStats)
    raw_response: dict[str, Any] = field(default_factory=dict)
    status: str = "success"
    error_message: str | None = None
    cache_hit: bool = False
    latency_seconds: float | None = None
