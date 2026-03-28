---
id: "pg-language-003"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 상속과 오버라이딩"

difficulty: 3
priority: 3
tags: [Java, 상속, 오버라이딩, 동적바인딩, extends, super, Override]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    class Animal {
        String sound() { return "..."; }
        void speak() { System.out.println(sound()); }
    }
    class Dog extends Animal {
        @Override
        String sound() { return "멍멍"; }
    }
    public class Main {
        public static void main(String[] args) {
            Animal a = new Dog();
            a.speak();
        }
    }
    ```
  answer: "멍멍"
---

## Java 상속과 오버라이딩

### 핵심 개념
상속(extends)은 부모 클래스의 필드와 메서드를 자식 클래스가 물려받는 메커니즘이다. 오버라이딩(@Override)은 부모의 메서드를 자식이 재정의하는 것으로, 인스턴스 메서드는 **동적 바인딩**에 의해 실제 객체 타입의 메서드가 호출된다. 반면 static 메서드와 필드는 **정적 바인딩**으로 참조 변수의 타입 기준으로 결정된다.

### 키워드
- **extends**: 클래스 상속 선언 키워드. Java는 단일 상속만 허용
- **super()**: 부모 클래스 생성자 호출. 자식 생성자의 첫 줄에서만 사용 가능
- **super.메서드()**: 부모의 오버라이딩된 메서드를 명시적으로 호출
- **@Override**: 오버라이딩 어노테이션. 컴파일러가 시그니처를 검증함
- **동적 바인딩**: 런타임에 실제 객체 타입으로 메서드를 결정 (instance 메서드)
- **정적 바인딩**: 컴파일 타임에 참조 변수 타입으로 결정 (static 메서드, 필드)

### 생성자 호출 순서
```
자식 객체 생성 시: 부모 생성자 → 자식 생성자 (위에서 아래로)
```

```java
class Parent {
    Parent() { System.out.print("P "); }
}
class Child extends Parent {
    Child() {
        super(); // 생략 시 자동 삽입
        System.out.print("C ");
    }
}
// new Child() → 출력: P C
```

### 정적 vs 동적 바인딩 비교
```java
class A {
    static String staticMethod() { return "A-static"; }
    String instanceMethod() { return "A-instance"; }
}
class B extends A {
    static String staticMethod() { return "B-static"; }   // 숨김(hiding)
    @Override
    String instanceMethod() { return "B-instance"; }      // 오버라이딩
}

A obj = new B();
obj.staticMethod();    // "A-static"  ← 정적 바인딩 (참조 타입 기준)
obj.instanceMethod();  // "B-instance" ← 동적 바인딩 (실제 타입 기준)
```

### 기출 포인트
> - **2025-1회**: `Animal a = new Dog()` 형태에서 speak() 내부의 sound()가 Dog의 sound()로 동적 바인딩되어 호출됨 — 출력 결과 추적 문제
> - **2025-2회**: static 메서드는 참조 변수 타입 기준으로 바인딩됨 (5P). `A obj = new B()`에서 static 메서드는 A의 것이 호출됨
> - **2024-2회**: 재귀 + 오버라이딩 혼합 문제. 출력 역순(dcba) 추적 필요
> - **출제 패턴**: 코드 주고 출력값 쓰기. 반드시 참조 타입 vs 실제 타입을 구분해야 함

### 연결 개념
- 관련 카드: `pg-language-006` (인터페이스와 추상클래스)
- 관련 카드: `pg-language-002` (Java 접근 제어자)
