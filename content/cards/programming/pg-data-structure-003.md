---
id: "pg-data-structure-003"
subject: "PG"
chapter: "자료구조"
title: "트리와 이진트리 순회"

difficulty: 3
priority: 2
tags: [트리, 이진트리, 전위순회, 중위순회, 후위순회, BST, 이진탐색트리]
quiz:
  type: "blank"
  question: |
    아래 이진 트리를 후위 순회(Post-order)한 결과를 쓰시오.
    ```
           A
          / \
         B   C
        / \
       D   E
    ```
  answer: "D E B C A"
---

## 트리와 이진트리 순회

### 핵심 개념
이진 트리(Binary Tree)는 각 노드가 최대 2개의 자식(왼쪽, 오른쪽)을 갖는 트리 자료구조다. 순회 방식 세 가지(전위/중위/후위)는 루트(Root)를 언제 방문하느냐로 구분하며, 기출에서는 트리 그림을 주고 특정 순회 결과를 쓰거나, 순회 코드를 추적하여 출력을 맞히는 형태로 출제된다.

### 키워드
- **전위 순회(Pre-order)**: Root → Left → Right
- **중위 순회(In-order)**: Left → Root → Right  ← BST에서 오름차순 출력
- **후위 순회(Post-order)**: Left → Right → Root  ← 수식 트리 계산에 사용
- **이진 탐색 트리(BST)**: 왼쪽 자식 < 루트 < 오른쪽 자식 항상 성립
- **높이(Height)**: 루트에서 가장 깊은 리프까지의 간선 수
- **리프 노드**: 자식이 없는 노드

### 순회 방법 정리
```
트리 예시:
       1
      / \
     2   3
    / \   \
   4   5   6

전위 (R-L-R): 1 2 4 5 3 6
중위 (L-R-R): 4 2 5 1 3 6
후위 (L-R-R): 4 5 2 6 3 1
```

### 재귀 코드로 이해하기
```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    if node is None: return
    print(node.val, end=' ')  # Root 먼저
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node.val, end=' ')  # Root 중간
    inorder(node.right)

def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')  # Root 마지막
```

### 이진 탐색 트리 삽입/탐색
```
삽입 규칙: 루트보다 작으면 왼쪽, 크면 오른쪽으로 이동 반복
탐색 시간복잡도: 평균 O(log n), 최악(편향 트리) O(n)

삽입 순서 [5, 3, 7, 1, 4] 로 만든 BST:
        5
       / \
      3   7
     / \
    1   4
중위 순회 결과: 1 3 4 5 7  (오름차순)
```

### 기출 포인트
> - **2025-1회**: Python으로 이진 트리 구성 후 순회 함수 호출 — 각 순회 결과 값의 합 또는 순서 추적
> - **2025년부터 매회 출제 추세**: 트리 그림 주고 전위/중위/후위 결과 쓰기, 또는 순회 코드 실행 결과 추적
> - **핵심 암기**: 전-중-후의 기준은 "Root가 언제 나오나": 앞(Pre)/가운데(In)/뒤(Post)
> - **BST 중위 순회 = 오름차순**: 이 성질을 이용한 정렬 관련 문제도 출제됨

### 연결 개념
- 관련 카드: `pg-data-structure-001` (스택과 큐 — DFS/BFS 구현에 활용)
- 관련 카드: `pg-algorithm-002` (탐색 알고리즘 — DFS, BFS, 이진탐색)
- 관련 카드: `pg-data-structure-002` (연결 리스트 — 트리 노드 구조 기반)
