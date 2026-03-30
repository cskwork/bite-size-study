"""
bite CLI 테스트 — Typer CliRunner 기반.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from typer.testing import CliRunner

from bite_size_study.cli import app
from bite_size_study.paths import ROOT

runner = CliRunner()


class TestCliHelp:
    def test_help_shows_commands(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "start" in result.output
        assert "progress" in result.output
        assert "cards" in result.output
        assert "stats" in result.output
        assert "calendar" in result.output
        assert "heatmap" in result.output

    def test_start_help(self):
        result = runner.invoke(app, ["start", "--help"])
        assert result.exit_code == 0

    def test_calendar_help_shows_options(self):
        result = runner.invoke(app, ["calendar", "--help"])
        assert result.exit_code == 0
        assert "--year" in result.output
        assert "--month" in result.output


class TestCliCommands:
    def test_stats_runs(self):
        result = runner.invoke(app, ["stats"])
        assert result.exit_code == 0

    def test_cards_lists_cards(self):
        result = runner.invoke(app, ["cards"])
        assert result.exit_code == 0
        assert "카드" in result.output

    def test_progress_runs(self):
        result = runner.invoke(app, ["progress"])
        assert result.exit_code == 0

    def test_heatmap_runs(self):
        result = runner.invoke(app, ["heatmap"])
        assert result.exit_code == 0

    def test_calendar_with_options(self):
        result = runner.invoke(app, ["calendar", "--year", "2026", "--month", "1"])
        assert result.exit_code == 0
        assert "2026" in result.output

    def test_calendar_default(self):
        result = runner.invoke(app, ["calendar"])
        assert result.exit_code == 0


class TestCliHelpSubcommands:
    """모든 서브커맨드의 --help가 정상 동작하는지 검증한다."""

    def test_progress_help(self):
        result = runner.invoke(app, ["progress", "--help"])
        assert result.exit_code == 0
        assert "진행률" in result.output

    def test_cards_help(self):
        result = runner.invoke(app, ["cards", "--help"])
        assert result.exit_code == 0
        assert "카드" in result.output

    def test_stats_help(self):
        result = runner.invoke(app, ["stats", "--help"])
        assert result.exit_code == 0
        assert "스트릭" in result.output

    def test_heatmap_help(self):
        result = runner.invoke(app, ["heatmap", "--help"])
        assert result.exit_code == 0
        assert "히트맵" in result.output

    def test_help_shows_app_description(self):
        """앱 설명이 help에 포함되어야 한다."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "micro-learning" in result.output.lower() or "학습" in result.output


class TestCliOutputContent:
    """명령 출력 내용을 검증한다."""

    def test_cards_output_contains_total_count(self):
        """카드 목록에 총 카드 수가 표시되어야 한다."""
        result = runner.invoke(app, ["cards"])
        assert result.exit_code == 0
        assert "장의 카드" in result.output

    def test_cards_output_contains_status_markers(self):
        """카드 목록에 학습 상태 표시(✓/○)가 포함되어야 한다."""
        result = runner.invoke(app, ["cards"])
        assert result.exit_code == 0
        assert "✓" in result.output or "○" in result.output

    def test_cards_output_contains_subject_codes(self):
        """카드 목록에 과목 코드가 포함되어야 한다."""
        result = runner.invoke(app, ["cards"])
        assert result.exit_code == 0
        has_subject = any(
            code in result.output for code in ["SE", "PG", "DB", "NW", "MT"]
        )
        assert has_subject

    def test_stats_output_contains_streak_info(self):
        """stats에 스트릭 관련 정보가 포함되어야 한다."""
        result = runner.invoke(app, ["stats"])
        assert result.exit_code == 0
        assert "스트릭" in result.output

    def test_stats_output_contains_xp(self):
        """stats에 XP 정보가 포함되어야 한다."""
        result = runner.invoke(app, ["stats"])
        assert result.exit_code == 0
        assert "XP" in result.output

    def test_progress_output_contains_subjects(self):
        """progress에 과목별 진행률이 포함되어야 한다."""
        result = runner.invoke(app, ["progress"])
        assert result.exit_code == 0
        assert "진행률" in result.output

    def test_progress_output_contains_level(self):
        """progress에 레벨 정보가 포함되어야 한다."""
        result = runner.invoke(app, ["progress"])
        assert result.exit_code == 0
        assert "Lv." in result.output

    def test_heatmap_output_contains_symbols(self):
        """히트맵에 학습/미학습 기호가 포함되어야 한다."""
        result = runner.invoke(app, ["heatmap"])
        assert result.exit_code == 0
        assert "■" in result.output or "□" in result.output


