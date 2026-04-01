"""순수 함수: 레벨, XP, 스트릭, 카드 선택, 퀴즈 판정."""

from __future__ import annotations

import logging
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from bite_size_study.paths import CARDS_DIR

logger = logging.getLogger(__name__)


# ── 카드 파싱 ──────────────────────────────────
def parse_card(card_path: Path) -> dict[str, Any] | None:
    """YAML frontmatter + Markdown 본문을 파싱한다."""
    text = card_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        logger.warning("Skipping card (no frontmatter): %s", card_path)
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        logger.warning("Skipping card (malformed frontmatter): %s", card_path)
        return None

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        logger.warning("Skipping card (YAML parse error): %s — %s", card_path, exc)
        return None

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
    """오늘 학습할 카드를 선택한다. 출제빈도(priority) 높은 카드 우선."""
    daily_new = config["session"]["daily_cards"]
    max_review = config["session"]["max_review_cards"]

    new_cards = sorted(
        [c for c in cards if c["id"] not in progress["cards"]],
        key=lambda c: c.get("priority", 2),
        reverse=True,
    )
    review_cards = sorted(
        [
            c for c in cards
            if c["id"] in progress["cards"]
            and progress["cards"][c["id"]].get("understanding", 0) <= 3
        ],
        key=lambda c: c.get("priority", 2),
        reverse=True,
    )

    selected_new = new_cards[:daily_new]
    selected_review = review_cards[:max_review]
    return selected_new + selected_review


# ── XP / 레벨 시스템 ──────────────────────────
def calc_level(xp: int) -> int:
    """XP 기반 레벨 계산. 레벨업에 필요한 XP가 점진적으로 증가."""
    level = 1
    required = 30
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
    """오늘 날짜를 기록하고 스트릭을 업데이트한다. 원본을 변경하지 않는다."""
    today = date.today().isoformat()
    yesterday = date.today().toordinal() - 1

    if today in streak["dates"]:
        return streak

    yesterday_str = date.fromordinal(yesterday).isoformat()
    new_current = (
        streak["current_streak"] + 1
        if yesterday_str in set(streak["dates"])
        else 1
    )

    return {
        **streak,
        "dates": streak["dates"] + [today],
        "current_streak": new_current,
        "best_streak": max(streak["best_streak"], new_current),
    }


# ── 퀴즈 판정 ─────────────────────────────────
def extract_answer_key(answer: str) -> str:
    """정답 문자열에서 비교용 핵심 부분만 추출한다.

    카드의 answer 필드는 'actual_answer — explanation (기출 출처)' 형태이므로
    ' — ' 이후의 설명/메타데이터를 제거하여 비교에 사용한다.
    """
    idx = answer.find(" — ")
    return answer[:idx].strip() if idx != -1 else answer.strip()


def check_answer(quiz_type: str, user_answer: str, correct_answer: str) -> bool:
    """퀴즈 정답을 판정한다. 다중 답안(쉼표 구분)은 모든 파트 매칭 필요."""
    if quiz_type == "ox":
        answer_key = extract_answer_key(correct_answer)
        return user_answer.upper() == answer_key.upper()

    answer_key = extract_answer_key(correct_answer)
    answer_parts = [p.strip().lower() for p in answer_key.split(",")]
    if len(answer_parts) > 1:
        user_parts = [p.strip().lower() for p in user_answer.split(",")]
        if len(user_parts) != len(answer_parts):
            return False
        return all(
            up in ap or ap in up
            for up, ap in zip(user_parts, answer_parts)
        )

    user_lower = user_answer.lower().strip()
    answer_lower = answer_key.lower()
    return user_lower in answer_lower or answer_lower in user_lower
