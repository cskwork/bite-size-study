---
id: "pg-language-018"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python 리스트 심화"

difficulty: 3
priority: 2
tags: [Python, 리스트, sort, pop, insert, append, 2차원리스트, 기출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    a = [4, 2, 7, 1, 9]
    a.sort()
    a.pop()
    a.insert(1, 5)
    print(a)
    ```
  answer: "[1, 5, 2, 4, 7]"
---

## Python 리스트 심화

### 핵심 개념
Python 리스트는 **가변(mutable)** 시퀀스로, 다양한 메서드로 원소를 추가·삭제·정렬할 수 있다. **원본을 변경하는 메서드**(sort, append, insert, pop, remove)와 **새 객체를 반환하는 함수**(sorted, reversed)를 구분하는 것이 핵심이다.

### 키워드
- **append(x)**: 끝에 x 추가. 원본 변경
- **insert(i, x)**: 인덱스 i에 x 삽입. 기존 원소는 뒤로 밀림
- **pop()**: 마지막 원소 제거 후 반환. `pop(i)`는 인덱스 i 제거
- **remove(x)**: 값 x의 첫 번째 항목 제거. 없으면 ValueError
- **sort()**: 오름차순 정렬. 원본 변경. `sort(reverse=True)` 내림차순
- **sorted(리스트)**: 정렬된 새 리스트 반환. 원본 유지
- **reverse()**: 원소 순서 뒤집기. 원본 변경
- **extend(리스트)**: 다른 리스트의 모든 원소를 끝에 추가
- **index(x)**: 값 x의 인덱스 반환

### 트레이싱
```
a = [4, 2, 7, 1, 9]
sort()   → [1, 2, 4, 7, 9]     원본 변경, 오름차순
pop()    → [1, 2, 4, 7]        마지막 원소 9 제거
insert(1, 5) → [1, 5, 2, 4, 7] 인덱스 1에 5 삽입
```

### sort() vs sorted()
```python
a = [3, 1, 4, 1, 5]

# sort(): 원본 변경, None 반환
a.sort()
print(a)  # [1, 1, 3, 4, 5]

# sorted(): 원본 유지, 새 리스트 반환
b = [3, 1, 4]
c = sorted(b)
print(b)  # [3, 1, 4] — 원본 그대로
print(c)  # [1, 3, 4] — 새 리스트
```

### 2차원 리스트
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# 행 접근
print(matrix[1])      # [4, 5, 6]
# 원소 접근
print(matrix[1][2])   # 6
# 대각선 합
diag = sum(matrix[i][i] for i in range(3))  # 1+5+9 = 15
```

### 리스트 컴프리헨션 심화
```python
# 짝수만 제곱
a = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# 2차원 리스트 평탄화
matrix = [[1,2], [3,4], [5,6]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6]
```

### 기출 포인트
> - **출제 패턴**: 리스트 메서드 체인 후 최종 상태 출력. sort → pop → insert 순서가 핵심
> - **핵심 구분**: sort()는 원본 변경(None 반환), sorted()는 새 리스트 반환
> - **주의**: pop()은 마지막 원소, pop(0)은 첫 번째 원소 제거
> - **insert(i, x)**: 인덱스 i **앞에** x를 삽입. 기존 원소는 뒤로 이동

### 연결 개념
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 리스트 기본 메서드)
- 관련 카드: `pg-data-structure-001` (스택과 큐 — append/pop으로 스택 구현)
