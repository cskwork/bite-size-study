---
id: "pg-language-004"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python 핵심 문법"

difficulty: 3
priority: 3
tags: [Python, 슬라이싱, 딕셔너리, 리스트컴프리헨션, 집합연산, 기출빈출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = {k: v for k, v in data.items() if v % 2 == 0}
    print(result)
    ```
  answer: "{'b': 2, 'd': 4}"
---

## Python 핵심 문법

### 핵심 개념
Python의 슬라이싱, 딕셔너리, 컴프리헨션은 정보처리기사 실기에서 매회 1~2문항 출제되는 핵심 주제다. 슬라이싱은 `[start:end:step]` 형식으로 원본을 변경하지 않고 새 객체를 반환한다. 딕셔너리 컴프리헨션과 집합 연산(&, |, -)은 코드 추적 문제의 핵심 포인트다.

### 키워드
- **슬라이싱 `[start:end:step]`**: end 인덱스는 미포함. `[::-1]`은 역순
- **dict.keys()**: 키 목록 반환 (dict_keys 타입)
- **dict.values()**: 값 목록 반환
- **dict.items()**: (키, 값) 튜플 쌍 반환
- **리스트 컴프리헨션**: `[표현식 for 변수 in 반복가능 if 조건]`
- **딕셔너리 컴프리헨션**: `{k: v for k, v in ...}`
- **집합 연산**: `&` 교집합, `|` 합집합, `-` 차집합

### 슬라이싱 예시
```python
s = "abcdefg"
s[2:5]    # 'cde'   (인덱스 2,3,4)
s[::2]    # 'aceg'  (0,2,4,6)
s[::-1]   # 'gfedcba' (역순)
s[-3:]    # 'efg'   (뒤에서 3개)

lst = [10, 20, 30, 40, 50]
lst[1:4]  # [20, 30, 40]
```

### 딕셔너리 + 집합 연산 예시
```python
# 딕셔너리 컴프리헨션
nums = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in nums if x % 2 != 0}
# {1: 1, 3: 9, 5: 25}

# 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)  # {3, 4}   교집합
print(a | b)  # {1,2,3,4,5,6} 합집합
print(a - b)  # {1, 2}   차집합
```

### 리스트 주요 메서드
```python
lst = [3, 1, 4, 1, 5]
lst.append(9)    # 끝에 추가
lst.insert(0, 7) # 인덱스 0에 삽입
lst.remove(1)    # 값 1 첫 번째 항목 삭제
lst.pop()        # 마지막 요소 제거 후 반환
lst.sort()       # 오름차순 정렬 (원본 변경)
sorted(lst)      # 정렬된 새 리스트 반환 (원본 유지)
```

### 기출 포인트
> - **2025-2회**: 딕셔너리 컴프리헨션 + 집합 교집합(&) 혼합 문제. `items()`로 순회하며 조건 필터링한 결과 출력
> - **2025-3회**: 딕셔너리와 리스트를 함께 활용하는 연산 문제. 중첩 딕셔너리 접근 포함
> - **출제 패턴**: 코드 실행 결과 추적. 슬라이싱 인덱스 계산, 컴프리헨션 필터 조건이 핵심

### 연결 개념
- 관련 카드: `pg-algorithm-001` (정렬 알고리즘 — sorted, list.sort 비교)
- 관련 카드: `pg-data-structure-001` (스택과 큐 — Python deque 활용)
