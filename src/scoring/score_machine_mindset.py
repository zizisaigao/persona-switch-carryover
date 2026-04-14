from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer

from src.utils.io import load_samples, write_jsonl
from src.utils.schema import ExperimentSample


MBTI_TYPES = [
    "ENFJ", "ENFP", "ENTJ", "ENTP",
    "ESFJ", "ESFP", "ESTJ", "ESTP",
    "INFJ", "INFP", "INTJ", "INTP",
    "ISFJ", "ISFP", "ISTJ", "ISTP",
]

DIMENSION_TO_INDEX = {
    "energy": 0,
    "information": 1,
    "decision": 2,
    "execution": 3,
}

DIMENSION_CODE_ORDER = {
    "energy": ("E", "I"),
    "information": ("S", "N"),
    "decision": ("T", "F"),
    "execution": ("J", "P"),
}

DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def build_reference_bank(labeled_path: Path) -> dict[str, Any]:
    dataframe = pd.read_parquet(labeled_path)
    self_awareness: dict[str, dict[str, Any]] = {}
    dimension_pole: dict[str, dict[str, Any]] = defaultdict(dict)

    for row in dataframe.to_dict(orient="records"):
        prompt_key = make_prompt_key(str(row.get("instruction", "")), str(row.get("input", "")))
        prompt_text = merge_instruction_input(str(row.get("instruction", "")), str(row.get("input", "")))
        source_group = str(row.get("source_group", ""))

        if source_group == "self_awareness":
            entry = self_awareness.setdefault(
                prompt_key,
                {
                    "instruction": str(row.get("instruction", "")),
                    "input": str(row.get("input", "")),
                    "prompt_text": prompt_text,
                    "references": {},
                },
            )
            mbti_type = str(row.get("mbti_type", ""))
            if mbti_type:
                entry["references"][mbti_type] = str(row.get("output", ""))
            continue

        if source_group == "dimension_pole":
            dimension = str(row.get("mbti_dimension", ""))
            code = str(row.get("mbti_code", ""))
            if not dimension or not code:
                continue
            dimension_entry = dimension_pole[dimension].setdefault(
                prompt_key,
                {
                    "instruction": str(row.get("instruction", "")),
                    "input": str(row.get("input", "")),
                    "prompt_text": prompt_text,
                    "references": {},
                },
            )
            dimension_entry["references"][code] = str(row.get("output", ""))

    return {
        "self_awareness": self_awareness,
        "dimension_pole": dict(dimension_pole),
    }


def build_eval_sets(
    *,
    labeled_path: Path,
    self_awareness_output: Path,
    dimension_output: Path,
    prompt_text: str = "Answer from the current persona's perspective.",
) -> dict[str, int]:
    reference_bank = build_reference_bank(labeled_path)
    self_rows: list[dict[str, Any]] = []
    dimension_rows: list[dict[str, Any]] = []

    for prompt_key, entry in sorted(reference_bank["self_awareness"].items()):
        available_types = sorted(entry["references"].keys())
        if available_types != MBTI_TYPES:
            continue
        self_rows.append(
            _make_unified_row(
                sample_id=f"machine_mindset_self_{short_hash(prompt_key)}",
                source_dataset="machine_mindset_self_awareness_eval",
                prompt_text=prompt_text,
                question_text=entry["prompt_text"],
                metadata={
                    "prompt_key": prompt_key,
                    "source_group": "self_awareness",
                    "available_mbti_types": available_types,
                },
            )
        )

    for dimension, prompt_map in sorted(reference_bank["dimension_pole"].items()):
        expected_codes = sorted(DIMENSION_CODE_ORDER[dimension])
        for prompt_key, entry in sorted(prompt_map.items()):
            available_codes = sorted(entry["references"].keys())
            if available_codes != expected_codes:
                continue
            dimension_rows.append(
                _make_unified_row(
                    sample_id=f"machine_mindset_dim_{dimension}_{short_hash(prompt_key)}",
                    source_dataset="machine_mindset_dimension_eval",
                    prompt_text=prompt_text,
                    question_text=entry["prompt_text"],
                    metadata={
                        "prompt_key": prompt_key,
                        "source_group": "dimension_pole",
                        "mbti_dimension": dimension,
                        "available_mbti_codes": available_codes,
                    },
                )
            )

    write_jsonl(self_awareness_output, self_rows)
    write_jsonl(dimension_output, dimension_rows)
    return {
        "self_awareness": len(self_rows),
        "dimension_pole": len(dimension_rows),
    }


