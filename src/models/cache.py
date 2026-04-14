from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class RequestCache:
    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._memory_cache: dict[str, dict[str, Any]] = {}

    def build_key(
        self,
        *,
        provider: str,
        model_name: str,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int,
    ) -> str:
        payload = {
            "provider": provider,
            "model_name": model_name,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        raw = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def _path(self, key: str) -> Path:
        return self.cache_dir / f"{key}.json"

    def get(self, key: str) -> dict[str, Any] | None:
        cached = self._memory_cache.get(key)
        if cached is not None:
            return cached
        path = self._path(key)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as handle:
            cached = json.load(handle)
        self._memory_cache[key] = cached
        return cached

    def set(self, key: str, value: dict[str, Any]) -> None:
        self._memory_cache[key] = value
        path = self._path(key)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