class TestCliCalendarEdgeCases:
    """캘린더 경계값 테스트."""

    def test_calendar_year_only(self):
        """--year만 지정하면 현재 월이 기본값이어야 한다."""
        result = runner.invoke(app, ["calendar", "--year", "2026"])
        assert result.exit_code == 0
        assert "2026" in result.output

    def test_calendar_month_only(self):
        """--month만 지정하면 현재 연도가 기본값이어야 한다."""
        result = runner.invoke(app, ["calendar", "--month", "6"])
        assert result.exit_code == 0
        assert "6월" in result.output

    def test_calendar_december(self):
        """12월 캘린더 경계값 테스트."""
        result = runner.invoke(app, ["calendar", "--year", "2025", "--month", "12"])
        assert result.exit_code == 0
        assert "12월" in result.output
        assert "2025" in result.output

    def test_calendar_january(self):
        """1월 캘린더 경계값 테스트."""
        result = runner.invoke(app, ["calendar", "--year", "2026", "--month", "1"])
        assert result.exit_code == 0
        assert "1월" in result.output

    def test_calendar_february_leap_year(self):
        """윤년 2월 캘린더 테스트."""
        result = runner.invoke(app, ["calendar", "--year", "2024", "--month", "2"])
        assert result.exit_code == 0
        assert "2월" in result.output


class TestCliMenu:
    def test_no_args_non_tty_numbered_menu(self):
        """non-TTY 환경에서 번호 메뉴가 표시된다."""
        result = runner.invoke(app, [], input="7\n")
        assert result.exit_code == 0

    def test_numbered_menu_displays_all_items(self):
        """번호 메뉴에 모든 항목이 표시되어야 한다."""
        result = runner.invoke(app, [], input="7\n")
        assert result.exit_code == 0
        assert "학습 시작" in result.output
        assert "학습 현황" in result.output
        assert "카드 목록" in result.output
        assert "스트릭 통계" in result.output
        assert "학습 캘린더" in result.output
        assert "히트맵" in result.output
        assert "종료" in result.output

    def test_numbered_menu_select_cards(self):
        """번호 메뉴에서 3번(카드 목록)을 선택하면 카드가 표시된다."""
        result = runner.invoke(app, [], input="3\n")
        assert result.exit_code == 0
        assert "카드" in result.output

    def test_numbered_menu_select_stats(self):
        """번호 메뉴에서 4번(스트릭 통계)을 선택하면 통계가 표시된다."""
        result = runner.invoke(app, [], input="4\n")
        assert result.exit_code == 0
        assert "스트릭" in result.output

    def test_numbered_menu_select_progress(self):
        """번호 메뉴에서 2번(학습 현황)을 선택하면 진행률이 표시된다."""
        result = runner.invoke(app, [], input="2\n")
        assert result.exit_code == 0
        assert "진행률" in result.output

    def test_numbered_menu_select_heatmap(self):
        """번호 메뉴에서 6번(히트맵)을 선택하면 히트맵이 표시된다."""
        result = runner.invoke(app, [], input="6\n")
        assert result.exit_code == 0

    def test_numbered_menu_select_calendar(self):
        """번호 메뉴에서 5번(학습 캘린더)을 선택하면 캘린더가 표시된다."""
        result = runner.invoke(app, [], input="5\n")
        assert result.exit_code == 0
        assert "캘린더" in result.output


class TestCliInit:
    """bite init 커맨드 테스트."""

    def _cleanup(self, deck_name: str) -> None:
        deck_path = ROOT / "content" / "cards" / deck_name
        if deck_path.exists():
            shutil.rmtree(deck_path)

    def test_init_creates_deck(self):
        """init이 카드덱 디렉토리와 예시 카드를 생성한다."""
        deck_name = "_test_deck_init"
        self._cleanup(deck_name)
        try:
            result = runner.invoke(app, ["init", deck_name])
            assert result.exit_code == 0
            assert "카드덱이 생성되었습니다" in result.output

            deck_path = ROOT / "content" / "cards" / deck_name
            assert deck_path.exists()
            assert (deck_path / f"{deck_name}-001.md").exists()

            card_content = (deck_path / f"{deck_name}-001.md").read_text()
            assert "id:" in card_content
            assert "quiz:" in card_content
        finally:
            self._cleanup(deck_name)

    def test_init_existing_deck_fails(self):
        """이미 존재하는 경로에 init하면 에러를 반환한다."""
        result = runner.invoke(app, ["init", "db"])
        assert result.exit_code == 1
        assert "이미 존재" in result.output

    def test_init_default_path(self):
        """경로를 지정하지 않으면 new-deck이 기본값이다."""
        self._cleanup("new-deck")
        try:
            result = runner.invoke(app, ["init"])
            assert result.exit_code == 0
            assert (ROOT / "content" / "cards" / "new-deck").exists()
        finally:
            self._cleanup("new-deck")

    def test_init_help(self):
        """init --help가 정상 동작한다."""
        result = runner.invoke(app, ["init", "--help"])
        assert result.exit_code == 0
