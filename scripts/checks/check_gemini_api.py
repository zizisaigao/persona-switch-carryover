from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from google import genai


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Gemini API key with the google-genai SDK.",
    )
    parser.add_argument(
        "--api-key-env",
        type=str,
        default="GEMINI_API_KEY",
        help="Environment variable that stores the Gemini API key.",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default="gemini-2.5-flash-lite",
        help="Gemini model name to test.",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="Reply with exactly: GEMINI_API_OK",
        help="Short prompt used for the validation request.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Temperature used for the validation request.",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=32,
        help="Maximum output tokens for the validation request.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the result as JSON.",
    )
    return parser.parse_args()


def main() -> int:
    _load_local_dotenv_if_available()
    args = parse_args()

    api_key = os.getenv(args.api_key_env, "").strip()
    if not api_key:
        return _emit(
            ok=False,
            result={
                "ok": False,
                "error_type": "missing_api_key",
                "message": f"Environment variable {args.api_key_env} is empty or not set.",
            },
            as_json=args.json,
        )

    start = time.perf_counter()
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=args.model_name,
            contents=args.prompt,
            config={
                "temperature": args.temperature,
                "max_output_tokens": args.max_output_tokens,
            },
        )
        latency_seconds = round(time.perf_counter() - start, 4)
    except Exception as exc:  # pragma: no cover - runtime validation path
        latency_seconds = round(time.perf_counter() - start, 4)
        return _emit(
            ok=False,
            result={
                "ok": False,
                "error_type": type(exc).__name__,
                "message": str(exc),
                "model_name": args.model_name,
                "latency_seconds": latency_seconds,
            },
            as_json=args.json,
        )

    prompt_tokens, completion_tokens, total_tokens, usage_payload = _extract_usage(response)
    cost_usd = _estimate_cost_usd(
        model_name=args.model_name,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
    )

    result = {
        "ok": True,
        "model_name": args.model_name,
        "response_text": getattr(response, "text", "") or "",
        "latency_seconds": latency_seconds,
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "cost_usd_estimate": cost_usd,
            "raw_usage": usage_payload,
        },
    }
    return _emit(ok=True, result=result, as_json=args.json)


def _load_local_dotenv_if_available() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    dotenv_path = repo_root / ".env"
    if not dotenv_path.exists():
        return
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv(dotenv_path, override=False)


def _extract_usage(response: Any) -> tuple[int, int, int, dict[str, Any]]:
    usage = getattr(response, "usage_metadata", None)
    if usage is None:
        return 0, 0, 0, {}

    raw_usage = _normalize_usage_payload(usage)
    prompt_tokens = int(_get_usage_value(usage, raw_usage, "prompt_token_count"))
    completion_tokens = int(_get_usage_value(usage, raw_usage, "candidates_token_count"))
    total_tokens = int(
        _get_usage_value(
            usage,
            raw_usage,
            "total_token_count",
            fallback=prompt_tokens + completion_tokens,
        )
    )
    return prompt_tokens, completion_tokens, total_tokens, raw_usage


def _normalize_usage_payload(usage: Any) -> dict[str, Any]:
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
    value = getattr(usage, field_name, None)
    if value is None:
        value = raw_usage.get(field_name)
    if value in (None, ""):
        return fallback
    try:
        return int(value)
    except (TypeError, ValueError):
        return fallback


def _estimate_cost_usd(model_name: str, prompt_tokens: int, completion_tokens: int) -> float:
    pricing = {
        "gemini-2.5-flash-lite": {"input": 0.10, "output": 0.40},
    }.get(model_name)
    if not pricing:
        return 0.0
    input_cost = (prompt_tokens / 1_000_000) * pricing["input"]
    output_cost = (completion_tokens / 1_000_000) * pricing["output"]
    return round(input_cost + output_cost, 8)


def _emit(*, ok: bool, result: dict[str, Any], as_json: bool) -> int:
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"ok={result.get('ok')}")
        if result.get("model_name"):
            print(f"model_name={result['model_name']}")
        if result.get("latency_seconds") is not None:
            print(f"latency_seconds={result['latency_seconds']}")
        if result.get("response_text"):
            print(f"response_text={result['response_text']}")
        usage = result.get("usage")
        if usage:
            print(
                "usage="
                + json.dumps(usage, ensure_ascii=False)
            )
        if result.get("error_type"):
            print(f"error_type={result['error_type']}")
        if result.get("message"):
            print(f"message={result['message']}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
