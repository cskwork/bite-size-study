---
id: "pg-language-012"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 메서드 오버로딩"

difficulty: 3
priority: 2
tags: [Java, 오버로딩, 메서드, 다형성, 시그니처, 기출출제]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    class Calc {
        int add(int a, int b) { return a + b; }
        double add(double a, double b) { return a + b; }
        int add(int a, int b, int c) { return a + b + c; }
    }
    public class Main {
        public static void main(String[] args) {
            Calc c = new Calc();
            System.out.print(c.add(3, 5) + " ");
            System.out.print(c.add(1, 2, 3));
        }
    }
    ```
  answer: "8 6"
---

## Java 메서드 오버로딩

### 핵심 개념
오버로딩(Overloading)은 **같은 이름의 메서드를 매개변수의 타입, 개수, 순서를 다르게** 하여 여러 개 정의하는 것이다. 컴파일 타임에 호출할 메서드가 결정되며(정적 바인딩), 오버라이딩과 구분하는 것이 핵심이다.

### 키워드
- **오버로딩(Overloading)**: 같은 이름, 다른 매개변수 목록. 컴파일 타임 결정
- **오버라이딩(Overriding)**: 같은 이름, 같은 매개변수. 런타임 결정 (동적 바인딩)
- **메서드 시그니처**: 메서드 이름 + 매개변수 타입/개수/순서 (반환 타입은 포함 안 됨)
- **자동 형변환**: `int` → `double` 자동 변환으로 오버로딩 메서드 선택에 영향

### 오버로딩 vs 오버라이딩
| 구분 | 오버로딩(Overloading) | 오버라이딩(Overriding) |
|------|---------------------|---------------------|
| 메서드 이름 | 같음 | 같음 |
| 매개변수 | 다름 (타입/개수/순서) | 같음 |
| 반환 타입 | 무관 | 같거나 하위 타입 |
| 적용 범위 | 같은 클래스 내 | 상속 관계 (부모↔자식) |
| 바인딩 | 정적 (컴파일 타임) | 동적 (런타임) |
| 어노테이션 | 없음 | @Override |

### 오버로딩 조건
```java
// ✅ 올바른 오버로딩
void print(int x) { }
void print(String x) { }          // 매개변수 타입 다름
void print(int x, int y) { }      // 매개변수 개수 다름
void print(String x, int y) { }   // 매개변수 순서/타입 다름

// ❌ 오버로딩 아님 (컴파일 에러)
int print(int x) { return x; }    // 반환 타입만 다르면 안 됨
```

### 자동 형변환 주의
```java
class Example {
    void f(int a) { System.out.print("int"); }
    void f(double a) { System.out.print("double"); }
}

Example e = new Example();
e.f(10);    // "int" — 정확히 매칭
e.f(10.5);  // "double" — 정확히 매칭
e.f('A');   // "int" — char → int 자동 변환 (65)
```

### 생성자 오버로딩
```java
class Student {
    String name;
    int score;
    Student() { this("이름없음", 0); }
    Student(String name) { this(name, 0); }
    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}
```

### 기출 포인트
> - **2025-1회**: 메서드 오버로딩 코드 출력 결과 추적 (답: 4)
> - **출제 패턴**: 매개변수 타입/개수가 다른 동명 메서드 중 어느 것이 호출되는지 추적
> - **핵심 구분**: 오버로딩은 **같은 클래스** 내에서 매개변수가 다른 것, 오버라이딩은 **상속** 관계에서 재정의
> - **주의**: 반환 타입만 다른 것은 오버로딩이 아님

### 연결 개념
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — 오버라이딩과 비교)
- 관련 카드: `pg-language-006` (Java 인터페이스와 추상클래스)
