---
id: "pg-language-002"
subject: "PG"
chapter: "language"
title: "Java 접근 제어자"

difficulty: 3
priority: 1
tags: [Java, 접근제어자, public, protected, default, private, 캡슐화]
quiz:
  type: "choice"
  question: "Java에서 같은 패키지 내의 클래스와 다른 패키지의 자식 클래스에서 접근 가능한 접근 제어자는?\n(1) private\n(2) default\n(3) protected\n(4) public"
  answer: "(3) protected — protected는 같은 패키지 + 다른 패키지의 상속받은 자식 클래스에서 접근 가능하다."
---

## Java 접근 제어자

### 핵심 개념
Java의 접근 제어자(Access Modifier)는 클래스, 변수, 메서드의 **접근 범위를 제한**하여 캡슐화(Encapsulation)를 구현한다. 4가지 접근 제어자는 접근 범위가 좁은 순서대로 private < default < protected < public이며, 각각의 접근 허용 범위를 정확히 구분하는 것이 핵심이다.

### 키워드
- **public**: 모든 클래스에서 접근 가능. 접근 제한 없음
- **protected**: 같은 패키지 + 다른 패키지의 자식 클래스(상속 관계)에서 접근 가능
- **default(패키지 접근)**: 접근 제어자를 명시하지 않으면 default. 같은 패키지 내에서만 접근 가능
- **private**: 같은 클래스 내에서만 접근 가능. 가장 좁은 범위. getter/setter를 통해 간접 접근
- **캡슐화**: 멤버 변수는 private으로 선언하고, public 메서드(getter/setter)로 접근하는 것이 객체지향 원칙

### 기출 포인트
> 접근 범위를 표로 정리하여 암기할 것: private(같은 클래스), default(같은 패키지), protected(같은 패키지 + 자식 클래스), public(모든 곳). 특히 **protected와 default의 차이**가 핵심 출제 포인트로, protected는 "다른 패키지의 자식 클래스"에서도 접근 가능하다는 점이 default와의 유일한 차이이다. default는 키워드가 아니라 아무 제어자도 붙이지 않은 상태를 의미한다는 점도 주의.

### 연결 개념
- 관련 카드: `pg-language-001` (C언어 포인터 기초)
- 관련 카드: `pg-language-003` (Java 클래스와 상속)
