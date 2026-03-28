---
id: "pg-data-structure-002"
subject: "PG"
chapter: "자료구조"
title: "연결 리스트"

difficulty: 3
priority: 3
tags: [연결리스트, LinkedList, 포인터, 노드, 단일연결리스트, 이중연결리스트, C언어]
quiz:
  type: "blank"
  question: |
    다음 C 코드에서 연결 리스트를 순서대로 순회하여 출력한 결과를 쓰시오.
    (head → 3 → 1 → 4 → 2 → NULL 순서로 연결된 상태)
    ```c
    Node *p = head;
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    ```
  answer: "3 1 4 2"
---

## 연결 리스트

### 핵심 개념
연결 리스트(Linked List)는 노드(데이터 + 포인터)를 동적으로 연결한 자료구조다. 배열과 달리 메모리가 연속적이지 않아 삽입/삭제가 O(1)이지만, 임의 접근은 O(n)이다. 기출에서는 주로 C 구조체 포인터를 이용한 코드를 주고 순회 결과를 추적하는 형식으로 출제된다.

### 키워드
- **노드(Node)**: data 필드 + next 포인터(단일) 또는 prev/next 포인터(이중)
- **head**: 첫 번째 노드를 가리키는 포인터. 리스트의 시작점
- **->**: 포인터로 구조체 멤버 접근 연산자. `p->data` == `(*p).data`
- **단일 연결 리스트**: 한 방향(next)으로만 순회 가능
- **이중 연결 리스트**: prev/next 양방향 순회 가능
- **원형 연결 리스트**: 마지막 노드의 next가 head를 가리킴

### 노드 구조 및 순회
```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// 순회 (head부터 NULL까지)
Node *p = head;
while (p != NULL) {
    printf("%d ", p->data);
    p = p->next;
}
```

### 노드 삽입 (앞에 삽입)
```c
Node *newNode = (Node*)malloc(sizeof(Node));
newNode->data = value;
newNode->next = head;   // 새 노드가 기존 head를 가리킴
head = newNode;          // head를 새 노드로 갱신
```

### 노드 삭제 (특정 노드 삭제)
```c
// target 앞 노드 prev가 있는 경우
prev->next = target->next;  // prev가 target의 다음을 가리킴
free(target);               // target 메모리 해제
```

### 포인터 추적 요령 (기출 핵심)
```
초기 연결: head → [35] → [42] → [11] → [21] → NULL

p = head          → p는 [35] 가리킴
p = p->next       → p는 [42] 가리킴
p = p->next       → p는 [11] 가리킴
...

화살표(→) 따라가며 data 값 순서대로 기록
```

### 기출 포인트
> - **2025-1회**: C 연결 리스트 순회 코드 추적 — 출력 결과 `35421` (각 노드 data 순서대로)
> - **2025-2회**: 연결 리스트 삽입/연결 후 순회 — 출력 `3 1 2` (포인터 재연결 순서 파악 필요)
> - **2024-2회**: 구조체 포인터와 연결 리스트 혼합 신유형. `->` 연산자와 포인터 역참조 구분
> - **주의**: 코드에서 next 포인터가 재할당되는 순서를 반드시 단계별로 추적할 것

### 연결 개념
- 관련 카드: `pg-data-structure-001` (스택과 큐 — 연결 리스트 기반 구현)
- 관련 카드: `pg-language-001` (C언어 포인터 기초)
- 관련 카드: `pg-language-005` (C언어 구조체와 이중 포인터)