def score_self_awareness_response(
    *,
    response_text: str,
    prompt_key: str,
    target_mbti_type: str,
    reference_bank: dict[str, Any],
    persona_a: str | None = None,
    similarity_model_name: str = DEFAULT_EMBEDDING_MODEL,
    embedding_cache_dir: Path | None = None,
) -> dict[str, Any]:
    entry = reference_bank["self_awareness"][prompt_key]
    references = entry["references"]
    similarities = rank_reference_similarities(
        response_text,
        references,
        embedding_model_name=similarity_model_name,
        embedding_cache_dir=embedding_cache_dir,
    )
    predicted_type = similarities[0]["label"] if similarities else ""
    labels = [item["label"] for item in similarities]
    target_rank = labels.index(target_mbti_type) + 1 if target_mbti_type in labels else None
    score = {
        "source_group": "self_awareness",
        "predicted_type": predicted_type,
        "target_type": target_mbti_type,
        "target_type_match": predicted_type == target_mbti_type,
        "target_type_rank": target_rank,
        "target_type_similarity": similarity_lookup(similarities, target_mbti_type),
        "reference_type_count": len(references),
        "top_similarity_type": predicted_type,
        "similarity_ranking": similarities,
    }
    if persona_a:
        score["persona_a_similarity"] = similarity_lookup(similarities, persona_a)
        score["rai_margin_a_minus_target"] = round(
            score["persona_a_similarity"] - score["target_type_similarity"],
            4,
        )
    return score


def score_dimension_response(
    *,
    response_text: str,
    prompt_key: str,
    dimension: str,
    target_mbti_type: str,
    reference_bank: dict[str, Any],
    persona_a: str | None = None,
    similarity_model_name: str = DEFAULT_EMBEDDING_MODEL,
    embedding_cache_dir: Path | None = None,
) -> dict[str, Any]:
    target_code = mbti_type_to_dimension_code(target_mbti_type, dimension)
    persona_a_code = mbti_type_to_dimension_code(persona_a, dimension) if persona_a else ""
    entry = reference_bank["dimension_pole"][dimension][prompt_key]
    references = entry["references"]
    similarities = rank_reference_similarities(
        response_text,
        references,
        embedding_model_name=similarity_model_name,
        embedding_cache_dir=embedding_cache_dir,
    )
    predicted_code = similarities[0]["label"] if similarities else ""
    score = {
        "source_group": "dimension_pole",
        "mbti_dimension": dimension,
        "predicted_code": predicted_code,
        "target_code": target_code,
        "target_code_match": predicted_code == target_code,
        "target_code_similarity": similarity_lookup(similarities, target_code),
        "reference_code_count": len(references),
        "similarity_ranking": similarities,
    }
    if persona_a_code:
        score["persona_a_code"] = persona_a_code
        score["persona_a_similarity"] = similarity_lookup(similarities, persona_a_code)
        score["rai_margin_a_minus_target"] = round(
            score["persona_a_similarity"] - score["target_code_similarity"],
            4,
        )
    return score


def rank_reference_similarities(
    candidate_text: str,
    references: dict[str, str],
    *,
    embedding_model_name: str = DEFAULT_EMBEDDING_MODEL,
    embedding_cache_dir: Path | None = None,
) -> list[dict[str, Any]]:
    if not references:
        return []
    scorer = _EmbeddingSimilarityScorer(
        model_name=embedding_model_name,
        cache_dir=embedding_cache_dir,
    )
    return scorer.rank(candidate_text, references)


def similarity_lookup(ranking: list[dict[str, Any]], label: str) -> float:
    for item in ranking:
        if item["label"] == label:
            return float(item["similarity"])
    return 0.0


def active_persona_for_condition(condition: str, persona_a: str, persona_b: str) -> str:
    return persona_a if condition in {"A_only", "A_only_strong"} else persona_b


def mbti_type_to_dimension_code(mbti_type: str | None, dimension: str) -> str:
    if not mbti_type:
        return ""
    index = DIMENSION_TO_INDEX[dimension]
    return mbti_type[index]


def make_prompt_key(instruction: str, model_input: str) -> str:
    merged = merge_instruction_input(instruction, model_input)
    normalized = normalize_text(merged)
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()


def merge_instruction_input(instruction: str, model_input: str) -> str:
    instruction_text = instruction.strip()
    input_text = model_input.strip()
    if input_text and input_text not in {"", " ", "None"}:
        return f"{instruction_text}\n\nAdditional input:\n{input_text}"
    return instruction_text


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def load_eval_sample_map(path: Path) -> dict[str, ExperimentSample]:
    return {sample.sample_id: sample for sample in load_samples(path)}


