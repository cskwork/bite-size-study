"""
bite-size-study 핵심 로직 테스트

TDD RED Phase: 순수 함수(레벨, XP, 스트릭, 카드 선택)를 검증한다.
Interactive I/O는 분리하여 EOFError 핸들링을 테스트한다.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from textwrap import dedent

import pytest

# ── 테스트 대상 임포트 ─────────────────────────
from scripts.study import (
    calc_level,
    check_answer,
    extract_answer_key,
    load_all_cards,
    load_config,
    load_progress,
    load_streak,
    parse_card,
    save_progress,
    save_streak,
    select_today_cards,
    show_card,
    show_progress,
    show_summary,
    show_welcome,
    update_streak,
    xp_for_next_level,
)


# ══════════════════════════════════════════════════
#  calc_level 테스트
# ══════════════════════════════════════════════════
class TestCalcLevel:
    def test_zero_xp_is_level_1(self):
        assert calc_level(0) == 1

    def test_exactly_30_xp_is_level_2(self):
        assert calc_level(30) == 2

    def test_29_xp_still_level_1(self):
        assert calc_level(29) == 1

    def test_level_3_threshold(self):
        # 레벨 2→3: 30 + int(30*1.3)=39 → 총 69 XP
        assert calc_level(68) == 2
        assert calc_level(69) == 3

    def test_high_xp_increases_level(self):
        # 레벨이 단조 증가하는지 확인
        prev_level = 1
        for xp in range(0, 1000, 50):
            level = calc_level(xp)
            assert level >= prev_level
            prev_level = level

    def test_negative_xp_is_level_1(self):
        assert calc_level(-10) == 1


# ══════════════════════════════════════════════════
#  xp_for_next_level 테스트
# ══════════════════════════════════════════════════
class TestXpForNextLevel:
    def test_zero_xp(self):
        current, required = xp_for_next_level(0)
        assert current == 0
        assert required == 30

    def test_mid_level(self):
        current, required = xp_for_next_level(15)
        assert current == 15
        assert required == 30

    def test_just_leveled_up(self):
        current, required = xp_for_next_level(30)
        assert current == 0
        assert required == 39  # int(30 * 1.3)

    def test_current_never_exceeds_required(self):
        for xp in range(0, 500):
            current, required = xp_for_next_level(xp)
            assert current < required


# ══════════════════════════════════════════════════
#  update_streak 테스트
# ══════════════════════════════════════════════════
class TestUpdateStreak:
    def test_first_day_streak(self):
        streak = {"dates": [], "current_streak": 0, "best_streak": 0}
        result = update_streak(streak)
        assert result["current_streak"] == 1
        assert date.today().isoformat() in result["dates"]

    def test_consecutive_day_increases_streak(self):
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        streak = {"dates": [yesterday], "current_streak": 5, "best_streak": 10}
        result = update_streak(streak)
        assert result["current_streak"] == 6

    def test_skip_day_resets_streak(self):
        two_days_ago = (date.today() - timedelta(days=2)).isoformat()
        streak = {"dates": [two_days_ago], "current_streak": 5, "best_streak": 10}
        result = update_streak(streak)
        assert result["current_streak"] == 1

    def test_same_day_no_duplicate(self):
        today = date.today().isoformat()
        streak = {"dates": [today], "current_streak": 3, "best_streak": 5}
        result = update_streak(streak)
        assert result["dates"].count(today) == 1
        assert result["current_streak"] == 3  # 변하지 않음

    def test_best_streak_updates(self):
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        streak = {"dates": [yesterday], "current_streak": 10, "best_streak": 10}
        result = update_streak(streak)
        assert result["best_streak"] == 11

    def test_best_streak_preserved_on_reset(self):
        two_days_ago = (date.today() - timedelta(days=2)).isoformat()
        streak = {"dates": [two_days_ago], "current_streak": 3, "best_streak": 15}
        result = update_streak(streak)
        assert result["current_streak"] == 1
        assert result["best_streak"] == 15  # 최고 기록 유지

    def test_immutability(self):
        """원본 streak dict가 변경되지 않아야 한다."""
        streak = {"dates": [], "current_streak": 0, "best_streak": 0}
        result = update_streak(streak)
        assert streak["dates"] == []  # 원본 불변
        assert streak["current_streak"] == 0
        assert result is not streak


# ══════════════════════════════════════════════════
#  parse_card 테스트
# ══════════════════════════════════════════════════
class TestParseCard:
    def test_valid_card(self, tmp_path: Path):
        card_file = tmp_path / "test-card.md"
        card_file.write_text(dedent("""\
            ---
            id: "test-001"
            subject: "DB"
            title: "테스트 카드"
            difficulty: 1
            quiz:
              type: "ox"
              question: "테스트 질문"
              answer: "O"
            ---

            ## 테스트 카드

            ### 핵심 개념
            테스트 내용입니다.
        """), encoding="utf-8")

        card = parse_card(card_file)

        assert card is not None
        assert card["id"] == "test-001"
        assert card["subject"] == "DB"
        assert card["title"] == "테스트 카드"
        assert card["quiz"]["type"] == "ox"
        assert "body" in card
        assert "테스트 내용" in card["body"]

    def test_missing_frontmatter(self, tmp_path: Path):
        card_file = tmp_path / "no-front.md"
        card_file.write_text("# Just a regular markdown file\n", encoding="utf-8")

        card = parse_card(card_file)
        assert card is None

    def test_incomplete_frontmatter(self, tmp_path: Path):
        card_file = tmp_path / "incomplete.md"
        card_file.write_text("---\nid: test\n", encoding="utf-8")

        card = parse_card(card_file)
        assert card is None


# ══════════════════════════════════════════════════
#  select_today_cards 테스트
# ══════════════════════════════════════════════════
class TestSelectTodayCards:
    @pytest.fixture()
    def sample_cards(self) -> list[dict]:
        return [
            {"id": "card-1", "subject": "DB", "title": "카드1"},
            {"id": "card-2", "subject": "SE", "title": "카드2"},
            {"id": "card-3", "subject": "PG", "title": "카드3"},
            {"id": "card-4", "subject": "NW", "title": "카드4"},
            {"id": "card-5", "subject": "MT", "title": "카드5"},
        ]

    @pytest.fixture()
    def default_config(self) -> dict:
        return {"session": {"daily_cards": 3, "max_review_cards": 5}}

    def test_selects_new_cards_first(self, sample_cards, default_config):
        progress = {"cards": {}}
        result = select_today_cards(sample_cards, progress, default_config)
        assert len(result) == 3
        assert result[0]["id"] == "card-1"

    def test_includes_review_cards(self, sample_cards, default_config):
        progress = {
            "cards": {
                "card-1": {"understanding": 2},  # 복습 대상 (≤3)
                "card-2": {"understanding": 5},  # 복습 불필요
            }
        }
        result = select_today_cards(sample_cards, progress, default_config)
        # 새 카드 3개 (card-3,4,5) + 복습 1개 (card-1)
        result_ids = [c["id"] for c in result]
        assert "card-3" in result_ids
        assert "card-1" in result_ids  # 복습 대상
        assert "card-2" not in result_ids  # 이해도 높아 제외

    def test_empty_cards_returns_empty(self, default_config):
        result = select_today_cards([], {"cards": {}}, default_config)
        assert result == []

    def test_all_cards_studied_high_understanding(self, sample_cards, default_config):
        progress = {
            "cards": {
                c["id"]: {"understanding": 5} for c in sample_cards
            }
        }
        result = select_today_cards(sample_cards, progress, default_config)
        assert result == []

    def test_respects_daily_limit(self, sample_cards):
        config = {"session": {"daily_cards": 1, "max_review_cards": 0}}
        progress = {"cards": {}}
        result = select_today_cards(sample_cards, progress, config)
        assert len(result) == 1


# ══════════════════════════════════════════════════
#  load_all_cards 통합 테스트
# ══════════════════════════════════════════════════
class TestLoadAllCards:
    def test_loads_real_cards(self):
        """실제 content/cards 디렉토리에서 카드를 로드한다."""
        cards = load_all_cards()
        assert len(cards) >= 20  # 최소 20장
        for card in cards:
            assert "id" in card
            assert "subject" in card
            assert "body" in card


# ══════════════════════════════════════════════════
#  run_session EOFError 핸들링 테스트
# ══════════════════════════════════════════════════
# ══════════════════════════════════════════════════
#  check_answer 테스트 (퀴즈 매칭 로직)
# ══════════════════════════════════════════════════
class TestCheckAnswer:
    def test_ox_correct(self):
        assert check_answer("ox", "O", "O") is True
        assert check_answer("ox", "x", "X") is True

    def test_ox_incorrect(self):
        assert check_answer("ox", "O", "X") is False

    def test_ox_case_insensitive(self):
        assert check_answer("ox", "o", "O") is True

    def test_blank_exact_match(self):
        assert check_answer("blank", "제2정규형", "제2정규형") is True

    def test_blank_partial_user_input(self):
        """핵심 키워드만 입력해도 정답 처리."""
        assert check_answer("blank", "제2정규형", "제2정규형(2NF)") is True

    def test_blank_full_answer_in_short_input(self):
        """정답이 사용자 입력에 포함되어도 정답."""
        assert check_answer("blank", "정답은 제2정규형(2NF)입니다", "제2정규형") is True

    def test_blank_wrong_answer(self):
        assert check_answer("blank", "제3정규형", "제2정규형(2NF)") is False

    def test_choice_number_match(self):
        assert check_answer("choice", "3", "(3) UPDATE") is True

    def test_choice_text_match(self):
        assert check_answer("choice", "UPDATE", "(3) UPDATE") is True

    def test_blank_whitespace_tolerance(self):
        assert check_answer("blank", " 세그먼트 ", "세그먼트") is True

    def test_multi_answer_all_correct(self):
        """다중 답안: 모든 파트를 쉼표로 구분하여 입력하면 정답."""
        assert check_answer("blank", "4, 5", "4, 5") is True

    def test_multi_answer_partial_match(self):
        """다중 답안: 각 파트가 부분 매칭되어도 정답."""
        assert check_answer("blank", "Degree, Cardinality", "Degree(차수), Cardinality(카디널리티)") is True

    def test_multi_answer_only_one_part(self):
        """다중 답안: 하나만 입력하면 오답."""
        assert check_answer("blank", "4", "4, 5") is False

    def test_multi_answer_wrong_order(self):
        """다중 답안: 순서가 다르면 오답 (빈칸 순서대로 입력해야 함)."""
        assert check_answer("blank", "5, 4", "4, 5") is False

    def test_multi_answer_wrong_count(self):
        """다중 답안: 개수가 다르면 오답."""
        assert check_answer("blank", "4, 5, 6", "4, 5") is False

    def test_multi_answer_with_metadata(self):
        """실제 카드: 정답에 기출 출처 메타데이터가 포함되어도 정답 판정."""
        real_answer = "Degree = 4 (속성/컬럼 수), Cardinality = 5 (튜플/행 수) — 2024-2회, 2025-1회 기출"
        assert check_answer("blank", "4, 5", real_answer) is True
        assert check_answer("blank", "Degree = 4, Cardinality = 5", real_answer) is True

    def test_multi_answer_with_metadata_wrong(self):
        """실제 카드: 메타데이터가 있어도 틀린 답은 오답."""
        real_answer = "Degree = 4 (속성/컬럼 수), Cardinality = 5 (튜플/행 수) — 2024-2회, 2025-1회 기출"
        assert check_answer("blank", "5, 4", real_answer) is False

    def test_single_answer_with_explanation(self):
        """단일 답안에 설명이 붙어도 정답 판정."""
        assert check_answer("blank", "고립성", "고립성(Isolation) — 동시에 실행되는 트랜잭션") is True

    def test_ox_with_explanation(self):
        """OX 문제에 설명이 붙어도 정답 판정."""
        assert check_answer("ox", "X", "X — Hash join은 정렬 불필요") is True

    def test_sql_multi_answer_with_explanation(self):
        """SQL 다중 답안에 설명이 붙어도 정답 판정."""
        real_answer = "INSERT, SELECT — INSERT INTO...SELECT 구문으로 삽입한다 (2024-2회 기출)"
        assert check_answer("blank", "INSERT, SELECT", real_answer) is True


# ══════════════════════════════════════════════════
#  extract_answer_key 테스트
# ══════════════════════════════════════════════════
class TestExtractAnswerKey:
    def test_strips_explanation(self):
        result = extract_answer_key("4, 5 — 설명 텍스트")
        assert result == "4, 5"

    def test_strips_metadata_with_commas(self):
        result = extract_answer_key(
            "Degree = 4 (속성/컬럼 수), Cardinality = 5 (튜플/행 수) — 2024-2회, 2025-1회 기출"
        )
        assert result == "Degree = 4 (속성/컬럼 수), Cardinality = 5 (튜플/행 수)"

    def test_no_explanation(self):
        result = extract_answer_key("제2정규형(2NF)")
        assert result == "제2정규형(2NF)"

    def test_whitespace_only_answer(self):
        result = extract_answer_key("  CROSS  ")
        assert result == "CROSS"


# ══════════════════════════════════════════════════
#  show 함수 스모크 테스트 (크래시 방지)
# ══════════════════════════════════════════════════
class TestShowFunctions:
    def test_show_welcome_no_crash(self, capsys):
        config = load_config()
        streak = {"dates": [], "current_streak": 0, "best_streak": 0}
        progress = {"cards": {}, "total_xp": 0, "level": 1}
        show_welcome(config, streak, progress)

    def test_show_welcome_with_streak(self, capsys):
        config = load_config()
        streak = {"dates": ["2026-03-28"], "current_streak": 7, "best_streak": 10}
        progress = {"cards": {}, "total_xp": 100, "level": 3}
        show_welcome(config, streak, progress)

    def test_show_card_no_crash(self, capsys):
        card = {
            "id": "test-001",
            "subject": "DB",
            "difficulty": 1,
            "body": "## 테스트\n\n내용",
        }
        show_card(card, 1, 3)

    def test_show_card_unknown_subject(self, capsys):
        card = {
            "id": "test-001",
            "subject": "XX",
            "difficulty": 2,
            "body": "## 테스트",
        }
        show_card(card, 1, 1)

    def test_show_progress_no_crash(self, capsys):
        show_progress()

    def test_main_cards_command(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["study.py", "cards"])
        from scripts.study import main
        main()

    def test_main_progress_command(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["study.py", "progress"])
        from scripts.study import main
        main()

    def test_main_unknown_command(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["study.py", "unknown"])
        from scripts.study import main
        main()


# ══════════════════════════════════════════════════
#  show_summary 테스트
# ══════════════════════════════════════════════════
class TestShowSummary:
    def test_summary_no_crash(self, capsys):
        cards = [{"id": "db-001", "subject": "DB"}]
        results = [{"card_id": "db-001", "xp": 15, "correct": True}]
        progress = {"cards": {"db-001": {}}, "total_xp": 50}
        streak = {"dates": ["2026-03-28"], "current_streak": 1, "best_streak": 1}
        config = load_config()
        show_summary(cards, results, progress, streak, config)

    def test_summary_streak_3_reward(self, capsys):
        cards = [{"id": "db-001", "subject": "DB"}]
        results = [{"card_id": "db-001", "xp": 15, "correct": True}]
        progress = {"cards": {"db-001": {}}, "total_xp": 100}
        streak = {"dates": [], "current_streak": 3, "best_streak": 3}
        config = load_config()
        show_summary(cards, results, progress, streak, config)

    def test_summary_streak_7_reward(self, capsys):
        cards = [{"id": "se-001", "subject": "SE"}]
        results = [{"card_id": "se-001", "xp": 20, "correct": False}]
        progress = {"cards": {"se-001": {}}, "total_xp": 200}
        streak = {"dates": [], "current_streak": 7, "best_streak": 7}
        config = load_config()
        show_summary(cards, results, progress, streak, config)

    def test_summary_streak_30_reward(self, capsys):
        cards = [{"id": "nw-001", "subject": "NW"}]
        results = [{"card_id": "nw-001", "xp": 10, "correct": True}]
        progress = {"cards": {"nw-001": {}}, "total_xp": 500}
        streak = {"dates": [], "current_streak": 30, "best_streak": 30}
        config = load_config()
        show_summary(cards, results, progress, streak, config)

    def test_summary_multiple_subjects(self, capsys):
        cards = [
            {"id": "db-001", "subject": "DB"},
            {"id": "se-001", "subject": "SE"},
            {"id": "pg-001", "subject": "PG"},
        ]
        results = [
            {"card_id": "db-001", "xp": 15, "correct": True},
            {"card_id": "se-001", "xp": 10, "correct": False},
            {"card_id": "pg-001", "xp": 20, "correct": True},
        ]
        progress = {"cards": {c["id"]: {} for c in cards}, "total_xp": 80}
        streak = {"dates": [], "current_streak": 2, "best_streak": 5}
        config = load_config()
        show_summary(cards, results, progress, streak, config)


# ══════════════════════════════════════════════════
#  데이터 저장/로드 테스트
# ══════════════════════════════════════════════════
class TestDataPersistence:
    def test_save_and_load_progress(self, tmp_path: Path, monkeypatch):
        monkeypatch.setattr("scripts.study.DATA_DIR", tmp_path)
        monkeypatch.setattr("scripts.study.PROGRESS_PATH", tmp_path / "progress.json")

        progress = {"cards": {"db-001": {"understanding": 4}}, "total_xp": 50, "level": 2}
        save_progress(progress)
        loaded = load_progress()
        assert loaded["total_xp"] == 50
        assert loaded["cards"]["db-001"]["understanding"] == 4

    def test_save_and_load_streak(self, tmp_path: Path, monkeypatch):
        monkeypatch.setattr("scripts.study.DATA_DIR", tmp_path)
        monkeypatch.setattr("scripts.study.STREAK_PATH", tmp_path / "streak.json")

        streak = {"dates": ["2026-03-28"], "current_streak": 1, "best_streak": 5}
        save_streak(streak)
        loaded = load_streak()
        assert loaded["current_streak"] == 1
        assert loaded["best_streak"] == 5

    def test_load_progress_missing_file(self, tmp_path: Path, monkeypatch):
        monkeypatch.setattr("scripts.study.PROGRESS_PATH", tmp_path / "nonexistent.json")
        result = load_progress()
        assert result == {"cards": {}, "total_xp": 0, "level": 1}

    def test_load_streak_missing_file(self, tmp_path: Path, monkeypatch):
        monkeypatch.setattr("scripts.study.STREAK_PATH", tmp_path / "nonexistent.json")
        result = load_streak()
        assert result == {"dates": [], "current_streak": 0, "best_streak": 0}


# ══════════════════════════════════════════════════
#  run_session EOFError 핸들링 테스트
# ══════════════════════════════════════════════════
class TestSessionEOFHandling:
    def test_session_handles_eof_gracefully(self, monkeypatch):
        """stdin이 없을 때 EOFError 대신 graceful exit해야 한다."""
        from scripts.study import run_session

        # stdin을 빈 상태로 만들어 EOFError 유발
        import io
        monkeypatch.setattr("sys.stdin", io.StringIO(""))

        # EOFError가 아닌 정상 종료 또는 SystemExit
        try:
            run_session()
        except (EOFError, KeyboardInterrupt):
            pytest.fail("run_session()이 EOFError를 처리하지 못했습니다")
        except SystemExit:
            pass  # 정상 종료
