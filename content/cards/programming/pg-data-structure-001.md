---
id: "pg-data-structure-001"
subject: "PG"
chapter: "data-structure"
title: "스택과 큐 (Stack & Queue)"
difficulty: 1
tags: [스택, 큐, LIFO, FIFO, 자료구조]
quiz:
  type: "ox"
  question: "스택(Stack)은 FIFO(First In First Out) 구조이다."
  answer: "X — 스택은 LIFO(Last In First Out) 구조이다. FIFO는 큐(Queue)의 특성이다."
---

## 스택과 큐 (Stack & Queue)

### 핵심 개념
스택(Stack)은 **후입선출(LIFO: Last In First Out)** 구조로, 가장 나중에 삽입된 데이터가 가장 먼저 삭제된다. 큐(Queue)는 **선입선출(FIFO: First In First Out)** 구조로, 가장 먼저 삽입된 데이터가 가장 먼저 삭제된다. 두 자료구조 모두 선형 자료구조이며, 배열 또는 연결 리스트로 구현할 수 있다.

### 키워드
- **스택 연산**: push(삽입), pop(삭제), peek/top(최상위 원소 확인), isEmpty(공백 확인)
- **큐 연산**: enqueue(삽입), dequeue(삭제), front(맨 앞 원소 확인), rear(맨 뒤 위치)
- **스택 활용**: 함수 호출 관리(콜 스택), 후위 표기법 계산, 괄호 검사, DFS(깊이 우선 탐색), Undo 기능
- **큐 활용**: 프로세스 스케줄링(Ready Queue), BFS(너비 우선 탐색), 버퍼(Buffer), 대기열 관리
- **오버플로/언더플로**: 가득 찬 상태에서 삽입 시 오버플로, 빈 상태에서 삭제 시 언더플로 발생

### 기출 포인트
> 스택과 큐의 LIFO/FIFO 구분은 가장 기본적인 출제 포인트이다. 스택 = LIFO, 큐 = FIFO를 반드시 구분할 것. 후위 표기법(Postfix) 연산에서 스택을 활용하는 과정과, 중위(Infix) -> 후위 변환 문제가 빈출된다. 또한 원형 큐(Circular Queue)에서 front와 rear 포인터 계산 문제도 자주 출제된다.

### 연결 개념
- 관련 카드: `pg-data-structure-002` (연결 리스트)
- 관련 카드: `pg-algorithm-001` (정렬 알고리즘)
