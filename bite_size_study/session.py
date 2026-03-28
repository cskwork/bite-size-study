"""학습 세션 UI: 환영 화면, 카드 표시, 퀴즈, 요약."""

from __future__ import annotations

import random
import sys
from datetime import date, datetime
from typing import Any

from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.text import Text

from bite_size_study.core import (
    calc_level,
    check_answer,
    load_all_cards,
    select_today_cards,
    update_streak,
    xp_for_next_level,
)
from bite_size_study.paths import (
    load_config,
    load_progress,
    load_streak,
    save_progress,
    save_streak,
)
from bite_size_study.ui import DIFFICULTY_LABELS, SUBJECT_NAMES, console

# ── stdin UTF-8 강제 설정 (Python 3.9 + macOS 한글 입력 호환) ──
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8", errors="replace")


# ── UI 렌더링 ──────────────────────────────────
def show_welcome(
    config: dict[str, Any],
    streak: dict[str, Any],
    progress: dict[str, Any],
) -> None:
    """세션 시작 화면을 표시한다."""
    identity = config["identity"]["message"]
    goal = config["identity"]["exam_goal"]
    current_streak = streak["current_streak"]
    level = calc_level(progress["total_xp"])
    current_xp, next_xp = xp_for_next_level(progress["total_xp"])

    hour = datetime.now().hour
    if hour < 12:
        greeting = "좋은 아침!"
    elif hour < 18:
        greeting = "좋은 오후!"
    else:
        greeting = "좋은 저녁!"

    streak_display = f"{current_streak}일" if current_streak > 0 else "오늘 시작!"
    fire = " [danger]🔥[/]" if current_streak >= 3 else ""

    welcome_text = Text()
    welcome_text.append(f"  {greeting}\n", style="bold")
    welcome_text.append(f"  스트릭: {streak_display}{fire}\n")
    welcome_text.append(f"  레벨: Lv.{level} ({current_xp}/{next_xp} XP)\n")
    welcome_text.append(f"  목표: {goal}\n\n", style="info")
    welcome_text.append(f'  "{identity}"', style="highlight")

    console.print()
    console.print(
        Panel(welcome_text, title="[bold]bite-size-study[/]", border_style="cyan")
    )

    anchors = config.get("anchors", [])
    if anchors:
        anchor = random.choice(anchors)
        console.print(
            f"\n  [dim]오늘의 앵커: {anchor['trigger']} → {anchor['action']}[/]"
        )


def show_card(card: dict[str, Any], index: int, total: int) -> None:
    """학습 카드를 표시한다."""
    subject = SUBJECT_NAMES.get(card.get("subject", ""), card.get("subject", ""))
    diff_label = DIFFICULTY_LABELS.get(card.get("difficulty", 1), "기초")

    header = f"[{index}/{total}] {subject} | {diff_label}"
    console.print()
    console.print(Panel(
        Markdown(card["body"]),
        title=f"[bold]{header}[/]",
        subtitle=f"[dim]{card['id']}[/]",
        border_style="green",
        padding=(1, 2),
    ))


def run_quiz(card: dict[str, Any]) -> bool:
    """카드의 퀴즈를 실행한다. 정답 여부를 반환."""
    quiz = card.get("quiz", {})
    if not quiz or not quiz.get("question"):
        return True

    quiz_type = quiz.get("type", "blank")
    question = quiz["question"]
    answer = str(quiz["answer"])

    console.print()
    console.print(Panel(f"[bold]{question}[/]", title="퀴즈", border_style="yellow"))

    answer_parts = [p.strip() for p in answer.split(",")]
    multi_hint = (
        f" [dim](쉼표로 {len(answer_parts)}개 입력)[/]"
        if len(answer_parts) > 1
        else ""
    )

    try:
        if quiz_type == "ox":
            user_answer = Prompt.ask("  O 또는 X", choices=["O", "X", "o", "x"])
        elif quiz_type == "choice":
            user_answer = Prompt.ask("  정답 입력")
        else:
            user_answer = Prompt.ask(f"  빈칸 채우기{multi_hint}")
    except UnicodeDecodeError:
        console.print("  [warning]입력 인코딩 오류 — 건너뜁니다[/]")
        console.print(f"  정답: [bold]{answer}[/]")
        return False

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

    subject_counts: dict[str, int] = {}
    for card in studied_cards:
        subj = card.get("subject", "?")
        subject_counts[subj] = subject_counts.get(subj, 0) + 1

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("과목", style="cyan")
    table.add_column("학습", style="green")
    for code, count in subject_counts.items():
        name = SUBJECT_NAMES.get(code, code)
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

    show_welcome(config, streak, progress)

    all_cards = load_all_cards()
    if not all_cards:
        console.print(
            "\n  [warning]학습 카드가 없습니다. content/cards/ 에 카드를 추가하세요.[/]"
        )
        return

    today_cards = select_today_cards(all_cards, progress, config)
    if not today_cards:
        console.print(
            "\n  [success]모든 카드를 학습했습니다! 새 카드를 추가하거나 복습을 기다려주세요.[/]"
        )
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

        understanding = IntPrompt.ask(
            "\n  이해도 (1: 모르겠음 ~ 5: 완벽히 이해)",
            choices=["1", "2", "3", "4", "5"],
            default=3,
        )

        quiz_correct = run_quiz(card)

        base_xp = 10
        quiz_bonus = 5 if quiz_correct else 0
        understanding_bonus = understanding * 2
        total_xp = base_xp + quiz_bonus + understanding_bonus

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

        if i < len(today_cards):
            cont = Prompt.ask(
                "\n  [dim]다음 카드로? (Enter=계속, q=종료)[/]", default="y"
            )
            if cont.lower() == "q":
                break

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
        name = SUBJECT_NAMES.get(code, code)
        pct = (done / total * 100) if total > 0 else 0
        bar_filled = int(pct / 5)
        bar = "\u2588" * bar_filled + "\u2591" * (20 - bar_filled)
        table.add_row(name, f"{done}/{total}", f"{bar} {pct:.0f}%")

    console.print()
    console.print(table)
    console.print(
        f"\n  레벨: Lv.{calc_level(progress['total_xp'])} | XP: {progress['total_xp']}"
    )
    console.print(
        f"  현재 스트릭: {streak['current_streak']}일 | 최장: {streak['best_streak']}일"
    )
