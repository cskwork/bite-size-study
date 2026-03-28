# bite-size-study

뇌과학 기반 정보처리실기 학습 CLI. 하기 싫어도 시스템이 끌고 간다.

## 핵심 원리

| 원리 | 메커니즘 | 시스템 적용 |
|------|----------|------------|
| 마이크로 습관 | 극단적으로 쉽게 시작 | 카드 2-3장 (5분) |
| 5분 규칙 | 자이가르닉 효과 → 자연 지속 | 최소 세션 5분 |
| If-Then 계획 | 결정 피로 제거 (d=0.65) | config.yaml 앵커 |
| 스트릭 | 가시적 진행 = 3.6배 동기 | 캘린더 + 히트맵 |
| 유혹 묶기 | 도파민 연합 학습 | 학습 후 보상 연결 |
| 정체성 전환 | 행동→정체성 루프 (r=0.55) | 세션 시작 메시지 |

## 빠른 시작

```bash
# 의존성 설치
pip install -r requirements.txt

# 학습 시작 (이것만 기억하세요)
python scripts/study.py

# alias 설정 (선택)
echo 'alias s="python ~/Documents/PARA/Resource/bite-size-study/scripts/study.py"' >> ~/.zshrc
source ~/.zshrc
```

## 명령어

```bash
python scripts/study.py              # 오늘의 학습 세션
python scripts/study.py progress     # 전체 진행률
python scripts/study.py cards        # 카드 목록

python scripts/streak.py             # 스트릭 전체 보기
python scripts/streak.py calendar    # 월간 캘린더
python scripts/streak.py heatmap     # 7주 히트맵
```

## 설정 커스터마이징

`config.yaml`에서 조정:
- `session.daily_cards`: 하루 새 카드 수 (기본 3)
- `anchors`: If-Then 트리거 설정
- `identity.message`: 정체성 메시지
- `rewards`: 스트릭별 보상 설정

## 카드 추가

`content/cards/{과목}/` 에 Markdown 파일 추가. `templates/card_template.md` 참고.

과목 코드: SE(소프트웨어 설계), PG(소프트웨어 개발), DB(데이터베이스), NW(시스템 통합), MT(유지보수)
