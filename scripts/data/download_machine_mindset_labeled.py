from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd
import requests


HF_DATASET_API = "https://huggingface.co/api/datasets/pandalla/Machine_Mindset_MBTI_dataset"
HF_RESOLVE_PREFIX = "https://huggingface.co/datasets/pandalla/Machine_Mindset_MBTI_dataset/resolve/main/"

DIMENSION_CODE_MAP = {
    ("energy", "extraversion"): "E",
    ("energy", "introversion"): "I",
    ("information", "sensing"): "S",
    ("information", "intuition"): "N",
    ("decision", "thinking"): "T",
    ("decision", "feeling"): "F",
    ("execution", "judging"): "J",
    ("execution", "perceiving"): "P",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Machine Mindset raw JSON files and build a labeled parquet dataset."
    )
    parser.add_argument(
        "--languages",
        nargs="+",
        default=["en"],
        choices=["en", "zh"],
        help="Languages to include from the Hugging Face dataset repo.",
    )
    parser.add_argument(
        "--include-self-awareness",
        action="store_true",
        help="Include per-type self-awareness files such as en_ENFJ_self_awareness.json.",
    )
    parser.add_argument(
        "--include-dimension-files",
        action="store_true",
        help="Include dimension-pole files such as en_energy_extraversion.json.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=Path("data/processed/machine_mindset_labeled.parquet"),
        help="Where to write the reconstructed labeled parquet file.",
    )
    parser.add_argument(
        "--manifest-file",
        type=Path,
        default=Path("data/processed/machine_mindset_labeled_manifest.json"),
        help="Where to write the download/build manifest.",
    )
    args = parser.parse_args()
    if not args.include_self_awareness and not args.include_dimension_files:
        args.include_self_awareness = True
        args.include_dimension_files = True
    return args


def main() -> None:
    args = parse_args()
    siblings = fetch_siblings()
    selected_files = [
        sibling
        for sibling in siblings
        if _should_include_file(
            sibling=sibling,
            languages=set(args.languages),
            include_self_awareness=args.include_self_awareness,
            include_dimension_files=args.include_dimension_files,
        )
    ]
    if not selected_files:
        raise SystemExit("No matching Machine Mindset files found for the requested filters.")

    rows: list[dict[str, Any]] = []
    file_summaries: list[dict[str, Any]] = []
    for sibling in selected_files:
        filename = sibling["rfilename"]
        file_rows = fetch_json_rows(filename)
        enriched_rows = _annotate_rows(filename, file_rows)
        rows.extend(enriched_rows)
        file_summaries.append(
            {
                "filename": filename,
                "row_count": len(enriched_rows),
            }
        )
        print(f"loaded {filename} -> {len(enriched_rows)} rows")

    dataframe = pd.DataFrame(rows)
    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_parquet(args.output_file, index=False)

    manifest = {
        "source_dataset": "pandalla/Machine_Mindset_MBTI_dataset",
        "languages": list(args.languages),
        "include_self_awareness": args.include_self_awareness,
        "include_dimension_files": args.include_dimension_files,
        "file_count": len(selected_files),
        "row_count": len(dataframe),
        "output_file": str(args.output_file),
        "files": file_summaries,
    }
    args.manifest_file.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"wrote labeled parquet -> {args.output_file}")
    print(f"wrote manifest -> {args.manifest_file}")


def fetch_siblings() -> list[dict[str, Any]]:
    response = requests.get(HF_DATASET_API, timeout=30)
    response.raise_for_status()
    payload = response.json()
    siblings = payload.get("siblings", [])
    return [item for item in siblings if item.get("rfilename", "").endswith(".json")]


def fetch_json_rows(filename: str) -> list[dict[str, Any]]:
    response = requests.get(f"{HF_RESOLVE_PREFIX}{filename}?download=true", timeout=120)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError(f"Unexpected payload for {filename}: expected list, got {type(payload).__name__}")
    return [row for row in payload if isinstance(row, dict)]


def _should_include_file(
    *,
    sibling: dict[str, Any],
    languages: set[str],
    include_self_awareness: bool,
    include_dimension_files: bool,
) -> bool:
    filename = sibling.get("rfilename", "")
    stem = Path(filename).stem
    parts = stem.split("_")
    if len(parts) < 3:
        return False
    if parts[0] not in languages:
        return False
    if parts[-2:] == ["self", "awareness"]:
        return include_self_awareness
    return include_dimension_files


def _annotate_rows(filename: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    stem = Path(filename).stem
    parts = stem.split("_")
    language = parts[0]

    is_self_awareness = parts[-2:] == ["self", "awareness"]
    mbti_type = ""
    mbti_dimension = ""
    mbti_pole = ""
    mbti_code = ""
    source_group = "self_awareness" if is_self_awareness else "dimension_pole"

    if is_self_awareness:
        if len(parts) < 4:
            raise ValueError(f"Unexpected self-awareness filename: {filename}")
        mbti_type = parts[1]
    else:
        if len(parts) != 3:
            raise ValueError(f"Unexpected dimension filename: {filename}")
        mbti_dimension = parts[1]
        mbti_pole = parts[2]
        mbti_code = DIMENSION_CODE_MAP.get((mbti_dimension, mbti_pole), "")

    annotated_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        annotated_rows.append(
            {
                "sample_id": _make_sample_id(language, source_group, mbti_type, mbti_dimension, mbti_pole, index),
                "instruction": str(row.get("instruction", "")),
                "input": str(row.get("input", "")),
                "output": str(row.get("output", "")),
                "language": language,
                "source_file": filename,
                "source_group": source_group,
                "mbti_type": mbti_type,
                "mbti_dimension": mbti_dimension,
                "mbti_pole": mbti_pole,
                "mbti_code": mbti_code,
            }
        )
    return annotated_rows


def _make_sample_id(
    language: str,
    source_group: str,
    mbti_type: str,
    mbti_dimension: str,
    mbti_pole: str,
    index: int,
) -> str:
    parts = ["machine_mindset", language, source_group]
    if mbti_type:
        parts.append(mbti_type)
    if mbti_dimension:
        parts.append(mbti_dimension)
    if mbti_pole:
        parts.append(mbti_pole)
    parts.append(f"{index:05d}")
    return "_".join(parts)


if __name__ == "__main__":
    main()
