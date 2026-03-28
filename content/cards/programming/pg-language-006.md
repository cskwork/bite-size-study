---
id: "pg-language-006"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 인터페이스와 추상클래스"

difficulty: 3
priority: 2
tags: [Java, 인터페이스, 추상클래스, interface, abstract, implements, 다형성]
quiz:
  type: "choice"
  question: |
    다음 중 Java 인터페이스(interface)에 대한 설명으로 옳지 않은 것은?
    ① 인터페이스는 다중 구현(implements)이 가능하다.
    ② 인터페이스의 모든 메서드는 기본적으로 public abstract이다.
    ③ 인터페이스는 인스턴스 변수(필드)를 가질 수 있다.
    ④ Java 8부터 default 메서드로 구현을 포함할 수 있다.
  answer: "③ — 인터페이스의 필드는 public static final(상수)만 허용됨"
---

## Java 인터페이스와 추상클래스

### 핵심 개념
인터페이스(interface)는 메서드 시그니처만 정의하는 순수 추상 타입으로, 클래스가 `implements`로 구현한다. 추상클래스(abstract class)는 일반 메서드와 추상 메서드를 모두 가질 수 있으며 `extends`로 상속한다. 인터페이스는 다중 구현이 가능하지만, 클래스 상속은 단일 상속만 허용된다.

### 키워드
- **interface**: 인터페이스 선언. 메서드는 기본적으로 `public abstract`
- **implements**: 클래스가 인터페이스를 구현할 때 사용
- **abstract class**: 추상 메서드를 1개 이상 포함하는 클래스. 인스턴스화 불가
- **abstract 메서드**: 선언만 있고 구현 없는 메서드. 자식에서 반드시 오버라이딩
- **default 메서드**: Java 8+에서 인터페이스에 기본 구현 제공 가능
- **다중 구현**: 클래스는 여러 인터페이스를 동시에 implements 가능

### 인터페이스 vs 추상클래스 비교

| 구분 | interface | abstract class |
|------|-----------|----------------|
| 키워드 | interface / implements | abstract class / extends |
| 다중 상속 | 가능 (다중 implements) | 불가 (단일 extends) |
| 필드 | public static final (상수)만 | 일반 필드 가능 |
| 메서드 | public abstract (default/static 가능) | 일반 + abstract 혼용 |
| 생성자 | 없음 | 있음 (직접 인스턴스화는 불가) |
| 목적 | 행위 규약(Can-do) | 공통 기능 공유(Is-a) |

### 코드 예시
```java
// 인터페이스 정의
interface Flyable {
    void fly();  // public abstract 자동 적용
    default void land() {
        System.out.println("착지");
    }
}

interface Swimmable {
    void swim();
}

// 다중 implements
class Duck implements Flyable, Swimmable {
    @Override
    public void fly() { System.out.println("오리 날기"); }
    @Override
    public void swim() { System.out.println("오리 수영"); }
}
```

### 추상클래스 예시
```java
abstract class Shape {
    String color;  // 일반 필드 허용

    Shape(String color) { this.color = color; }  // 생성자 허용

    abstract double area();  // 추상 메서드 — 반드시 오버라이딩

    void printColor() {  // 일반 메서드 — 그대로 상속
        System.out.println("색상: " + color);
    }
}

class Circle extends Shape {
    double radius;
    Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    @Override
    double area() { return Math.PI * radius * radius; }
}
```

### 기출 포인트
> - **2024-2회**: 인터페이스 구현 문제 — 홀수/짝수 판별 인터페이스를 implements하여 합 계산. `implements` 키워드와 메서드 오버라이딩 필수
> - **2025-3회**: `implements` 키워드 사용 여부 및 인터페이스 메서드 구현 코드 출력 추적
> - **출제 패턴**: 인터페이스 구현 클래스의 메서드 호출 결과 쓰기, 또는 interface/abstract class 차이 선다형
> - **핵심 구분**: interface는 `implements` + 다중 가능, abstract class는 `extends` + 단일만

### 연결 개념
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — extends, 동적 바인딩)
- 관련 카드: `pg-language-002` (Java 접근 제어자)
