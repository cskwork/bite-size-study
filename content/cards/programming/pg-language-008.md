---
id: "pg-language-008"
subject: "PG"
chapter: "C언어 프로그래밍"
title: "C언어 재귀 함수"

difficulty: 4
priority: 3
tags: [C언어, 재귀, 팩토리얼, 피보나치, 호출스택, 기출빈출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```c
    #include <stdio.h>
    int f(int n) {
        if (n < 2) return n;
        return f(n-1) + f(n-2);
    }
    int main() {
        printf("%d", f(6));
        return 0;
    }
    ```
  answer: "8"
---

## C언어 재귀 함수

### 핵심 개념
재귀 함수(Recursive Function)는 **자기 자신을 호출하는 함수**이다. 반드시 종료 조건(Base Case)이 필요하며, 호출될 때마다 스택 프레임이 쌓인다. 코드 추적 시 호출 트리를 그려서 반환값을 역추적하는 것이 핵심이다.

### 키워드
- **종료 조건(Base Case)**: 재귀 호출을 멈추는 조건. 없으면 무한 재귀 → 스택 오버플로우
- **재귀 호출(Recursive Case)**: 자기 자신을 호출하여 문제를 분할
- **호출 스택(Call Stack)**: 함수 호출마다 스택 프레임 생성, 반환 시 제거
- **꼬리 재귀(Tail Recursion)**: 재귀 호출이 함수의 마지막 연산인 경우

### 피보나치 트레이싱
```
f(6) = f(5) + f(4)
     = (f(4) + f(3)) + (f(3) + f(2))
     = ((f(3)+f(2)) + (f(2)+f(1))) + ((f(2)+f(1)) + (f(1)+f(0)))
     = ((2+1) + (1+1)) + ((1+1) + (1+0))
     = (3 + 2) + (2 + 1)
     = 5 + 3
     = 8
```

### 팩토리얼 (기본형)
```c
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
// factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
```

### 재귀로 숫자 뒤집기
```c
void reverse(int n) {
    if (n <= 0) return;
    printf("%d", n % 10);  // 마지막 자릿수 출력
    reverse(n / 10);       // 나머지 자릿수 재귀
}
// reverse(1234) → 4321
```

### 재귀로 합계
```c
int sum(int n) {
    if (n == 1) return 1;
    return n + sum(n - 1);
}
// sum(5) = 5+4+3+2+1 = 15
```

### 기출 포인트
> - **2025-1회**: Java 재귀함수 결과 추적 (답: 20). C와 동일한 트레이싱 기법 적용
> - **매회 1~2문항**: 재귀 함수 출력 결과 쓰기는 가장 빈출되는 유형
> - **트레이싱 팁**: 호출 트리를 그려서 종료 조건부터 역으로 계산하면 정확도 향상
> - **주의**: `f(n-1) + f(n-2)` 같은 이중 재귀는 호출 횟수가 기하급수적 증가

### 연결 개념
- 관련 카드: `pg-language-013` (Java 재귀함수 — 동일 패턴, 다른 문법)
- 관련 카드: `pg-data-structure-003` (트리 순회 — 재귀 기반 순회)
