<!-- Generated: 2026-03-28 | Files scanned: 56 | Token estimate: ~600 -->

# Architecture — bite-size-study

## System Type
Single-app Python CLI — 뇌과학 기반 정보처리실기 학습 시스템

## Data Flow
```
config.yaml ─┐
              ├─→ scripts/study.py ─→ data/progress.json
cards/*.md ───┘         │               data/streak.json
                        ▼
                  Rich TUI (terminal)

scripts/streak.py ─→ data/streak.json (read-only)
                         │
                         ▼
                   Rich TUI (calendar, heatmap)
```

## Entry Points
- `scripts/study.py [start|progress|cards]` — 학습 세션 + 진행률 조회
- `scripts/streak.py [all|calendar|stats|heatmap]` — 스트릭 시각화

## Module Responsibilities
| Module | Role | Lines |
|--------|------|-------|
| `scripts/study.py` | 학습 세션, XP/레벨, 카드 선택, 퀴즈, 진행 저장 | ~540 |
| `scripts/streak.py` | 스트릭 통계, 월간 캘린더, 7주 히트맵 | ~185 |

## State Files (JSON)
| File | Schema |
|------|--------|
| `data/progress.json` | `{cards: {id: {understanding, quiz_correct, last_studied, study_count}}, total_xp, level}` |
| `data/streak.json` | `{dates: [ISO], current_streak, best_streak}` |

## Key Algorithms
- **Card selection**: priority DESC → 새 카드(daily_cards) + 복습 카드(understanding ≤ 3)
- **XP/Level**: base(10) + quiz(5) + understanding(×2); level threshold = 30 × 1.3^n
- **Streak**: 어제 학습 기록 존재 → +1, 아니면 리셋; best_streak 보존

## Dependencies
- `rich` ≥13.0 — TUI 렌더링 (Panel, Table, Markdown, Prompt)
- `pyyaml` ≥6.0 — config/card frontmatter 파싱
- `pytest` — 테스트 (dev)
