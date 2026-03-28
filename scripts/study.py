#!/usr/bin/env python3
"""
bite-size-study shim — 기존 import 경로 호환을 위한 re-export 모듈.

tests/test_study.py 가 `from scripts.study import ...` 형태로 임포트하므로
모든 공개 이름을 그대로 노출한다. monkeypatch 타겟(DATA_DIR 등)도 유지.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# ── 모듈 변수 (monkeypatch 타겟) ──────────────
from bite_size_study.paths import (
    CARDS_DIR,
    CONFIG_PATH,
    DATA_DIR,
    PROGRESS_PATH,
    ROOT,
    STREAK_PATH,
)

# ── 순수 함수 re-export ──────────────────────
from bite_size_study.core import (  # noqa: F401
    calc_level,
    check_answer,
    load_all_cards,
    parse_card,
    select_today_cards,
    update_streak,
    xp_for_next_level,
)

# ── UI 함수 re-export ────────────────────────
from bite_size_study.session import (  # noqa: F401
    run_session,
    show_card,
    show_progress,
    show_summary,
    show_welcome,
)

from bite_size_study.ui import console  # noqa: F401


# ── 데이터 I/O: 모듈 변수를 참조하도록 래핑 ──
# monkeypatch.setattr("scripts.study.PROGRESS_PATH", ...) 가 동작하려면
# 이 모듈의 변수를 사용해야 한다.
def load_config() -> dict[str, Any]:
    from bite_size_study.paths import load_config as _load
    return _load()


def load_progress() -> dict[str, Any]:
    from bite_size_study.paths import load_progress as _load
    return _load(path=PROGRESS_PATH)


def save_progress(progress: dict[str, Any]) -> None:
    from bite_size_study.paths import save_progress as _save
    _save(progress, path=PROGRESS_PATH)


def load_streak() -> dict[str, Any]:
    from bite_size_study.paths import load_streak as _load
    return _load(path=STREAK_PATH)


def save_streak(streak: dict[str, Any]) -> None:
    from bite_size_study.paths import save_streak as _save
    _save(streak, path=STREAK_PATH)


# ── CLI 진입점 ─────────────────────────────────
def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] == "start":
        run_session()
    elif args[0] == "progress":
        show_progress()
    elif args[0] == "cards":
        cards = load_all_cards()
        studied = load_progress()["cards"]
        console.print(f"\n  총 {len(cards)}장의 카드가 있습니다.\n")
        for card in cards:
            status = "\u2713" if card["id"] in studied else "\u25cb"
            console.print(
                f"  {status} [{card.get('subject', '?')}] {card['title']} ({card['id']})"
            )
    else:
        console.print("[info]사용법: python study.py [start|progress|cards][/]")


if __name__ == "__main__":
    main()
