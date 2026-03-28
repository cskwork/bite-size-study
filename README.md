# bite-size-study

뇌과학 기반 정보처리기사 실기 학습 CLI. 하기 싫어도 시스템이 끌고 간다.

## 주요 기능

- **인터랙티브 메뉴** — 화살표 키로 탐색, 한 화면에서 모든 기능 접근
- **학습 세션** — 출제빈도 기반 카드 선택 + 퀴즈 (OX, 빈칸, 선택)
- **XP & 레벨 시스템** — 학습할수록 레벨업, 도파민 설계
- **스트릭 추적** — 연속 학습일 기록, 보상 연결
- **학습 캘린더** — GitHub 잔디 스타일 월간 캘린더
- **히트맵** — 최근 7주 학습 현황 시각화
- **과목별 진행률** — SE, PG, DB, NW, MT 5과목 진행 추적

## 핵심 원리

| 원리 | 메커니즘 | 시스템 적용 |
|------|----------|------------|
| 마이크로 습관 | 극단적으로 쉽게 시작 | 카드 2-3장 (5분) |
| 5분 규칙 | 자이가르닉 효과 → 자연 지속 | 최소 세션 5분 |
| If-Then 계획 | 결정 피로 제거 (d=0.65) | config.yaml 앵커 |
| 스트릭 | 가시적 진행 = 3.6배 동기 | 캘린더 + 히트맵 |
| 유혹 묶기 | 도파민 연합 학습 | 학습 후 보상 연결 |
| 정체성 전환 | 행동→정체성 루프 (r=0.55) | 세션 시작 메시지 |

## 설치

```bash
pip install -e .
```

## 사용법

```bash
# 인터랙티브 메뉴 (추천)
bite

# 개별 명령어
bite start        # 학습 세션 시작
bite progress     # 과목별 진행률
bite cards        # 전체 카드 목록
bite stats        # 스트릭 통계
bite calendar     # 월간 학습 캘린더
bite heatmap      # 최근 7주 히트맵

# 캘린더 옵션
bite calendar --year 2026 --month 3
```

### 레거시 스크립트 (호환 유지)

```bash
python scripts/study.py              # 학습 세션
python scripts/study.py progress     # 진행률
python scripts/study.py cards        # 카드 목록
python scripts/streak.py             # 스트릭 전체
python scripts/streak.py calendar    # 월간 캘린더
python scripts/streak.py heatmap     # 7주 히트맵
```

## 프로젝트 구조

```
bite-size-study/
├── bite_size_study/        # 메인 패키지
│   ├── cli.py              # Typer CLI 진입점
│   ├── menu.py             # 인터랙티브 화살표 키 메뉴
│   ├── core.py             # 순수 함수 (레벨, XP, 스트릭, 퀴즈)
│   ├── session.py          # 학습 세션 UI
│   ├── streak.py           # 스트릭 통계 + 캘린더 시각화
│   ├── paths.py            # 경로 상수 + 데이터 I/O
│   └── ui.py               # Rich 테마 + 공유 상수
├── scripts/                # 레거시 호환 shim
├── content/cards/          # 학습 카드 (YAML frontmatter + Markdown)
├── data/                   # 학습 진행 데이터 (JSON)
├── config.yaml             # 세션, 앵커, 보상 설정
├── tests/                  # pytest 테스트
└── pyproject.toml          # 패키지 설정
```

## 설정 커스터마이징

`config.yaml`에서 조정:

| 설정 | 설명 | 기본값 |
|------|------|--------|
| `session.daily_cards` | 하루 새 카드 수 | 3 |
| `session.max_review_cards` | 하루 최대 복습 카드 수 | 5 |
| `anchors` | If-Then 트리거 설정 | 아침 커피, 점심 후 |
| `identity.message` | 정체성 메시지 | "나는 매일 성장하는 개발자다." |
| `rewards` | 스트릭별 보상 | daily, 3일, 7일, 30일 |

## 카드 추가

`content/cards/{과목}/`에 Markdown 파일 추가:

```markdown
---
id: "db-051"
subject: "DB"
title: "정규화 단계"
difficulty: 2
priority: 3
quiz:
  type: "blank"
  question: "제2정규형(2NF)은 ___을 제거한 것이다."
  answer: "부분 함수 종속"
---

## 정규화 단계

### 핵심 개념
...
```

과목 코드: SE(소프트웨어 설계), PG(소프트웨어 개발), DB(데이터베이스), NW(시스템 통합), MT(유지보수)

## 테스트

```bash
pytest tests/ -v
```

## 기술 스택

- Python 3.9+
- [Typer](https://typer.tiangolo.com/) — CLI 프레임워크
- [Rich](https://rich.readthedocs.io/) — 터미널 UI (패널, 테이블, 마크다운)
- PyYAML — 카드 파싱 + 설정