def _make_unified_row(
    *,
    sample_id: str,
    source_dataset: str,
    prompt_text: str,
    question_text: str,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    return {
        "sample_id": sample_id,
        "task_type": "machine_mindset",
        "source_dataset": source_dataset,
        "prompt_text": prompt_text,
        "question_text": question_text,
        "options_json": "",
        "target_label": "",
        "metadata_json": json.dumps(metadata, ensure_ascii=False),
    }


class _EmbeddingSimilarityScorer:
    _instances: dict[tuple[str, str], "_EmbeddingSimilarityScorer"] = {}

    def __new__(cls, *, model_name: str, cache_dir: Path | None) -> "_EmbeddingSimilarityScorer":
        cache_key = (model_name, str(cache_dir or ""))
        instance = cls._instances.get(cache_key)
        if instance is None:
            instance = super().__new__(cls)
            cls._instances[cache_key] = instance
        return instance

    def __init__(self, *, model_name: str, cache_dir: Path | None) -> None:
        if hasattr(self, "_initialized") and self._initialized:
            return
        self.model_name = model_name
        self.cache_dir = cache_dir or (Path(__file__).resolve().parents[2] / "outputs" / "embedding_cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.model_cache_dir = Path(__file__).resolve().parents[2] / "outputs" / "hf_cache"
        self.model_cache_dir.mkdir(parents=True, exist_ok=True)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            cache_dir=str(self.model_cache_dir),
        )
        self.model = AutoModel.from_pretrained(
            model_name,
            cache_dir=str(self.model_cache_dir),
        )
        self.model.to(self.device)
        self.model.eval()
        self._memory_cache: dict[str, list[float]] = {}
        self._initialized = True

    def rank(self, candidate_text: str, references: dict[str, str]) -> list[dict[str, Any]]:
        candidate_embedding = self._embed(candidate_text)
        scored: list[dict[str, Any]] = []
        for label, text in references.items():
            reference_embedding = self._embed(text)
            similarity = float(torch.dot(candidate_embedding, reference_embedding).item())
            scored.append({"label": label, "similarity": round(similarity, 4)})
        scored.sort(key=lambda item: item["similarity"], reverse=True)
        return scored

    def _embed(self, text: str) -> torch.Tensor:
        cache_key = self._text_cache_key(text)
        cached = self._memory_cache.get(cache_key)
        if cached is None:
            cache_path = self.cache_dir / f"{cache_key}.json"
            if cache_path.exists():
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                self._memory_cache[cache_key] = cached
            else:
                embedding = self._compute_embedding(text)
                cached = embedding.tolist()
                cache_path.write_text(json.dumps(cached), encoding="utf-8")
                self._memory_cache[cache_key] = cached
        return torch.tensor(cached, dtype=torch.float32)

    def _compute_embedding(self, text: str) -> torch.Tensor:
        if callable(self.tokenizer):
            encoded = self.tokenizer(
                text,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=256,
            )
        else:
            tokens = self.tokenizer.tokenize(text)
            max_body_length = 254
            if len(tokens) > max_body_length:
                tokens = tokens[:max_body_length]
            tokens = [self.tokenizer.cls_token, *tokens, self.tokenizer.sep_token]
            input_ids = self.tokenizer.convert_tokens_to_ids(tokens)
            attention_mask = [1] * len(input_ids)
            pad_token_id = self.tokenizer.pad_token_id
            if pad_token_id is None:
                pad_token_id = 0
            while len(input_ids) < 256:
                input_ids.append(pad_token_id)
                attention_mask.append(0)
            encoded = {
                "input_ids": torch.tensor([input_ids], dtype=torch.long),
                "attention_mask": torch.tensor([attention_mask], dtype=torch.long),
            }
        encoded = {key: value.to(self.device) for key, value in encoded.items()}
        with torch.no_grad():
            outputs = self.model(**encoded)
        token_embeddings = outputs.last_hidden_state if hasattr(outputs, "last_hidden_state") else outputs[0]
        attention_mask = encoded["attention_mask"].unsqueeze(-1).expand(token_embeddings.size()).float()
        summed = torch.sum(token_embeddings * attention_mask, dim=1)
        counts = torch.clamp(attention_mask.sum(dim=1), min=1e-9)
        mean_pooled = summed / counts
        normalized = torch.nn.functional.normalize(mean_pooled, p=2, dim=1)
        return normalized.squeeze(0).cpu()

    def _text_cache_key(self, text: str) -> str:
        payload = {
            "model_name": self.model_name,
            "text": text,
        }
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
