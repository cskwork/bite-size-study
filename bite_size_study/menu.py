"""인터랙티브 화살표 키 메뉴."""

from __future__ import annotations

import sys
from typing import Callable

from rich.panel import Panel
from rich.text import Text

from bite_size_study.core import calc_level, xp_for_next_level
from bite_size_study.paths import load_progress, load_streak
from bite_size_study.ui import console


# ── 메뉴 항목 정의 ────────────────────────────
MenuItem = tuple[str, str, Callable[[], None]]  # (label, description, action)

QUIT_LABEL = "종료"


def _read_key() -> str:
    """단일 키 입력을 읽는다. 화살표 키는 'up'/'down', Enter는 'enter'."""
    import os
    import select
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = os.read(fd, 1).decode("utf-8", errors="replace")
        if ch == "\x1b":
            if select.select([fd], [], [], 0.05)[0]:
                ch2 = os.read(fd, 1).decode("utf-8", errors="replace")
                if select.select([fd], [], [], 0.05)[0]:
                    ch3 = os.read(fd, 1).decode("utf-8", errors="replace")
                    if ch2 == "[":
                        if ch3 == "A":
                            return "up"
                        if ch3 == "B":
                            return "down"
            return "escape"
        if ch in ("\r", "\n"):
            return "enter"
        if ch == "q":
            return "quit"
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def _render_menu(items: list[MenuItem], selected: int) -> Text:
    """메뉴를 렌더링한다. 선택된 항목을 하이라이트."""
    text = Text()
    for i, (label, desc, _) in enumerate(items):
        if i == selected:
            text.append(f"  ▸ {label}", style="bold green")
            text.append(f"  {desc}\n", style="green")
        else:
            text.append(f"    {label}", style="bold")
            text.append(f"  {desc}\n")
    return text


def _show_status_bar() -> None:
    progress = load_progress()
    streak = load_streak()
    level = calc_level(progress["total_xp"])
    current_xp, next_xp = xp_for_next_level(progress["total_xp"])
    current_streak = streak["current_streak"]
    fire = " 🔥" if current_streak >= 3 else ""

    status = (
        f"  Lv.{level} ({current_xp}/{next_xp} XP)  |  "
        f"스트릭: {current_streak}일{fire}  |  "
        f"카드: {len(progress['cards'])}장 학습"
    )
    console.print(f"\n  {status}")


def run_interactive_menu() -> None:
    from bite_size_study.session import run_session, show_progress
    from bite_size_study.streak import (
        show_calendar,
        show_streak_stats,
        show_weekly_heatmap,
    )

    def list_cards() -> None:
        from bite_size_study.core import load_all_cards
        from bite_size_study.paths import load_progress as _lp

        cards = load_all_cards()
        studied = _lp()["cards"]
        console.print(f"\n  총 {len(cards)}장의 카드가 있습니다.\n")
        for card in cards:
            mark = "✓" if card["id"] in studied else "○"
            console.print(
                f"  {mark} [{card.get('subject', '?')}] {card['title']} ({card['id']})"
            )

    items: list[MenuItem] = [
        ("학습 시작", "오늘의 카드 학습 세션", run_session),
        ("학습 현황", "과목별 진행률 확인", show_progress),
        ("카드 목록", "전체 카드 확인", list_cards),
        ("스트릭 통계", "XP, 스트릭, 학습일 통계", show_streak_stats),
        ("학습 캘린더", "월간 학습 캘린더", show_calendar),
        ("히트맵", "최근 7주 학습 히트맵", show_weekly_heatmap),
        (QUIT_LABEL, "프로그램 종료", lambda: None),
    ]

    if not sys.stdin.isatty():
        _run_numbered_menu(items)
        return

    _run_arrow_menu(items)


def _run_arrow_menu(items: list[MenuItem]) -> None:
    selected = 0

    while True:
        console.clear()
        _show_status_bar()

        menu_text = _render_menu(items, selected)
        console.print()
        console.print(Panel(
            menu_text,
            title="[bold]bite-size-study[/]",
            subtitle="[↑↓] 이동  [Enter] 선택  [q] 종료",
            border_style="green",
        ))

        key = _read_key()
        if key == "up":
            selected = (selected - 1) % len(items)
        elif key == "down":
            selected = (selected + 1) % len(items)
        elif key == "enter":
            label, _, action = items[selected]
            if label == QUIT_LABEL:
                console.print("\n  [dim]다음에 만나요! 👋[/]\n")
                break
            console.clear()
            action()
            console.print("\n  [dim]Enter를 누르면 메뉴로 돌아갑니다...[/]")
            _read_key()
        elif key == "quit":
            console.print("\n  [dim]다음에 만나요! 👋[/]\n")
            break


def _run_numbered_menu(items: list[MenuItem]) -> None:
    from rich.prompt import Prompt

    _show_status_bar()
    console.print()

    for i, (label, desc, _) in enumerate(items, 1):
        console.print(f"  [{i}] {label} — {desc}")

    console.print()
    choice = Prompt.ask(
        "  번호 선택",
        choices=[str(i) for i in range(1, len(items) + 1)],
        default="1",
    )

    idx = int(choice) - 1
    label, _, action = items[idx]
    if label != QUIT_LABEL:
        action()
