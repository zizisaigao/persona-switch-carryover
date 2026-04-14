from __future__ import annotations

import os
import time
from typing import Any

from google import genai
from google.genai import types

from src.models.base_client import BaseClient
from src.models.pricing import estimate_cost_usd
from src.utils.schema import Message, ModelResponse, UsageStats


class GeminiClient(BaseClient):
    provider_name = "gemini"

    def __init__(
        self,
        *,
        api_key_env: str,
        timeout_seconds: int = 60,
        max_retries: int = 3,
    ) -> None:
        self.api_key = os.getenv(api_key_env, "")
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None

    def generate(
        self,
        *,
        messages: list[Message],
        model_name: str,
        temperature: float,
        max_tokens: int,
    ) -> ModelResponse:
        if not self.api_key:
            return ModelResponse(
                text="",
                status="error",
                error_message="Missing Gemini API key in environment.",
            )
        if self.client is None:
            return ModelResponse(
                text="",
                status="error",
                error_message="Gemini client could not be initialized.",
            )

        system_instruction, contents = _messages_to_gemini_payload(messages)
        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
            system_instruction=system_instruction or None,
            http_options=types.HttpOptions(timeout=self.timeout_seconds * 1000),
        )

        last_error: str | None = None
        for attempt in range(self.max_retries + 1):
            start = time.perf_counter()
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=contents,
                    config=config,
                )
                latency = time.perf_counter() - start
                data = _normalize_response_payload(response)
                usage = self._parse_usage(getattr(response, "usage_metadata", None))
                usage.cost_usd = estimate_cost_usd(model_name, usage)
                text = self._extract_text(response, data)
                if not text:
                    finish_reason = _extract_finish_reason(response, data)
                    prompt_feedback = data.get("promptFeedback", {})
                    return ModelResponse(
                        text="",
                        usage=usage,
                        raw_response=data,
                        status="error",
                        error_message=(
                            f"Gemini returned no text output. "
                            f"finish_reason={finish_reason!r}, prompt_feedback={prompt_feedback!r}"
                        ),
                        latency_seconds=round(latency, 4),
                    )
                return ModelResponse(
                    text=text,
                    usage=usage,
                    raw_response=data,
                    status="success",
                    latency_seconds=round(latency, 4),
                )
            except Exception as exc:  # pragma: no cover - runtime provider path
                last_error = str(exc)
                if attempt >= self.max_retries:
                    break
                time.sleep(2 ** attempt)

        return ModelResponse(
            text="",
            status="error",
            error_message=last_error or "Unknown Gemini request error.",
        )

    def _extract_text(self, response: Any, response_data: dict[str, Any]) -> str:
        text = getattr(response, "text", "") or ""
        if text:
            return str(text).strip()
        candidates = response_data.get("candidates", [])
        if not candidates:
            return ""
        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        texts = [str(part.get("text", "")) for part in parts if part.get("text")]
        return "".join(texts).strip()

    def _parse_usage(self, usage_data: Any) -> UsageStats:
        raw_usage = _normalize_usage_payload(usage_data)
        prompt_tokens = int(_get_usage_value(usage_data, raw_usage, "prompt_token_count"))
        completion_tokens = int(_get_usage_value(usage_data, raw_usage, "candidates_token_count"))
        total_tokens = int(
            _get_usage_value(
                usage_data,
                raw_usage,
                "total_token_count",
                fallback=prompt_tokens + completion_tokens,
            )
        )
        return UsageStats(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )


def _messages_to_gemini_payload(messages: list[Message]) -> tuple[str, list[types.Content]]:
    system_parts: list[str] = []
    contents: list[types.Content] = []
    for message in messages:
        role = str(message.get("role", "user"))
        content = str(message.get("content", ""))
        if role == "system":
            system_parts.append(content)
            continue
        gemini_role = "model" if role == "assistant" else "user"
        contents.append(
            types.Content(
                role=gemini_role,
                parts=[types.Part(text=content)],
            )
        )
    return "\n\n".join(system_parts).strip(), contents


def _extract_finish_reason(response: Any, response_data: dict[str, Any]) -> str:
    candidates_attr = getattr(response, "candidates", None)
    if candidates_attr:
        finish_reason = getattr(candidates_attr[0], "finish_reason", None)
        if finish_reason is not None:
            return str(finish_reason)
    candidates = response_data.get("candidates", [])
    if not candidates:
        return ""
    return str(candidates[0].get("finishReason", ""))


def _normalize_response_payload(response: Any) -> dict[str, Any]:
    if hasattr(response, "model_dump"):
        return dict(response.model_dump())
    if hasattr(response, "to_json_dict"):
        return dict(response.to_json_dict())
    if isinstance(response, dict):
        return dict(response)
    return {}


def _normalize_usage_payload(usage: Any) -> dict[str, Any]:
    if usage is None:
        return {}
    if hasattr(usage, "model_dump"):
        return dict(usage.model_dump())
    if hasattr(usage, "to_json_dict"):
        return dict(usage.to_json_dict())
    if isinstance(usage, dict):
        return dict(usage)
    return {
        key: value
        for key, value in vars(usage).items()
        if not key.startswith("_")
    }


def _get_usage_value(usage: Any, raw_usage: dict[str, Any], field_name: str, fallback: int = 0) -> int:
    if usage is not None:
        value = getattr(usage, field_name, None)
        if value not in (None, ""):
            try:
                return int(value)
            except (TypeError, ValueError):
                pass
    value = raw_usage.get(field_name)
    if value in (None, ""):
        return fallback
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback
