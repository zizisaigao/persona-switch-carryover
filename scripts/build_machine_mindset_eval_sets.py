from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.scoring.machine_mindset_alignment import build_eval_sets


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build prompt-aligned Machine Mindset evaluation sets from the labeled parquet."
    )
    parser.add_argument(
        "--labeled-dataset",
        type=Path,
        default=Path("data/processed/machine_mindset_labeled.parquet"),
        help="Labeled Machine Mindset parquet created from the raw JSON files.",
    )
    parser.add_argument(
        "--self-awareness-output",
        type=Path,
        default=Path("data/processed/machine_mindset_self_awareness_eval.jsonl"),
        help="Output JSONL for complete-type self-awareness evaluation prompts.",
    )
    parser.add_argument(
        "--dimension-output",
        type=Path,
        default=Path("data/processed/machine_mindset_dimension_eval.jsonl"),
        help="Output JSONL for dimension-pole evaluation prompts.",
    )
    parser.add_argument(
        "--prompt-text",
        default="Answer from the current persona's perspective.",
        help="Prompt prefix used for both eval sets.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    counts = build_eval_sets(
        labeled_path=args.labeled_dataset,
        self_awareness_output=args.self_awareness_output,
        dimension_output=args.dimension_output,
        prompt_text=args.prompt_text,
    )
    print(f"wrote self-awareness eval set -> {args.self_awareness_output} ({counts['self_awareness']} rows)")
    print(f"wrote dimension eval set -> {args.dimension_output} ({counts['dimension_pole']} rows)")


if __name__ == "__main__":
    main()
