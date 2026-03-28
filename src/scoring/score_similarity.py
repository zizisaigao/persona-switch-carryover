from __future__ import annotations

from typing import Any


def score_text_similarity(reference_text: str, candidate_text: str) -> dict[str, Any]:
    reference_tokens = set(reference_text.lower().split())
    candidate_tokens = set(candidate_text.lower().split())
    if not reference_tokens or not candidate_tokens:
        score = 0.0
    else:
        score = len(reference_tokens & candidate_tokens) / len(reference_tokens | candidate_tokens)
    return {
        "score_type": "lexical_jaccard",
        "score": round(score, 4),
    }
