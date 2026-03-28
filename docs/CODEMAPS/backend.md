<!-- Generated: 2026-03-28 | Files scanned: 56 | Token estimate: ~700 -->

# Backend (CLI Logic) — bite-size-study

## scripts/study.py — Main Session Engine

### CLI Commands
```
study.py              → main() → run_session()      # 학습 세션
study.py progress     → main() → show_progress()    # 과목별 진행률
study.py cards        → main() → (inline card list)  # 카드 목록
```

### Function Map
```
Data I/O:
  load_config()      → config.yaml → dict
  load_progress()    → progress.json → dict (default: {cards:{}, total_xp:0, level:1})
  save_progress()    → dict → progress.json
  load_streak()      → streak.json → dict (default: {dates:[], current_streak:0, best_streak:0})
  save_streak()      → dict → streak.json

Card Handling:
  parse_card(path)        → YAML frontmatter + body → dict | None
  load_all_cards()        → CARDS_DIR.rglob("*.md") → list[dict]
  select_today_cards()    → priority DESC sort → new[:daily] + review[:max]

Game Mechanics:
  calc_level(xp)          → XP → level (threshold: 30 × 1.3^n)
  xp_for_next_level(xp)   → (current_in_level, required) tuple
  update_streak(streak)   → immutable update → new streak dict
  check_answer(type, user, correct) → bool (OX/blank/choice, multi-answer support)

Quiz & Session:
  run_quiz(card)               → interactive quiz → bool (correct?)
  run_session()                → orchestrates full session flow
  _run_interactive_session()   → card loop: show → rate → quiz → save

UI Rendering:
  show_welcome(config, streak, progress)  → greeting + streak + level + anchor
  show_card(card, index, total)           → card panel with subject/difficulty
  show_summary(cards, results, progress, streak, config)  → XP + rewards
  show_progress()                          → subject progress bars
```

## scripts/streak.py — Visualization Engine

### CLI Commands
```
streak.py             → main() → show_all (stats + calendar + heatmap)
streak.py calendar    → show_calendar()
streak.py stats       → show_streak_stats()
streak.py heatmap     → show_weekly_heatmap()
```

### Function Map
```
show_calendar(year?, month?)  → monthly grid, study days highlighted (green)
show_streak_stats()           → 30-day progress bar + XP/cards/streak table
show_weekly_heatmap()         → 7-week GitHub-style ■/□ grid
```

## Quiz Answer Logic (check_answer)
```
OX:      case-insensitive exact match
Single:  bidirectional substring (user⊂answer OR answer⊂user)
Multi:   comma-split, count must match, each part bidirectional substring
```

## Tests

### tests/test_study.py (~486 lines)
| Class | Tests | Scope |
|-------|-------|-------|
| TestCalcLevel | 6 | XP → level 변환 |
| TestXpForNextLevel | 4 | 레벨 내 XP 계산 |
| TestUpdateStreak | 7 | 스트릭 업데이트 + 불변성 |
| TestParseCard | 3 | YAML frontmatter 파싱 |
| TestSelectTodayCards | 5 | 카드 선택 알고리즘 |
| TestLoadAllCards | 1 | 실제 카드 로드 통합 |
| TestCheckAnswer | 12 | 퀴즈 매칭 (OX/blank/multi) |
| TestShowFunctions | 7 | UI 렌더링 스모크 |
| TestShowSummary | 5 | 요약 + 보상 표시 |
| TestDataPersistence | 4 | JSON 저장/로드 |
| TestSessionEOFHandling | 1 | graceful exit |

### tests/test_streak.py (~124 lines)
| Class | Tests | Scope |
|-------|-------|-------|
| TestStreakDataConsistency | 2 | JSON 형식 + ISO 날짜 |
| TestStreakDisplay | 6 | 캘린더/히트맵 스모크 |
| TestStreakEdgeCases | 2 | 장기 공백 + 중복 업데이트 |
