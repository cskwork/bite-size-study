# Contributing / 기여 가이드

bite-size-study에 기여해 주셔서 감사합니다!

## 기여 방법

### 1. 새 학습 카드 추가 (가장 쉬운 기여)

`content/cards/{subject}/` 에 Markdown 파일을 추가하세요.

```markdown
---
id: "subject-001"
subject: "DB"
title: "카드 제목"
difficulty: 2
priority: 3
quiz:
  type: "blank"
  question: "질문"
  answer: "정답"
---

## 카드 제목

### 핵심 개념
- ...
```

**카드 작성 규칙:**
- `id`는 `{subject}-{number}` 형식 (예: `db-051`)
- `difficulty`: 1(기초), 2(응용), 3(심화)
- `priority`: 3(매회 출제), 2(자주), 1(가끔)
- `quiz.type`: `ox`, `blank`, `choice` 중 하나

### 2. 버그 수정 / 기능 추가

1. 이 저장소를 Fork합니다
2. 새 브랜치를 생성합니다: `git checkout -b feat/my-feature`
3. 변경사항을 커밋합니다: `git commit -m "feat: add my feature"`
4. 브랜치를 Push합니다: `git push origin feat/my-feature`
5. Pull Request를 생성합니다

### 커밋 메시지

[Conventional Commits](https://www.conventionalcommits.org/) 형식을 사용합니다:

- `feat:` 새 기능
- `fix:` 버그 수정
- `docs:` 문서 변경
- `test:` 테스트 추가/수정
- `refactor:` 리팩토링
- `chore:` 빌드, 설정 변경

### 개발 환경 설정

```bash
git clone https://github.com/cskwork/bite-size-study.git
cd bite-size-study
pip install -e ".[dev]"
pytest tests/ -v
```

### 테스트

모든 PR은 테스트를 통과해야 합니다.

```bash
pytest tests/ -v --cov=bite_size_study --cov-report=term-missing
```

## 행동 강령

[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)를 참고하세요.

## 질문이 있으시면

[Issues](https://github.com/cskwork/bite-size-study/issues)에 질문을 남겨주세요.
