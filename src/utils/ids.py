from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4


def timestamp_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_run_id(prefix: str = "run") -> str:
    return f"{prefix}_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid4().hex[:8]}"


def make_trial_id(index: int) -> str:
    return f"trial_{index:03d}"
