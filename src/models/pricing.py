from __future__ import annotations

from src.utils.schema import UsageStats


DEFAULT_PRICING_USD_PER_MILLION: dict[str, dict[str, float]] = {
    "openai/gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "mock/persona-simulator": {"input": 0.0, "output": 0.0},
}


def estimate_cost_usd(model_name: str, usage: UsageStats) -> float:
    pricing = DEFAULT_PRICING_USD_PER_MILLION.get(model_name)
    if not pricing:
        return 0.0
    input_cost = (usage.prompt_tokens / 1_000_000) * pricing["input"]
    output_cost = (usage.completion_tokens / 1_000_000) * pricing["output"]
    return round(input_cost + output_cost, 8)
