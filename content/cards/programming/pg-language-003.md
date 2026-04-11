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

### 왜 배우나
Dog, Cat, Cow, Bird 같은 클래스를 따로따로 만든다고 해 보자. 클래스란 객체를 찍어내는 설계도다. "이름, 나이, 먹기, 걷기"처럼 공통된 부분을 매번 복사해서 붙여야 한다. 나중에 "먹기"를 고쳐야 하면 모든 클래스를 다 찾아다니며 수정해야 한다.

상속은 "공통 부분은 부모 설계도에 한 번만 써 두고, 자식들은 그걸 물려받자"는 아이디어다. 자식은 부모에게서 물려받은 것을 그대로 쓰거나, 필요할 때 자기 방식대로 덮어쓴다. 덮어쓰는 동작이 오버라이딩이다. 이 두 가지를 위해 `extends`와 `@Override`가 준비되어 있다.

### 핵심 개념
상속(Inheritance)은 부모 클래스의 변수와 메서드를 자식 클래스가 물려받는 문법이다. 메서드란 클래스가 가진 기능 하나를 말한다. `extends` 키워드로 "누구의 자식인지"를 알려 준다. Java는 부모를 하나만 둘 수 있다(단일 상속).

오버라이딩(Overriding)은 물려받은 메서드를 자식이 다시 정의하는 것이다. 이름, 매개변수, 반환형이 부모와 똑같아야 한다. `@Override`를 붙이면 컴파일러가 이걸 맞게 썼는지 검사해 준다. 컴파일러는 사람이 쓴 코드를 실행 파일로 바꿔 주는 도구다.

여기서 중요한 포인트가 하나 있다. 인스턴스 메서드는 동적 바인딩을 따른다. 실행 중에 실제로 어떤 객체인지를 보고 어느 메서드를 부를지 결정한다는 뜻이다. 반면 static 메서드와 필드는 정적 바인딩이다. 변수에 적힌 타입만 보고 결정한다. 필드는 클래스가 가진 변수를 말한다.

### 시각화
```
상속 구조:

┌─────────────┐
│   Animal    │  ← 부모 클래스
│ sound(): "…"│
│ speak()     │
└──────┬──────┘
       │ extends (물려받기)
       ▼
┌─────────────┐
│    Dog      │  ← 자식 클래스
│ sound(): "멍멍"│  ← @Override (덮어쓰기)
└─────────────┘

동적 바인딩 흐름:

  Animal a = new Dog();
  a.speak();

  speak() 안에서 sound() 를 호출
       │
       ▼
  a 의 실제 타입은 Dog
       │
       ▼
  Dog 의 sound() 가 실행 → "멍멍"
```

### 이웃 개념 구분
- **오버라이딩 vs 오버로딩**: 오버라이딩은 부모의 메서드를 자식이 다시 정의. 오버로딩은 같은 이름의 메서드를 매개변수만 다르게 여러 개 만드는 것.
- **동적 바인딩 vs 정적 바인딩**: 인스턴스 메서드는 실제 객체 타입으로 결정(동적). static 메서드는 변수 선언 타입으로 결정(정적).

### 키워드
- **extends**: 클래스 상속을 선언하는 키워드. Java는 부모 하나만 상속 가능
- **super()**: 부모 생성자를 호출. 생성자는 객체가 만들어질 때 처음 실행되는 초기화 코드. 자식 생성자의 첫 줄에서만 쓸 수 있다
- **super.메서드()**: 부모가 원래 가지고 있던 메서드를 대놓고 호출하고 싶을 때 사용
- **@Override**: 오버라이딩이라는 걸 표시하는 어노테이션. 어노테이션은 코드에 붙이는 보조 메모다. 이름이나 매개변수를 잘못 썼을 때 컴파일러가 잡아 준다
- **동적 바인딩(Dynamic Binding)**: 프로그램 실행 중에 실제 객체 타입을 보고 메서드를 결정
- **정적 바인딩(Static Binding)**: 코드를 컴파일할 때 참조 변수의 타입만 보고 메서드를 결정

### 생성자 호출 순서
```
자식 객체를 만들 때: 부모 생성자 → 자식 생성자 (위에서 아래로)
```

```java
class Parent {
    Parent() { System.out.print("P "); }
}
class Child extends Parent {
    Child() {
        super(); // 생략해도 자동으로 들어감
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
obj.staticMethod();    // "A-static"   ← 정적 바인딩 (참조 타입 A 기준)
obj.instanceMethod();  // "B-instance" ← 동적 바인딩 (실제 타입 B 기준)
```

### 스스로 가르쳐보기
상속과 오버라이딩을 처음 듣는 친구에게 설명한다면 어떻게 말하시겠어요? 가족이 물려받는 물건, 설계도, 레시피 같은 비유 하나로 한 문장 정의를 만들어 보세요.

**체크포인트** — 아래를 말로 풀어 설명할 수 있는지 확인해 보세요.
- `Animal a = new Dog();`에서 `a.speak()`가 왜 Dog의 `sound()`를 부르게 되는지
- static 메서드 호출이 인스턴스 메서드와 다르게 동작하는 이유
- 자식 객체를 만들 때 부모 생성자가 먼저 실행되는 이유
- `@Override`를 빼도 동작은 같은데 왜 굳이 붙이는지

### 기출 포인트
> - **2025-1회**: `Animal a = new Dog()` 형태에서 `speak()` 안의 `sound()`가 Dog의 것으로 동적 바인딩. 출력값 쓰기
> - **2025-2회**: static 메서드는 참조 변수 타입 기준으로 바인딩(5P). `A obj = new B()`이면 A의 static 메서드가 불린다
> - **2024-2회**: 재귀 + 오버라이딩 혼합 문제. 역순(dcba) 출력 추적
> - **출제 패턴**: 코드를 주고 출력값을 쓰는 유형. 참조 타입과 실제 타입을 반드시 구분할 것

### 연결 개념
- 관련 카드: `pg-language-006` (인터페이스와 추상클래스)
- 관련 카드: `pg-language-002` (Java 접근 제어자)
