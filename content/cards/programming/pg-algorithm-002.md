---
id: "pg-algorithm-002"
subject: "PG"
chapter: "알고리즘"
title: "탐색 알고리즘 (이진탐색, 해싱, DFS, BFS)"

difficulty: 3
priority: 2
tags: [이진탐색, 해싱, DFS, BFS, 탐색알고리즘, 시간복잡도, 그래프]
quiz:
  type: "blank"
  question: |
    정렬된 배열 [1, 3, 5, 7, 9, 11, 13, 15]에서 이진 탐색으로 값 7을 찾을 때,
    탐색하는 인덱스(mid)를 순서대로 쓰시오. (0-based index 사용)
  answer: "3 (mid=3, arr[3]=7 → 탐색 완료, 1회만에 발견)"
---

## 탐색 알고리즘

### 핵심 개념
이진 탐색(Binary Search)은 정렬된 배열에서 중간값과 비교를 반복해 O(log n)으로 탐색한다. DFS(깊이 우선 탐색)는 스택/재귀로 구현하며 한 경로를 끝까지 탐색하고, BFS(너비 우선 탐색)는 큐로 구현하며 가까운 노드부터 단계적으로 탐색한다. 두 방법 모두 그래프/트리 순회에 사용된다.

### 키워드
- **이진 탐색**: 정렬된 배열 필수 조건. mid = (low + high) // 2
- **O(log n)**: 이진 탐색 시간복잡도. 탐색마다 범위 절반으로 축소
- **DFS(깊이 우선)**: 스택(반복) 또는 재귀로 구현. 경로 탐색, 사이클 감지에 적합
- **BFS(너비 우선)**: 큐(Queue)로 구현. 최단 경로 탐색에 적합
- **해싱(Hashing)**: 해시 함수로 키를 인덱스로 변환. 평균 O(1) 탐색
- **충돌(Collision)**: 다른 키가 같은 해시값. 체이닝/개방 주소법으로 해결

### 이진 탐색 구현
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid          # 발견
        elif arr[mid] < target:
            low = mid + 1       # 오른쪽 절반 탐색
        else:
            high = mid - 1      # 왼쪽 절반 탐색
    return -1  # 미발견

# 예시: [1,3,5,7,9] 에서 9 탐색
# mid=2(5) → 9>5 → low=3
# mid=4(9) → 발견! 인덱스 4 반환
```

### DFS vs BFS 비교
```
그래프:
    1
   / \
  2   3
 / \
4   5

DFS (스택/재귀): 1 → 2 → 4 → 5 → 3  (깊이 우선)
BFS (큐):       1 → 2 → 3 → 4 → 5  (레벨 순서)
```

### DFS 구현 (재귀)
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### BFS 구현 (큐)
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 탐색 알고리즘 시간복잡도 비교

| 알고리즘 | 평균 | 최악 | 전제 조건 |
|---------|------|------|---------|
| 순차 탐색 | O(n) | O(n) | 없음 |
| 이진 탐색 | O(log n) | O(log n) | 정렬된 배열 |
| 해시 탐색 | O(1) | O(n) | 해시 테이블 |
| DFS/BFS | O(V+E) | O(V+E) | 그래프 |

### 기출 포인트
> - **2025년부터 이진탐색 신규 출제**: 정렬된 배열에서 mid 인덱스 추적 또는 탐색 횟수 계산 문제
> - **비트연산 결합 문제**: `mid = (low + high) >> 1` (비트 오른쪽 시프트 = //2) 형태로 출제
> - **DFS/BFS 출력 순서**: 인접 리스트 순서에 따라 방문 순서가 달라짐 — 코드에서 neighbors 순서 확인 필수
> - **BFS = 최단경로**: 가중치 없는 그래프에서 BFS로 찾은 경로가 최단 경로

### 연결 개념
- 관련 카드: `pg-algorithm-001` (정렬 알고리즘 — 이진 탐색 전제인 정렬 필요)
- 관련 카드: `pg-data-structure-001` (스택과 큐 — DFS/BFS 구현 기반 자료구조)
- 관련 카드: `pg-data-structure-003` (트리 — DFS/BFS를 트리 순회에 적용)
