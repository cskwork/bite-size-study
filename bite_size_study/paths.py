"""경로 상수 및 데이터 I/O."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

# ── 경로 설정 ──────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.yaml"
CARDS_DIR = ROOT / "content" / "cards"
DATA_DIR = ROOT / "data"
PROGRESS_PATH = DATA_DIR / "progress.json"
STREAK_PATH = DATA_DIR / "streak.json"


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"config.yaml not found at {CONFIG_PATH}. "
            "Copy config.yaml.example to config.yaml and fill in your settings."
        )
    with open(CONFIG_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"config.yaml must be a YAML mapping, got {type(data)}")
    return data


def load_progress(path: Path | None = None) -> dict[str, Any]:
    p = path or PROGRESS_PATH
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"cards": {}, "total_xp": 0, "level": 1}


def save_progress(progress: dict[str, Any], path: Path | None = None) -> None:
    p = path or PROGRESS_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def load_streak(path: Path | None = None) -> dict[str, Any]:
    p = path or STREAK_PATH
    if p.exists():
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"dates": [], "current_streak": 0, "best_streak": 0}


def save_streak(streak: dict[str, Any], path: Path | None = None) -> None:
    p = path or STREAK_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(streak, f, ensure_ascii=False, indent=2)
