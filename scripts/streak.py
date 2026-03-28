#!/usr/bin/env python3
"""
스트릭 추적 + 캘린더 시각화

뇌과학 원리: 가시적 진행 기록이 동기를 3.6배 높인다.
GitHub 잔디처럼 "깨기 아까운" 연속 기록이 행동 유지의 핵심.
"""

from __future__ import annotations

import json
from calendar import monthrange
from datetime import date, timedelta
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

ROOT = Path(__file__).resolve().parent.parent
STREAK_PATH = ROOT / "data" / "streak.json"
PROGRESS_PATH = ROOT / "data" / "progress.json"

console = Console()


def load_streak() -> dict:
    if STREAK_PATH.exists():
        with open(STREAK_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"dates": [], "current_streak": 0, "best_streak": 0}


def load_progress() -> dict:
    if PROGRESS_PATH.exists():
        with open(PROGRESS_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"cards": {}, "total_xp": 0, "level": 1}


def show_calendar(target_year: int | None = None, target_month: int | None = None) -> None:
    """월간 학습 캘린더를 표시한다. GitHub 잔디 스타일."""
    streak = load_streak()
    dates_set = set(streak["dates"])

    today = date.today()
    year = target_year or today.year
    month = target_month or today.month

    _, days_in_month = monthrange(year, month)
    first_day = date(year, month, 1)
    weekday_offset = first_day.weekday()  # 0=월요일

    # 요일 헤더
    days_header = " 월  화  수  목  금  토  일"

    # 캘린더 그리드 생성
    lines: list[Text] = []
    current_line = Text()
    current_line.append("  " * weekday_offset)

    for day_num in range(1, days_in_month + 1):
        current_date = date(year, month, day_num)
        date_str = current_date.isoformat()
        weekday = current_date.weekday()

        if date_str in dates_set:
            if current_date == today:
                current_line.append(f" {day_num:2d} ", style="bold green on dark_green")
            else:
                current_line.append(f" {day_num:2d} ", style="green")
        elif current_date == today:
            current_line.append(f" {day_num:2d} ", style="bold yellow")
        elif current_date > today:
            current_line.append(f" {day_num:2d} ", style="dim")
        else:
            current_line.append(f" {day_num:2d} ", style="white")

        if weekday == 6:  # 일요일 = 줄바꿈
            lines.append(current_line)
            current_line = Text()

    if len(current_line) > 0:
        lines.append(current_line)

    # 이번 달 학습일 수
    month_dates = [
        d for d in streak["dates"]
        if d.startswith(f"{year}-{month:02d}")
    ]

    cal_text = Text()
    cal_text.append(f"  {days_header}\n", style="bold cyan")
    for line in lines:
        cal_text.append("  ")
        cal_text.append_text(line)
        cal_text.append("\n")

    title = f"{year}년 {month}월 학습 캘린더"
    subtitle = f"학습일: {len(month_dates)}일 | ■ 학습 완료"

    console.print()
    console.print(Panel(cal_text, title=f"[bold]{title}[/]", subtitle=subtitle, border_style="green"))


def show_streak_stats() -> None:
    """스트릭 통계를 표시한다."""
    streak = load_streak()
    progress = load_progress()

    current = streak["current_streak"]
    best = streak["best_streak"]
    total_days = len(streak["dates"])
    total_xp = progress.get("total_xp", 0)
    total_cards = len(progress.get("cards", {}))

    # 스트릭 바 (최대 30일 표시)
    bar_length = min(current, 30)
    streak_bar = "🟩" * bar_length + "⬜" * (30 - bar_length)

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("항목", style="cyan")
    table.add_column("값", style="bold")

    fire = " 🔥" if current >= 3 else ""
    table.add_row("현재 스트릭", f"{current}일{fire}")
    table.add_row("최장 스트릭", f"{best}일")
    table.add_row("총 학습일", f"{total_days}일")
    table.add_row("학습한 카드", f"{total_cards}장")
    table.add_row("누적 XP", f"{total_xp} XP")

    console.print()
    console.print(Panel(
        f"  {streak_bar}\n  [dim]{current}/30일 목표[/]",
        title="[bold]스트릭 진행[/]",
        border_style="yellow",
    ))
    console.print(table)


def show_weekly_heatmap() -> None:
    """최근 7주 히트맵을 표시한다. GitHub 잔디 스타일."""
    streak = load_streak()
    dates_set = set(streak["dates"])
    today = date.today()

    # 최근 49일 (7주)
    heatmap = Text()
    heatmap.append("  ")
    for week in range(6, -1, -1):
        for weekday in range(7):
            target = today - timedelta(days=week * 7 + (6 - weekday))
            if target.isoformat() in dates_set:
                heatmap.append("■ ", style="green")
            elif target <= today:
                heatmap.append("□ ", style="dim")
            else:
                heatmap.append("  ")
        heatmap.append("\n  ")

    console.print()
    console.print(Panel(heatmap, title="[bold]최근 7주[/]", subtitle="■ 학습 완료 □ 미학습", border_style="cyan"))


def main() -> None:
    import sys

    args = sys.argv[1:]
    command = args[0] if args else "all"

    if command == "calendar":
        show_calendar()
    elif command == "stats":
        show_streak_stats()
    elif command == "heatmap":
        show_weekly_heatmap()
    else:
        show_streak_stats()
        show_calendar()
        show_weekly_heatmap()


if __name__ == "__main__":
    main()
