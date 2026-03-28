---
id: "se-design-001"
subject: "SE"
chapter: "design"
title: "디자인패턴 - GoF 생성패턴 5가지"

difficulty: 3
priority: 3
tags: [디자인패턴, GoF, 생성패턴, 객체지향]
quiz:
  type: "blank"
  question: "GoF 생성패턴 5가지: Abstract Factory, Builder, ______, Prototype, Singleton"
  answer: "Factory Method"
---

## 디자인패턴 - GoF 생성패턴 5가지

### 핵심 개념
GoF(Gang of Four) 디자인패턴은 생성(Creational), 구조(Structural), 행위(Behavioral) 3가지로 분류된다. **생성패턴**은 객체 생성 메커니즘을 다루며, 시스템이 어떤 구체 클래스를 사용하는지 감추고 객체 생성의 유연성을 높인다. 생성패턴 5가지는 암기 필수 항목이다.

### 키워드
- **Abstract Factory**: 관련된 객체군(family)을 생성하는 인터페이스 제공. 구체 팩토리를 교체하면 제품군 전체가 바뀜
- **Builder**: 복잡한 객체의 생성 과정과 표현을 분리. 동일한 생성 절차로 다른 표현 결과를 만듦
- **Factory Method**: 객체 생성을 서브클래스에 위임. 상위 클래스는 인터페이스만 정의하고 하위 클래스가 구체 클래스를 결정
- **Prototype**: 기존 객체를 복제(clone)하여 새 객체를 생성. 생성 비용이 클 때 유용
- **Singleton**: 클래스의 인스턴스를 하나만 생성하고 전역 접근점을 제공

### 기출 포인트
> 암기법: **"AB를 FPS로 만든다"** (Abstract Factory, Builder, Factory Method, Prototype, Singleton). 생성패턴은 총 5개, 구조패턴 7개(어댑터, 브리지, 컴포지트, 데코레이터, 퍼사드, 플라이웨이트, 프록시), 행위패턴 11개이다. 패턴 이름과 분류를 정확히 매칭하는 문제가 자주 출제된다.

### 연결 개념
- 관련 카드: `se-requirements-001`
- 관련 카드: `se-architecture-001`
