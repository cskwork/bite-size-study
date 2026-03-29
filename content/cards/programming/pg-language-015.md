---
id: "pg-language-015"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 배열과 2차원 배열"

difficulty: 3
priority: 2
tags: [Java, 배열, 2차원배열, 대각선, 반복문, 기출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    public class Main {
        public static void main(String[] args) {
            int[][] a = {{1, 2, 3}, {4, 5, 6}};
            int sum = 0;
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 3; j++) {
                    if (i == j)
                        sum += a[i][j];
                }
            }
            System.out.print(sum);
        }
    }
    ```
  answer: "6"
---

## Java 배열과 2차원 배열

### 핵심 개념
Java 배열은 **같은 타입의 데이터를 연속 저장**하는 참조 타입 객체이다. 크기가 고정되며, `length` 속성으로 크기를 확인한다. 2차원 배열은 `배열의 배열`로 구현되며, 행렬 연산이나 대각선 합 문제가 빈출된다.

### 키워드
- **선언/생성**: `int[] a = new int[5];` 또는 `int[] a = {1,2,3};`
- **length**: 배열 크기. `a.length` (메서드가 아닌 속성)
- **2차원 배열**: `int[][] a = new int[행][열];`
- **가변 배열**: 각 행의 열 수가 다를 수 있음. `int[][] a = new int[3][];`
- **ArrayIndexOutOfBoundsException**: 인덱스 범위 초과 시 발생

### 대각선 합 트레이싱
```
a = {{1, 2, 3},
     {4, 5, 6}}

i==j인 경우:
(0,0) → a[0][0] = 1
(1,1) → a[1][1] = 5
sum = 1 + 5 = 6
```

### 1차원 배열 조작
```java
int[] a = {5, 3, 8, 1, 2};

// 최댓값 찾기
int max = a[0];
for (int i = 1; i < a.length; i++) {
    if (a[i] > max) max = a[i];
}
// max = 8

// 총합
int sum = 0;
for (int x : a) sum += x;  // 향상된 for문
// sum = 19
```

### 2차원 배열 패턴
```java
int[][] a = {{1,2,3}, {4,5,6}, {7,8,9}};

// 행 합
for (int i = 0; i < 3; i++) {
    int rowSum = 0;
    for (int j = 0; j < 3; j++)
        rowSum += a[i][j];
    System.out.print(rowSum + " ");
}
// 6 15 24

// 열 합
for (int j = 0; j < 3; j++) {
    int colSum = 0;
    for (int i = 0; i < 3; i++)
        colSum += a[i][j];
    System.out.print(colSum + " ");
}
// 12 15 18

// 역대각선 합 (i+j==n-1)
int revDiag = 0;
for (int i = 0; i < 3; i++)
    revDiag += a[i][2-i];  // a[0][2]+a[1][1]+a[2][0] = 3+5+7 = 15
```

### 기출 포인트
> - **기출 패턴**: 이중 for문으로 2차원 배열 순회, 조건에 맞는 원소 합/출력
> - **빈출 유형**: 대각선 합 (`i==j`), 역대각선 합 (`i+j==n-1`), 행/열 합
> - **주의**: Java 배열은 0부터 시작. `a.length`는 행 수, `a[0].length`는 0번째 행의 열 수
> - **향상된 for문**: `for (int x : a)` 형태는 읽기 전용 순회에 사용

### 연결 개념
- 관련 카드: `pg-language-007` (C언어 배열과 반복문 — C와 Java 배열 비교)
- 관련 카드: `pg-language-011` (Java 예외처리 — ArrayIndexOutOfBoundsException)
