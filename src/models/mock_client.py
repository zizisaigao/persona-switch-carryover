from __future__ import annotations

import hashlib
import re
from typing import Iterable

from src.models.base_client import BaseClient
from src.models.pricing import estimate_cost_usd
from src.utils.schema import Message, ModelResponse, UsageStats


PERSONA_STYLES = {
    "INTJ": "Strategic view:",
    "ESFP": "Energetic take:",
    "INFJ": "Reflective perspective:",
    "ENTP": "Alternative angle:",
    "NEUTRAL": "Direct answer:",
}


class MockClient(BaseClient):
    provider_name = "mock"

    def generate(
        self,
        *,
        messages: list[Message],
        model_name: str,
        temperature: float,
        max_tokens: int,
    ) -> ModelResponse:
        system_text = next((msg["content"] for msg in messages if msg["role"] == "system"), "")
        latest_user = next((msg["content"] for msg in reversed(messages) if msg["role"] == "user"), "")
        persona = self._extract_persona(system_text)
        response_text = self._build_response(persona=persona, latest_user=latest_user, all_messages=messages)
        usage = self._estimate_usage(messages, response_text)
        usage.cost_usd = estimate_cost_usd(model_name, usage)
        return ModelResponse(
            text=response_text,
            usage=usage,
            raw_response={"mock": True, "persona": persona},
        )

    def _extract_persona(self, system_text: str) -> str:
        match = re.search(r"Persona:\s*([A-Z]+)", system_text)
        if match:
            return match.group(1)
        return "NEUTRAL"

    def _build_response(self, *, persona: str, latest_user: str, all_messages: Iterable[Message]) -> str:
        prefix = PERSONA_STYLES.get(persona, PERSONA_STYLES["NEUTRAL"])
        if "exactly two bullet points" in latest_user.lower():
            return (
                "- Clarify the goal, likely friction points, and the outcome you need.\n"
                "- Rehearse two concrete examples so the conversation stays specific."
            )
        option_labels = re.findall(r"^([A-Z])\.\s", latest_user, flags=re.MULTILINE)
        if option_labels:
            chosen = option_labels[self._stable_index(persona + latest_user, len(option_labels))]
            return f"{chosen}. {prefix} I would anchor on this option because it best matches the current framing."
        condensed = latest_user.replace("\n", " ").strip()
        return f"{prefix} {condensed[:180]} This reply is generated in mock mode for pipeline validation."

    def _estimate_usage(self, messages: list[Message], response_text: str) -> UsageStats:
        prompt_tokens = sum(len(message["content"].split()) for message in messages)
        completion_tokens = len(response_text.split())
        return UsageStats(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
        )

    def _stable_index(self, text: str, size: int) -> int:
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % max(size, 1)
