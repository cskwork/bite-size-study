#!/usr/bin/env python3
"""
bite-size-study: 뇌과학 기반 정보처리실기 학습 CLI

핵심 원리:
- 마이크로 습관: 카드 2-3장으로 시작 (5분 규칙)
- 자이가르닉 효과: 시작하면 자연스레 지속
- 도파민 설계: 스트릭 + 레벨 + 시각적 보상
- 정체성 전환: 세션 시작 시 정체성 메시지
"""

from __future__ import annotations

import json
import random
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

# ── 경로 설정 ──────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.yaml"
CARDS_DIR = ROOT / "content" / "cards"
DATA_DIR = ROOT / "data"
PROGRESS_PATH = DATA_DIR / "progress.json"
STREAK_PATH = DATA_DIR / "streak.json"

# ── 테마 ───────────────────────────────────────
theme = Theme({
    "info": "cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "danger": "bold red",
    "highlight": "bold magenta",
})
console = Console(theme=theme)


# ── 데이터 로드/저장 ──────────────────────────────
def load_config() -> dict[str, Any]:
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_progress() -> dict[str, Any]:
    if PROGRESS_PATH.exists():
        with open(PROGRESS_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"cards": {}, "total_xp": 0, "level": 1}


def save_progress(progress: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def load_streak() -> dict[str, Any]:
    if STREAK_PATH.exists():
        with open(STREAK_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"dates": [], "current_streak": 0, "best_streak": 0}


def save_streak(streak: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(STREAK_PATH, "w", encoding="utf-8") as f:
        json.dump(streak, f, ensure_ascii=False, indent=2)


# ── 카드 파싱 ──────────────────────────────────
def parse_card(card_path: Path) -> dict[str, Any] | None:
    """YAML frontmatter + Markdown 본문을 파싱한다."""
    text = card_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None

    meta = yaml.safe_load(parts[1])
    body = parts[2].strip()
    return {**meta, "body": body, "path": str(card_path)}


def load_all_cards() -> list[dict[str, Any]]:
    """모든 학습 카드를 로드한다."""
    cards = []
    for md_file in sorted(CARDS_DIR.rglob("*.md")):
        card = parse_card(md_file)
        if card:
            cards.append(card)
    return cards


# ── 카드 선택 로직 ─────────────────────────────
def select_today_cards(
    cards: list[dict[str, Any]],
    progress: dict[str, Any],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    """오늘 학습할 카드를 선택한다. 새 카드 우선, 복습 카드 추가."""
    daily_new = config["session"]["daily_cards"]
    max_review = config["session"]["max_review_cards"]

    # 새 카드: 아직 학습하지 않은 카드
    new_cards = [c for c in cards if c["id"] not in progress["cards"]]
    # 복습 카드: 이해도가 낮은 카드 (3 이하)
    review_cards = [
        c for c in cards
        if c["id"] in progress["cards"]
        and progress["cards"][c["id"]].get("understanding", 0) <= 3
    ]

    selected_new = new_cards[:daily_new]
    selected_review = review_cards[:max_review]
    return selected_new + selected_review


# ── XP / 레벨 시스템 ──────────────────────────
def calc_level(xp: int) -> int:
    """XP 기반 레벨 계산. 레벨업에 필요한 XP가 점진적으로 증가."""
    level = 1
    required = 30  # 레벨 2에 필요한 XP
    while xp >= required:
        xp -= required
        level += 1
        required = int(required * 1.3)
    return level


def xp_for_next_level(total_xp: int) -> tuple[int, int]:
    """(현재 레벨 내 XP, 다음 레벨까지 필요 XP) 반환."""
    remaining = total_xp
    required = 30
    while remaining >= required:
        remaining -= required
        required = int(required * 1.3)
    return remaining, required


# ── 스트릭 업데이트 ────────────────────────────
def update_streak(streak: dict[str, Any]) -> dict[str, Any]:
    """오늘 날짜를 기록하고 스트릭을 업데이트한다."""
    today = date.today().isoformat()
    yesterday = date.today().toordinal() - 1

    if today in streak["dates"]:
        return streak  # 이미 오늘 기록됨

    dates_set = set(streak["dates"])
    yesterday_str = date.fromordinal(yesterday).isoformat()

    new_streak = dict(streak)
    new_dates = streak["dates"] + [today]
    new_streak["dates"] = new_dates

    if yesterday_str in dates_set:
        new_streak["current_streak"] = streak["current_streak"] + 1
    else:
        new_streak["current_streak"] = 1

    new_streak["best_streak"] = max(
        new_streak["best_streak"], new_streak["current_streak"]
    )
    return new_streak


# ── UI 렌더링 ──────────────────────────────────
def show_welcome(config: dict[str, Any], streak: dict[str, Any], progress: dict[str, Any]) -> None:
    """세션 시작 화면을 표시한다."""
    identity = config["identity"]["message"]
    goal = config["identity"]["exam_goal"]
    current_streak = streak["current_streak"]
    level = calc_level(progress["total_xp"])
    current_xp, next_xp = xp_for_next_level(progress["total_xp"])

    # 시간대별 인사
    hour = datetime.now().hour
    if hour < 12:
        greeting = "좋은 아침!"
    elif hour < 18:
        greeting = "좋은 오후!"
    else:
        greeting = "좋은 저녁!"

    # 스트릭 이모지
    streak_display = f"{current_streak}일" if current_streak > 0 else "오늘 시작!"
    fire = " [danger]🔥[/]" if current_streak >= 3 else ""

    welcome_text = Text()
    welcome_text.append(f"  {greeting}\n", style="bold")
    welcome_text.append(f"  스트릭: {streak_display}{fire}\n")
    welcome_text.append(f"  레벨: Lv.{level} ({current_xp}/{next_xp} XP)\n")
    welcome_text.append(f"  목표: {goal}\n\n", style="info")
    welcome_text.append(f'  "{identity}"', style="highlight")

    console.print()
    console.print(Panel(welcome_text, title="[bold]bite-size-study[/]", border_style="cyan"))

    # If-Then 앵커 리마인더
    anchors = config.get("anchors", [])
    if anchors:
        anchor = random.choice(anchors)
        console.print(
            f"\n  [dim]오늘의 앵커: {anchor['trigger']} → {anchor['action']}[/]"
        )


def show_card(card: dict[str, Any], index: int, total: int) -> None:
    """학습 카드를 표시한다."""
    subject_names = {
        "SE": "소프트웨어 설계",
        "PG": "소프트웨어 개발",
        "DB": "데이터베이스 구축",
        "NW": "시스템 통합",
        "MT": "소프트웨어 유지보수",
    }
    subject = subject_names.get(card.get("subject", ""), card.get("subject", ""))
    difficulty_labels = {1: "기초", 2: "응용", 3: "기출심화"}
    diff_label = difficulty_labels.get(card.get("difficulty", 1), "기초")

    header = f"[{index}/{total}] {subject} | {diff_label}"
    console.print()
    console.print(Panel(
        Markdown(card["body"]),
        title=f"[bold]{header}[/]",
        subtitle=f"[dim]{card['id']}[/]",
        border_style="green",
        padding=(1, 2),
    ))


def check_answer(quiz_type: str, user_answer: str, correct_answer: str) -> bool:
    """퀴즈 정답을 판정한다. 양방향 부분 매칭 지원."""
    if quiz_type == "ox":
        return user_answer.upper() == correct_answer.upper()
    # choice, blank: 양방향 부분 매칭 (핵심 키워드만 입력해도 정답)
    user_lower = user_answer.lower().strip()
    answer_lower = correct_answer.lower().strip()
    return user_lower in answer_lower or answer_lower in user_lower


def run_quiz(card: dict[str, Any]) -> bool:
    """카드의 퀴즈를 실행한다. 정답 여부를 반환."""
    quiz = card.get("quiz", {})
    if not quiz or not quiz.get("question"):
        return True  # 퀴즈 없으면 통과

    quiz_type = quiz.get("type", "blank")
    question = quiz["question"]
    answer = str(quiz["answer"])

    console.print()
    console.print(Panel(f"[bold]{question}[/]", title="퀴즈", border_style="yellow"))

    if quiz_type == "ox":
        user_answer = Prompt.ask("  O 또는 X", choices=["O", "X", "o", "x"])
    elif quiz_type == "choice":
        user_answer = Prompt.ask("  정답 입력")
    else:  # blank
        user_answer = Prompt.ask("  빈칸 채우기")

    correct = check_answer(quiz_type, user_answer, answer)
    if correct:
        console.print("  [success]정답! +5 XP[/]")
    else:
        console.print(f"  [danger]오답![/] 정답: [bold]{answer}[/]")
    return correct


def show_summary(
    studied_cards: list[dict[str, Any]],
    results: list[dict[str, Any]],
    progress: dict[str, Any],
    streak: dict[str, Any],
    config: dict[str, Any],
) -> None:
    """세션 요약을 표시한다."""
    total_xp_gained = sum(r["xp"] for r in results)
    level = calc_level(progress["total_xp"])
    current_xp, next_xp = xp_for_next_level(progress["total_xp"])
    total_cards = len(progress["cards"])
    current_streak = streak["current_streak"]

    # 과목별 학습 요약
    subject_counts: dict[str, int] = {}
    for card in studied_cards:
        subj = card.get("subject", "?")
        subject_counts[subj] = subject_counts.get(subj, 0) + 1

    subject_names = {
        "SE": "소프트웨어 설계",
        "PG": "소프트웨어 개발",
        "DB": "데이터베이스 구축",
        "NW": "시스템 통합",
        "MT": "소프트웨어 유지보수",
    }

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("과목", style="cyan")
    table.add_column("학습", style="green")
    for code, count in subject_counts.items():
        name = subject_names.get(code, code)
        table.add_row(name, f"+{count}장")

    summary_parts = [
        f"  [success]오늘 학습 완료![/]\n",
        f"  획득 XP: +{total_xp_gained}",
        f"  레벨: Lv.{level} ({current_xp}/{next_xp} XP)",
        f"  누적 카드: {total_cards}장 학습 완료",
        f"  스트릭: {current_streak}일 {'🔥' if current_streak >= 3 else ''}",
    ]

    console.print()
    console.print(Panel(
        "\n".join(summary_parts),
        title="[bold]오늘의 성취[/]",
        border_style="green",
    ))
    console.print(table)

    # 보상 리마인더
    rewards = config.get("rewards", {})
    if current_streak >= 30 and rewards.get("streak_30"):
        console.print(f"\n  [highlight]30일 연속 달성! 보상: {rewards['streak_30']}[/]")
    elif current_streak >= 7 and rewards.get("streak_7"):
        console.print(f"\n  [highlight]7일 연속 달성! 보상: {rewards['streak_7']}[/]")
    elif current_streak >= 3 and rewards.get("streak_3"):
        console.print(f"\n  [highlight]3일 연속 달성! 보상: {rewards['streak_3']}[/]")
    elif rewards.get("daily"):
        console.print(f"\n  [info]오늘의 보상: {rewards['daily']}[/]")


# ── 메인 세션 ──────────────────────────────────
def run_session() -> None:
    """학습 세션을 실행한다."""
    config = load_config()
    progress = load_progress()
    streak = load_streak()

    # 환영 화면
    show_welcome(config, streak, progress)

    # 카드 로드 및 선택
    all_cards = load_all_cards()
    if not all_cards:
        console.print("\n  [warning]학습 카드가 없습니다. content/cards/ 에 카드를 추가하세요.[/]")
        return

    today_cards = select_today_cards(all_cards, progress, config)
    if not today_cards:
        console.print("\n  [success]모든 카드를 학습했습니다! 새 카드를 추가하거나 복습을 기다려주세요.[/]")
        return

    console.print(f"\n  [info]오늘의 학습: {len(today_cards)}장[/]")
    console.print("  [dim]Enter로 시작, q로 종료[/]\n")

    try:
        _run_interactive_session(today_cards, progress, streak, config)
    except (EOFError, KeyboardInterrupt):
        console.print("\n\n  [dim]세션을 종료합니다. 다음에 만나요![/]")


def _run_interactive_session(
    today_cards: list[dict[str, Any]],
    progress: dict[str, Any],
    streak: dict[str, Any],
    config: dict[str, Any],
) -> None:
    """대화형 학습 루프. EOFError/KeyboardInterrupt는 호출자가 처리."""
    input_val = Prompt.ask("  준비되셨나요?", default="y")
    if input_val.lower() == "q":
        console.print("  [dim]다음에 만나요![/]")
        return

    results: list[dict[str, Any]] = []
    studied_cards: list[dict[str, Any]] = []

    for i, card in enumerate(today_cards, 1):
        show_card(card, i, len(today_cards))

        # 이해도 체크
        understanding = IntPrompt.ask(
            "\n  이해도 (1: 모르겠음 ~ 5: 완벽히 이해)",
            choices=["1", "2", "3", "4", "5"],
            default=3,
        )

        # 퀴즈
        quiz_correct = run_quiz(card)

        # XP 계산
        base_xp = 10
        quiz_bonus = 5 if quiz_correct else 0
        understanding_bonus = understanding * 2
        total_xp = base_xp + quiz_bonus + understanding_bonus

        # 진행 상황 업데이트 (불변 패턴)
        card_progress = {
            "understanding": understanding,
            "quiz_correct": quiz_correct,
            "last_studied": date.today().isoformat(),
            "study_count": progress["cards"].get(card["id"], {}).get("study_count", 0) + 1,
        }
        updated_cards = {**progress["cards"], card["id"]: card_progress}
        new_total_xp = progress["total_xp"] + total_xp
        progress = {
            **progress,
            "cards": updated_cards,
            "total_xp": new_total_xp,
            "level": calc_level(new_total_xp),
        }

        results.append({"card_id": card["id"], "xp": total_xp, "correct": quiz_correct})
        studied_cards.append(card)

        # 다음 카드 안내
        if i < len(today_cards):
            cont = Prompt.ask("\n  [dim]다음 카드로? (Enter=계속, q=종료)[/]", default="y")
            if cont.lower() == "q":
                break

    # 스트릭 업데이트 & 저장
    if studied_cards:
        streak = update_streak(streak)
        save_progress(progress)
        save_streak(streak)
        show_summary(studied_cards, results, progress, streak, config)


def show_progress() -> None:
    """전체 학습 진행 상황을 표시한다."""
    progress = load_progress()
    streak = load_streak()
    all_cards = load_all_cards()

    subject_names = {
        "SE": "소프트웨어 설계",
        "PG": "소프트웨어 개발",
        "DB": "데이터베이스 구축",
        "NW": "시스템 통합",
        "MT": "소프트웨어 유지보수",
    }

    # 과목별 진행률
    subject_total: dict[str, int] = {}
    subject_done: dict[str, int] = {}
    for card in all_cards:
        subj = card.get("subject", "?")
        subject_total[subj] = subject_total.get(subj, 0) + 1
        if card["id"] in progress["cards"]:
            subject_done[subj] = subject_done.get(subj, 0) + 1

    table = Table(title="과목별 진행률", border_style="cyan")
    table.add_column("과목", style="bold")
    table.add_column("진행", justify="center")
    table.add_column("진행률", justify="right")

    for code in ["SE", "PG", "DB", "NW", "MT"]:
        total = subject_total.get(code, 0)
        done = subject_done.get(code, 0)
        name = subject_names.get(code, code)
        pct = (done / total * 100) if total > 0 else 0
        bar_filled = int(pct / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        table.add_row(name, f"{done}/{total}", f"{bar} {pct:.0f}%")

    console.print()
    console.print(table)
    console.print(f"\n  레벨: Lv.{calc_level(progress['total_xp'])} | XP: {progress['total_xp']}")
    console.print(f"  현재 스트릭: {streak['current_streak']}일 | 최장: {streak['best_streak']}일")


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
            status = "✓" if card["id"] in studied else "○"
            console.print(f"  {status} [{card.get('subject', '?')}] {card['title']} ({card['id']})")
    else:
        console.print("[info]사용법: python study.py [start|progress|cards][/]")


if __name__ == "__main__":
    main()
