from __future__ import annotations

from pathlib import Path
from typing import Any

from dotenv import load_dotenv
import yaml


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data


def load_all_configs(root: Path | None = None) -> dict[str, Any]:
    project_root = root or get_project_root()
    load_dotenv(project_root / ".env", override=False)
    return {
        "models": load_yaml(project_root / "configs" / "models.yaml"),
        "personas": load_yaml(project_root / "configs" / "personas.yaml"),
        "experiments": load_yaml(project_root / "configs" / "experiments.yaml"),
        "tasks": load_yaml(project_root / "configs" / "tasks.yaml"),
    }
