from __future__ import annotations

import os
import time
from typing import Any

import requests

from src.models.base_client import BaseClient
from src.models.pricing import estimate_cost_usd
from src.utils.schema import Message, ModelResponse, UsageStats


class OpenRouterClient(BaseClient):
    provider_name = "openrouter"

    def __init__(
        self,
        *,
        api_key_env: str,
        timeout_seconds: int = 60,
        max_retries: int = 3,
    ) -> None:
        self.api_key = os.getenv(api_key_env, "")
        self.base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries

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
                error_message="Missing OpenRouter API key in environment.",
            )

        payload = {
            "model": model_name,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        last_error: str | None = None
        for attempt in range(self.max_retries + 1):
            start = time.perf_counter()
            try:
                response = requests.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=self.timeout_seconds,
                )
                latency = time.perf_counter() - start
                response.raise_for_status()
                data = response.json()
                usage = self._parse_usage(data.get("usage", {}))
                usage.cost_usd = estimate_cost_usd(model_name, usage)
                text = self._extract_text(data)
                return ModelResponse(
                    text=text,
                    usage=usage,
                    raw_response=data,
                    status="success",
                    latency_seconds=round(latency, 4),
                )
            except requests.RequestException as exc:
                last_error = str(exc)
                if attempt >= self.max_retries:
                    break
                time.sleep(2 ** attempt)

        return ModelResponse(
            text="",
            status="error",
            error_message=last_error or "Unknown OpenRouter request error.",
        )

    def _extract_text(self, response_data: dict[str, Any]) -> str:
        choices = response_data.get("choices", [])
        if not choices:
            return ""
        message = choices[0].get("message", {})
        return message.get("content", "")

    def _parse_usage(self, usage_data: dict[str, Any]) -> UsageStats:
        prompt_tokens = int(usage_data.get("prompt_tokens", 0) or 0)
        completion_tokens = int(usage_data.get("completion_tokens", 0) or 0)
        total_tokens = int(usage_data.get("total_tokens", prompt_tokens + completion_tokens) or 0)
        return UsageStats(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )
