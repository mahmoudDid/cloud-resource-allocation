"""Configuration YAML loader."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict
import yaml


def load_yaml_config(config_path: str) -> Dict[str, Any]:
    """Load configuration dictionary from YAML file."""
    path = Path(config_path)
    if not path.is_file():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
