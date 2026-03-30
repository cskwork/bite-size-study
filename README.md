<p align="center">
  <img src="docs/assets/logo.svg" alt="bite-size-study" width="120">
</p>

<h1 align="center">bite-size-study</h1>

<p align="center">
  <strong>뇌과학 기반 마이크로 학습 CLI</strong><br>
  하루 5분, 카드 2장. 하기 싫어도 시스템이 끌고 간다.
</p>

<p align="center">
  <a href="https://github.com/cskwork/bite-size-study/actions/workflows/ci.yml"><img src="https://github.com/cskwork/bite-size-study/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/cskwork/bite-size-study/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cskwork/bite-size-study" alt="License"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/coverage-85%25-brightgreen" alt="Coverage">
</p>

<p align="center">
  <a href="README.en.md">English</a> | <b>한국어</b>
</p>

---

```
$ bite

  Lv.3 (12/51 XP)  |  스트릭: 7일 🔥  |  카드: 28장 학습

  ┌─── bite-size-study ──────────────────────┐
  │  ▸ 학습 시작    오늘의 카드 학습 세션     │
  │    학습 현황    과목별 진행률 확인         │
  │    카드 목록    전체 카드 확인             │
  │    스트릭 통계  XP, 스트릭, 학습일 통계   │
  │    학습 캘린더  월간 학습 캘린더           │
  │    히트맵      최근 7주 학습 히트맵        │
  └── [↑↓] 이동  [Enter] 선택  [q] 종료 ────┘
```

## 왜 bite-size-study인가?

대부분의 학습 도구는 **"많이 하면 잘 된다"** 고 가정한다. 하지만 뇌과학은 정반대를 말한다.

| 원리 | 연구 근거 | 시스템 적용 |
|------|----------|------------|
| **마이크로 습관** | 2분 규칙 (BJ Fogg) | 카드 2--3장, 5분 세션 |
| **간격 반복** | Ebbinghaus 망각 곡선 | 이해도 기반 복습 스케줄링 |
| **스트릭 효과** | 가시적 진행 = 3.6배 동기 부여 | GitHub 잔디 스타일 캘린더 |
| **유혹 묶기** | 도파민 연합 학습 (10--51% 향상) | 학습 후 보상 연결 |
| **If-Then 계획** | 결정 피로 제거 (d=0.65) | 설정 가능한 트리거 앵커 |
| **정체성 전환** | 행동 -> 정체성 루프 (r=0.55) | 세션 시작 메시지 |

> Anki가 **무엇을** 복습할지 정해준다면, bite-size-study는 **시작하게 만든다.**

## 주요 기능

- **인터랙티브 메뉴** -- 화살표 키로 탐색, 한 화면에서 모든 기능 접근
- **퀴즈 시스템** -- OX, 빈칸 채우기, 객관식 3종 퀴즈
- **XP & 레벨** -- 학습할수록 레벨업, 도파민 설계
- **스트릭 추적** -- 연속 학습일 기록 + 보상 연결
- **학습 캘린더** -- GitHub 잔디 스타일 월간 히트맵
- **과목별 진행률** -- 프로그레스 바로 진행 상황 시각화
- **출제빈도 기반** -- priority 태그로 자주 나오는 카드 우선 학습
- **Markdown 카드** -- YAML frontmatter + Markdown으로 카드 작성

## 빠른 시작

```bash
# 설치
pip install bite-size-study

# 또는 소스에서 설치
git clone https://github.com/cskwork/bite-size-study.git
cd bite-size-study
pip install -e .

# 실행
bite
```

## 사용법

```bash
bite              # 인터랙티브 메뉴 (추천)
bite start        # 학습 세션 시작
bite progress     # 과목별 진행률
bite cards        # 전체 카드 목록
bite stats        # 스트릭 통계
bite calendar     # 월간 학습 캘린더
bite heatmap      # 최근 7주 히트맵
bite init         # 새 카드덱 초기화
```

## 나만의 카드 만들기

`content/cards/` 아래에 Markdown 파일을 추가하면 된다.

```markdown
---
id: "my-001"
subject: "DB"
title: "정규화 단계"
difficulty: 2          # 1: 기초, 2: 응용, 3: 심화
priority: 3            # 3: 매회 출제, 2: 자주, 1: 가끔
quiz:
  type: "blank"        # ox, blank, choice
  question: "제2정규형(2NF)은 ___을 제거한 것이다."
  answer: "부분 함수 종속"
---

## 정규화 단계

### 핵심 개념
- 1NF: 원자값
- 2NF: 부분 함수 종속 제거
- 3NF: 이행 함수 종속 제거
- BCNF: 결정자가 모두 후보키
```

### 카드 구조

```
content/cards/
├── db/                # 데이터베이스
├── network/           # 네트워크
├── os/                # 운영체제 & 유지보수
├── programming/       # 프로그래밍
├── software-eng/      # 소프트웨어 공학
└── your-topic/        # 원하는 주제 추가 가능
```

## 설정

`config.yaml`에서 학습 시스템을 커스터마이징할 수 있다.

```yaml
session:
  daily_cards: 3            # 하루 새 카드 수
  max_review_cards: 5       # 하루 최대 복습 카드 수
  min_session_minutes: 5    # 최소 세션 시간

anchors:                    # If-Then 트리거
  - trigger: "아침 커피를 마실 때"
    action: "카드 2장 읽기"

identity:
  message: "나는 매일 성장하는 개발자다."

rewards:                    # 스트릭 보상
  daily: "좋아하는 음료 한 잔"
  streak_7: "좋아하는 콘텐츠 1시간"
  streak_30: "원하던 것 하나 구매"
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
├── content/cards/          # 학습 카드 (50장, 5과목)
├── tests/                  # pytest 테스트 (85% 커버리지)
├── config.yaml             # 학습 시스템 설정
└── pyproject.toml          # 패키지 설정
```

## 기술 스택

| 도구 | 용도 |
|------|------|
| [Typer](https://typer.tiangolo.com/) | CLI 프레임워크 |
| [Rich](https://rich.readthedocs.io/) | 터미널 UI (패널, 테이블, 마크다운) |
| [PyYAML](https://pyyaml.org/) | 카드 파싱 + 설정 |
| [pytest](https://pytest.org/) | 테스트 프레임워크 |

## 기여하기

기여를 환영합니다! [CONTRIBUTING.md](CONTRIBUTING.md)를 참고해 주세요.

새 카드 추가, 버그 수정, 기능 제안 모두 환영합니다.

## 라이선스

[MIT](LICENSE) -- 자유롭게 사용하고 수정하세요.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cskwork/bite-size-study&type=Date)](https://star-history.com/#cskwork/bite-size-study&Date)
