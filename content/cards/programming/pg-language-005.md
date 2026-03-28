---
id: "pg-language-005"
subject: "PG"
chapter: "C언어 프로그래밍"
title: "C언어 구조체와 이중 포인터"

difficulty: 3
priority: 2
tags: [C언어, 구조체, 포인터, 이중포인터, malloc, free, 동적메모리]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```c
    #include <stdio.h>
    struct Point { int x; int y; };
    int main() {
        struct Point p = {3, 7};
        struct Point *ptr = &p;
        printf("%d %d\n", ptr->x, (*ptr).y);
        return 0;
    }
    ```
  answer: "3 7"
---

## C언어 구조체와 이중 포인터

### 핵심 개념
구조체(struct)는 서로 다른 타입의 데이터를 하나의 단위로 묶는 사용자 정의 자료형이다. 포인터로 구조체 멤버에 접근할 때는 `->` 연산자를 사용한다. 이중 포인터(`**pp`)는 포인터의 포인터로, 함수에서 포인터 자체를 변경하거나 2차원 배열을 다룰 때 주로 사용된다.

### 키워드
- **struct**: 구조체 정의 키워드. 다양한 타입을 하나로 묶음
- **->**: 포인터로 구조체 멤버 접근. `ptr->x` == `(*ptr).x`
- **이중 포인터(`**pp`)**: 포인터 변수의 주소를 저장. 역참조 2회 필요
- **malloc(size)**: 힙 영역에 동적 메모리 할당. 실패 시 NULL 반환
- **free(ptr)**: 동적으로 할당된 메모리 해제. 해제 후 ptr = NULL 권장
- **sizeof()**: 자료형 또는 변수의 바이트 크기 반환

### 구조체 기본 사용
```c
struct Student {
    char name[20];
    int score;
};

// 값으로 선언 및 접근
struct Student s1 = {"홍길동", 95};
printf("%s: %d\n", s1.name, s1.score);

// 포인터로 선언 및 접근
struct Student *p = &s1;
printf("%s: %d\n", p->name, p->score);    // -> 사용
printf("%s: %d\n", (*p).name, (*p).score); // * 역참조 후 . 사용
```

### 이중 포인터 예시
```c
int a = 10;
int *p = &a;    // p는 a의 주소
int **pp = &p;  // pp는 p의 주소

printf("%d\n", a);    // 10
printf("%d\n", *p);   // 10  (p 역참조)
printf("%d\n", **pp); // 10  (pp 이중 역참조)

*p = 20;              // a 값 변경
printf("%d\n", **pp); // 20
```

### 구조체 배열과 동적 할당
```c
#include <stdlib.h>

struct Point {
    int x, y;
};

// 구조체 동적 할당
struct Point *arr = (struct Point*)malloc(3 * sizeof(struct Point));
arr[0].x = 1; arr[0].y = 2;
arr[1].x = 3; arr[1].y = 4;

// 포인터 산술로 접근
(arr + 1)->x = 5;  // arr[1].x = 5 와 동일

free(arr);  // 메모리 해제
arr = NULL;
```

### typedef로 구조체 별칭
```c
typedef struct {
    int x, y;
} Point;  // struct 키워드 없이 Point만으로 사용 가능

Point p1 = {1, 2};
Point *ptr = &p1;
printf("%d\n", ptr->x);  // 1
```

### 기출 포인트
> - **2025-2회**: 이중 포인터(`**pp`) + 구조체 배열 혼합 문제. `pp`를 이중 역참조(`**pp`)하거나 `(*pp)->field`로 멤버 접근하는 출력 추적 (5, 6 출력)
> - **2024-3회**: 구조체 신유형 — typedef + 함수 포인터 또는 구조체 내 배열 멤버 접근
> - **주의**: `->` vs `.` 혼동 금지. 포인터일 때는 `->`, 일반 변수일 때는 `.`
> - **malloc 반환값**: `void*` 타입이므로 반드시 해당 타입으로 형변환 후 사용

### 연결 개념
- 관련 카드: `pg-language-001` (C언어 포인터 기초)
- 관련 카드: `pg-data-structure-002` (연결 리스트 — 구조체 포인터 활용)
