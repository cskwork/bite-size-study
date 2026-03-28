#!/usr/bin/env python3
"""
streak.py shim — 기존 import 경로 호환을 위한 re-export 모듈.
"""

from __future__ import annotations

from bite_size_study.streak import (  # noqa: F401
    main,
    show_calendar,
    show_streak_stats,
    show_weekly_heatmap,
)

if __name__ == "__main__":
    main()
