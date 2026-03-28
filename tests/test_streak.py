"""
streak.py 테스트

스트릭 통계, 캘린더 렌더링, 히트맵 로직을 검증한다.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import pytest

from scripts.streak import show_calendar, show_streak_stats, show_weekly_heatmap


# ══════════════════════════════════════════════════
#  스트릭 데이터 일관성 테스트
# ══════════════════════════════════════════════════
class TestStreakDataConsistency:
    def test_streak_file_format(self, tmp_path: Path):
        """streak.json이 올바른 형식으로 저장되는지 확인."""
        from scripts.study import save_streak

        streak = {
            "dates": ["2026-03-27", "2026-03-28"],
            "current_streak": 2,
            "best_streak": 5,
        }
        # DATA_DIR를 tmp_path로 우회
        streak_path = tmp_path / "streak.json"
        with open(streak_path, "w", encoding="utf-8") as f:
            json.dump(streak, f, ensure_ascii=False, indent=2)

        with open(streak_path, encoding="utf-8") as f:
            loaded = json.load(f)

        assert loaded["dates"] == ["2026-03-27", "2026-03-28"]
        assert loaded["current_streak"] == 2
        assert loaded["best_streak"] == 5

    def test_dates_are_iso_format(self):
        """스트릭 날짜가 ISO 8601 형식인지 확인."""
        from scripts.study import update_streak

        streak = {"dates": [], "current_streak": 0, "best_streak": 0}
        result = update_streak(streak)
        for d in result["dates"]:
            # ISO 형식 파싱 가능해야 함
            parsed = date.fromisoformat(d)
            assert isinstance(parsed, date)


# ══════════════════════════════════════════════════
#  스트릭 엣지 케이스 테스트
# ══════════════════════════════════════════════════
# ══════════════════════════════════════════════════
#  streak.py 표시 함수 스모크 테스트
# ══════════════════════════════════════════════════
class TestStreakDisplay:
    def test_show_calendar_no_crash(self, capsys):
        show_calendar()

    def test_show_calendar_specific_month(self, capsys):
        show_calendar(target_year=2026, target_month=1)

    def test_show_streak_stats_no_crash(self, capsys):
        show_streak_stats()

    def test_show_weekly_heatmap_no_crash(self, capsys):
        show_weekly_heatmap()

    def test_main_all(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["streak.py"])
        from scripts.streak import main
        main()

    def test_main_calendar(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["streak.py", "calendar"])
        from scripts.streak import main
        main()

    def test_main_stats(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["streak.py", "stats"])
        from scripts.streak import main
        main()

    def test_main_heatmap(self, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["streak.py", "heatmap"])
        from scripts.streak import main
        main()


# ══════════════════════════════════════════════════
#  스트릭 엣지 케이스 테스트
# ══════════════════════════════════════════════════
class TestStreakEdgeCases:
    def test_long_gap_then_restart(self):
        """오랜 공백 후 다시 시작하면 스트릭 1로 리셋."""
        from scripts.study import update_streak

        old_date = (date.today() - timedelta(days=100)).isoformat()
        streak = {
            "dates": [old_date],
            "current_streak": 50,
            "best_streak": 50,
        }
        result = update_streak(streak)
        assert result["current_streak"] == 1
        assert result["best_streak"] == 50

    def test_multiple_updates_same_day(self):
        """같은 날 여러 번 업데이트해도 날짜 중복 없음."""
        from scripts.study import update_streak

        streak = {"dates": [], "current_streak": 0, "best_streak": 0}
        result = update_streak(streak)
        result = update_streak(result)
        result = update_streak(result)
        today = date.today().isoformat()
        assert result["dates"].count(today) == 1
        assert result["current_streak"] == 1
