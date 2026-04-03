from __future__ import annotations

import argparse
import json
from pathlib import Path

import requests


DATASETS = {
    "ifeval": {
        "hf_name": "google/IFEval",
        "filename": "ifeval_full.parquet",
    },
    "machine_mindset": {
        "hf_name": "pandalla/Machine_Mindset_MBTI_dataset",
        "filename": "machine_mindset_full.parquet",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download public datasets used by the persona-switch pipeline.")
    parser.add_argument(
        "--dataset",
        choices=["ifeval", "machine_mindset", "all"],
        default="all",
        help="Which dataset to download.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/processed"),
        help="Directory where downloaded parquet files will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_names = list(DATASETS) if args.dataset == "all" else [args.dataset]
    args.output_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, dict[str, str | int]] = {}
    for dataset_name in target_names:
        info = DATASETS[dataset_name]
        parquet_url = resolve_parquet_url(info["hf_name"])
        destination = args.output_dir / info["filename"]
        download_file(parquet_url, destination)
        manifest[dataset_name] = {
            "hf_name": info["hf_name"],
            "parquet_url": parquet_url,
            "local_path": str(destination),
            "size_bytes": destination.stat().st_size,
        }
        print(f"downloaded {dataset_name} -> {destination}")

    manifest_path = args.output_dir / "public_dataset_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote manifest -> {manifest_path}")


def resolve_parquet_url(hf_name: str) -> str:
    response = requests.get(
        "https://datasets-server.huggingface.co/parquet",
        params={"dataset": hf_name},
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    parquet_files = payload.get("parquet_files", [])
    if not parquet_files:
        raise ValueError(f"No parquet files found for dataset: {hf_name}")
    return str(parquet_files[0]["url"])


def download_file(url: str, destination: Path) -> None:
    with requests.get(url, stream=True, timeout=120) as response:
        response.raise_for_status()
        with destination.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    handle.write(chunk)


if __name__ == "__main__":
    main()
