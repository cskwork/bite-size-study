<!-- Generated: 2026-03-28 | Files scanned: 56 | Token estimate: ~500 -->

# Data Model — bite-size-study

## Content Layer (Markdown + YAML)

### Card Schema (YAML frontmatter in `content/cards/{subject}/*.md`)
```yaml
id: "{subject}-{chapter}-{number}"   # e.g. "db-sql-001"
subject: "DB"                         # SE, PG, DB, NW, MT
chapter: "sql"
title: "SQL 기본"
difficulty: 1                         # 1=기초, 2=응용, 3=기출심화
priority: 2                           # 3=매회, 2=자주, 1=가끔
tags: []
quiz:
  type: "blank"                       # blank, ox, choice
  question: "____"
  answer: "정답"
```

### Card Distribution (50장)
| Dir | Subject | Count |
|-----|---------|-------|
| `db/` | DB 구축 | 10 |
| `network/` | 시스템 통합 | 10 |
| `os/` | 유지보수 | 10 |
| `programming/` | SW 개발 | 11 |
| `software-eng/` | SW 설계 | 9 |

### Subject Catalog (`content/subjects.yaml`)
5과목 × 4챕터 = 20 chapter slots, NCS 기반 구조

## Config Layer (`config.yaml`)
```
session: {daily_cards: 3, max_review_cards: 5, min_session_minutes: 5}
anchors: [{trigger, action}]
identity: {message, exam_goal}
rewards: {daily, streak_3, streak_7, streak_30}
commitment: {weekly_cards: 15, weekly_quizzes: 3}
dopamine: {show_streak, show_level, show_progress_bar, celebration_emojis}
```

## State Layer (`data/`)

### progress.json
```json
{
  "cards": {
    "card-id": {
      "understanding": 1-5,
      "quiz_correct": bool,
      "last_studied": "YYYY-MM-DD",
      "study_count": int
    }
  },
  "total_xp": int,
  "level": int
}
```

### streak.json
```json
{
  "dates": ["YYYY-MM-DD", ...],
  "current_streak": int,
  "best_streak": int
}
```

## Research Layer (`research/`, `data/raw/`)
기출 동향 분석 자료 — 카드 생성 파이프라인 입력
- `research/exam-trends-2024-2026.md` — 2024~2026 기출 트렌드 분석
- `research/2026-1회-기출조사.md` — 2026년 1회 기출 조사
- `data/raw/2025-1회-기출-원자료.md` — 원본 기출 데이터
