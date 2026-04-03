from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.io import load_samples


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a deterministic sampled JSONL dataset from any supported sample file."
    )
    parser.add_argument("--input-file", type=Path, required=True)
    parser.add_argument("--output-file", type=Path, required=True)
    parser.add_argument("--max-samples", type=int, required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--sample-ids-output",
        type=Path,
        default=None,
        help="Optional newline-delimited sample_id list for reuse across runs.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    samples = load_samples(args.input_file)
    shuffled = list(samples)
    random.Random(args.seed).shuffle(shuffled)
    selected = shuffled[: args.max_samples]

    rows = [
        {
            "sample_id": sample.sample_id,
            "task_type": sample.task_type,
            "source_dataset": sample.source_dataset,
            "prompt_text": sample.prompt_text,
            "question_text": sample.question_text,
            "options_json": sample.options_json,
            "target_label": sample.target_label,
            "metadata_json": sample.metadata_json,
        }
        for sample in selected
    ]

    args.output_file.parent.mkdir(parents=True, exist_ok=True)
    with args.output_file.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    if args.sample_ids_output is not None:
        args.sample_ids_output.parent.mkdir(parents=True, exist_ok=True)
        with args.sample_ids_output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["sample_id"])
            for sample in selected:
                writer.writerow([sample.sample_id])

    print(f"sampled {len(selected)} of {len(samples)} -> {args.output_file}")
    if args.sample_ids_output is not None:
        print(f"wrote sample ids -> {args.sample_ids_output}")


if __name__ == "__main__":
    main()
