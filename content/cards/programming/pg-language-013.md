---
id: "pg-language-013"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 재귀함수"

difficulty: 4
priority: 3
tags: [Java, 재귀, 호출스택, 팩토리얼, 피보나치, 기출직접출제]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    public class Main {
        static void f(int n) {
            if (n <= 0) return;
            printf(n % 10);
            f(n / 10);
        }
        static void printf(int x) {
            System.out.print(x);
        }
        public static void main(String[] args) {
            f(1234);
        }
    }
    ```
  answer: "4321"
---

## Java 재귀함수

### 핵심 개념
Java에서 재귀함수는 C와 동일한 원리로 동작하지만, Java 특유의 **메서드 오버라이딩과 결합된 재귀**, **static 메서드 재귀** 등이 출제된다. 호출 스택을 추적할 때 매개변수 값의 변화를 단계별로 기록하는 것이 핵심이다.

### 키워드
- **재귀 호출**: 메서드가 자기 자신을 호출. `static` 메서드에서 주로 출제
- **종료 조건**: `if (n <= 0) return;` 등으로 무한 호출 방지
- **호출 트리**: 재귀 호출 관계를 트리로 시각화하면 추적이 쉬움
- **스택 오버플로우**: 종료 조건 없이 재귀 시 StackOverflowError 발생

### 숫자 뒤집기 트레이싱
```
f(1234):
  print(1234 % 10) → 4    f(1234 / 10) → f(123)
f(123):
  print(123 % 10)  → 3    f(123 / 10)  → f(12)
f(12):
  print(12 % 10)   → 2    f(12 / 10)   → f(1)
f(1):
  print(1 % 10)    → 1    f(1 / 10)    → f(0)
f(0):
  return
→ 출력: 4321
```

### 재귀 합계
```java
static int sum(int n) {
    if (n == 1) return 1;
    return n + sum(n - 1);
}
// sum(10) = 10+9+...+1 = 55
```

### 재귀와 출력 순서
```java
// 재귀 호출 전에 출력하면 → 순방향
static void forward(int n) {
    if (n <= 0) return;
    System.out.print(n + " ");  // 먼저 출력
    forward(n - 1);
}
// forward(3) → 3 2 1

// 재귀 호출 후에 출력하면 → 역방향
static void backward(int n) {
    if (n <= 0) return;
    backward(n - 1);
    System.out.print(n + " ");  // 나중에 출력
}
// backward(3) → 1 2 3
```

### 재귀와 상속 혼합 (고난도)
```java
class A {
    int f(int n) {
        if (n <= 1) return 1;
        return n * f(n - 1);  // 동적 바인딩!
    }
}
class B extends A {
    @Override
    int f(int n) {
        if (n <= 1) return 1;
        return n + f(n - 1);  // 재정의: 곱 → 합
    }
}
A obj = new B();
System.out.print(obj.f(4));  // B의 f 호출: 4+3+2+1 = 10
```

### 기출 포인트
> - **2025-1회**: Java 재귀 메서드 결과 추적 (답: 20). 종료 조건과 반환값 계산이 핵심
> - **2024-2회**: 재귀 + 오버라이딩 혼합. 동적 바인딩으로 어느 클래스의 재귀가 호출되는지 판단
> - **출제 패턴**: `f(n-1)` 형태의 재귀 호출 후 반환값 조합. 출력 위치(전/후)로 순서 결정
> - **트레이싱 팁**: 매개변수 → 조건 체크 → 재귀 호출 → 반환값 순서로 표 작성

### 연결 개념
- 관련 카드: `pg-language-008` (C언어 재귀 함수 — 동일 원리, C 문법)
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — 재귀+오버라이딩 혼합)
