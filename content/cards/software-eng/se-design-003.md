---
id: "se-design-003"
subject: "SE"
chapter: "디자인패턴"
title: "GoF 행위 패턴 11가지"

difficulty: 3
priority: 3
tags: [디자인패턴, GoF, 행위패턴, Observer, Strategy, Command, Iterator, State, TemplateMethod, Visitor, Mediator, Memento, ChainOfResponsibility, Interpreter]
quiz:
  type: "choice"
  question: "다음 중 GoF 행위 패턴이 아닌 것은?\n① Observer  ② Strategy  ③ Facade  ④ Iterator"
  answer: "③ Facade (Facade는 구조 패턴)"
---

## GoF 행위 패턴 11가지

### 핵심 개념
행위 패턴은 객체나 클래스 간의 알고리즘 및 책임 분배에 관한 패턴이다. 객체 간 통신 방식, 알고리즘 캡슐화, 상태 관리 등을 다루며 GoF 3가지 분류 중 패턴 수가 가장 많다(11가지). 시험에서 비중이 가장 높은 분류다.

### 키워드
- **Observer(옵저버)**: 객체 상태 변화 시 의존 객체들에 자동 통지 — "이벤트 구독", 1:N 의존 관계
- **Strategy(전략)**: 알고리즘을 캡슐화하여 교체 가능하게 — "전략 교체", 런타임에 알고리즘 변경
- **Command(커맨드)**: 요청을 객체로 캡슐화하여 실행 취소·재실행 지원 — "명령 객체화"
- **Iterator(이터레이터)**: 컬렉션 내부 구조 노출 없이 순차 접근 — "순회", 내부 표현 독립적 접근
- **State(상태)**: 객체 상태에 따라 행동을 변경 — "상태 기계", 상태별 클래스로 분리
- **Template Method(템플릿 메서드)**: 알고리즘 골격을 상위 클래스에 정의, 세부 구현은 하위 클래스에 위임
- **Visitor(방문자)**: 객체 구조와 연산을 분리하여 새 연산을 쉽게 추가 — "이중 디스패치"
- **Mediator(중재자)**: 객체 간 통신을 중재 객체가 담당 — "통신 집중화", 결합도 감소
- **Memento(메멘토)**: 객체 상태를 외부에 저장하여 이전 상태로 복원 — "스냅샷", Undo 구현
- **Chain of Responsibility(책임 연쇄)**: 요청을 처리할 수 있는 객체를 연쇄적으로 탐색 — "체인"
- **Interpreter(인터프리터)**: 언어의 문법을 클래스로 표현하고 인터프리터 구현

### 기출 포인트
> - 빈출 Top 3: **Iterator**, **Observer**, **Strategy** — 매회 출제 수준
> - **2024-2회**: Iterator 패턴 설명 빈칸 문제 출제
> - 구조 패턴 Facade와 혼동 주의 — Facade는 구조 패턴, State·Strategy는 행위 패턴
> - "알고리즘 교체" → Strategy, "상태에 따른 행동 변화" → State 구분 필수

### 연결 개념
- 관련 카드: `se-design-001` (GoF 생성 패턴)
- 관련 카드: `se-design-002` (GoF 구조 패턴)
