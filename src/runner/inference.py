from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

from src.models.base_client import BaseClient
from src.models.cache import RequestCache
from src.utils.ids import timestamp_utc
from src.utils.io import append_jsonl
from src.utils.schema import Message, ModelResponse, UsageStats


def generate_with_cache(
    *,
    client: BaseClient,
    cache: RequestCache | None,
    usage_log_path: Path,
    provider: str,
    model_name: str,
    messages: list[Message],
    temperature: float,
    max_tokens: int,
    log_context: dict[str, str],
) -> ModelResponse:
    cache_key = None
    if cache is not None:
        cache_key = cache.build_key(
            provider=provider,
            model_name=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        cached = cache.get(cache_key)
        if cached is not None:
            usage = UsageStats(**cached.get("usage", {}))
            return ModelResponse(
                text=cached.get("text", ""),
                usage=usage,
                raw_response=cached.get("raw_response", {}),
                status=cached.get("status", "success"),
                error_message=cached.get("error_message"),
                cache_hit=True,
                latency_seconds=cached.get("latency_seconds"),
            )

    response = client.generate(
        messages=messages,
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    _log_usage(usage_log_path=usage_log_path, response=response, model_name=model_name, log_context=log_context)

    if cache is not None and cache_key is not None and response.status == "success":
        cache.set(
            cache_key,
            {
                "text": response.text,
                "usage": asdict(response.usage),
                "raw_response": response.raw_response,
                "status": response.status,
                "error_message": response.error_message,
                "latency_seconds": response.latency_seconds,
            },
        )
    return response


def _log_usage(
    *,
    usage_log_path: Path,
    response: ModelResponse,
    model_name: str,
    log_context: dict[str, str],
) -> None:
    record = {
        "timestamp": timestamp_utc(),
        "model_name": model_name,
        "status": response.status,
        "cache_hit": response.cache_hit,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
        "cost_usd": response.usage.cost_usd,
        "error_message": response.error_message,
    }
    record.update(log_context)
    append_jsonl(usage_log_path, record)
