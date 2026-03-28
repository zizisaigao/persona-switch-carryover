from __future__ import annotations

from abc import ABC, abstractmethod

from src.utils.schema import Message, ModelResponse


class BaseClient(ABC):
    provider_name: str = "base"

    @abstractmethod
    def generate(
        self,
        *,
        messages: list[Message],
        model_name: str,
        temperature: float,
        max_tokens: int,
    ) -> ModelResponse:
        raise NotImplementedError
