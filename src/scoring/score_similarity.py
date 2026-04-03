from __future__ import annotations

import re
from typing import Any


def score_text_similarity(
    reference_text: str,
    candidate_text: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata = metadata or {}
    references = _collect_references(reference_text, metadata)
    candidate_tokens = _tokens(candidate_text)

    best_index = -1
    best_metrics = {
        "reference_overlap_f1": 0.0,
        "reference_precision": 0.0,
        "reference_recall": 0.0,
        "reference_jaccard": 0.0,
    }

    for index, reference in enumerate(references):
        metrics = _pairwise_metrics(_tokens(reference), candidate_tokens)
        if metrics["reference_overlap_f1"] > best_metrics["reference_overlap_f1"]:
            best_metrics = metrics
            best_index = index

    keywords = _collect_keywords(metadata)
    keyword_metrics = _keyword_metrics(keywords, candidate_tokens)

    score = max(best_metrics["reference_overlap_f1"], keyword_metrics["keyword_recall"])
    return {
        "score_type": "machine_mindset",
        "score": round(score, 4),
        "reference_count": len(references),
        "best_reference_index": best_index,
        **best_metrics,
        **keyword_metrics,
    }


def _collect_references(reference_text: str, metadata: dict[str, Any]) -> list[str]:
    references: list[str] = []
    metadata_reference = metadata.get("reference_answer")
    if metadata_reference:
        references.append(str(metadata_reference))

    metadata_references = metadata.get("reference_answers", [])
    if isinstance(metadata_references, list):
        references.extend(str(item) for item in metadata_references if item)
    elif metadata_references:
        references.append(str(metadata_references))

    if not references and reference_text:
        references.append(reference_text)
    return references


def _collect_keywords(metadata: dict[str, Any]) -> list[str]:
    value = metadata.get("expected_keywords", [])
    if isinstance(value, list):
        return [str(item).lower() for item in value if str(item).strip()]
    if value:
        return [str(value).lower()]
    return []


def _pairwise_metrics(reference_tokens: set[str], candidate_tokens: set[str]) -> dict[str, float]:
    if not reference_tokens or not candidate_tokens:
        return {
            "reference_overlap_f1": 0.0,
            "reference_precision": 0.0,
            "reference_recall": 0.0,
            "reference_jaccard": 0.0,
        }

    overlap = len(reference_tokens & candidate_tokens)
    precision = overlap / len(candidate_tokens)
    recall = overlap / len(reference_tokens)
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    jaccard = overlap / len(reference_tokens | candidate_tokens)
    return {
        "reference_overlap_f1": round(f1, 4),
        "reference_precision": round(precision, 4),
        "reference_recall": round(recall, 4),
        "reference_jaccard": round(jaccard, 4),
    }


def _keyword_metrics(keywords: list[str], candidate_tokens: set[str]) -> dict[str, float]:
    if not keywords:
        return {
            "keyword_hits": 0,
            "keyword_total": 0,
            "keyword_recall": 0.0,
        }

    hits = 0
    for keyword in keywords:
        keyword_tokens = _tokens(keyword)
        if keyword_tokens and keyword_tokens.issubset(candidate_tokens):
            hits += 1
    recall = hits / len(keywords)
    return {
        "keyword_hits": hits,
        "keyword_total": len(keywords),
        "keyword_recall": round(recall, 4),
    }


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[A-Za-z0-9']+", text)}
