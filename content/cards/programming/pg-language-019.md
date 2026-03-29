---
id: "pg-language-019"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python lambda와 내장함수"

difficulty: 3
priority: 2
tags: [Python, lambda, map, filter, reduce, 내장함수, 기출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    a = list(map(lambda x: x ** 2, range(1, 6)))
    b = list(filter(lambda x: x > 10, a))
    print(b)
    ```
  answer: "[16, 25]"
---

## Python lambda와 내장함수

### 핵심 개념
lambda는 **이름 없는 한 줄 함수**로, `lambda 매개변수: 표현식` 형태로 작성한다. map, filter 등의 내장함수와 결합하여 리스트를 변환·필터링하는 문제가 출제된다. `range`, `zip`, `enumerate` 등 반복 관련 내장함수도 빈출된다.

### 키워드
- **lambda**: `lambda x: x + 1` — 익명 함수. 단일 표현식만 가능
- **map(함수, 반복가능)**: 각 원소에 함수 적용. `list()`로 변환 필요
- **filter(함수, 반복가능)**: 함수가 True인 원소만 필터링
- **range(start, end, step)**: start부터 end-1까지 정수 시퀀스
- **zip(a, b)**: 두 반복가능 객체를 쌍으로 묶기
- **enumerate(반복가능)**: 인덱스와 값을 함께 반환
- **sum(), min(), max()**: 합계, 최솟값, 최댓값
- **abs()**: 절대값. `abs(-5)` → 5
- **len()**: 길이/크기

### 트레이싱
```
range(1, 6) → [1, 2, 3, 4, 5]
map(lambda x: x**2, ...) → [1, 4, 9, 16, 25]
filter(lambda x: x > 10, ...) → [16, 25]
```

### lambda 기본 사용
```python
# 일반 함수
def add(x, y):
    return x + y

# lambda 동일
add = lambda x, y: x + y
print(add(3, 5))  # 8
```

### map 활용
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]

# 문자열 변환
words = ["hello", "world"]
upper = list(map(str.upper, words))
print(upper)  # ['HELLO', 'WORLD']
```

### filter 활용
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

### zip과 enumerate
```python
names = ["홍길동", "이순신"]
scores = [85, 92]

# zip
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# 홍길동: 85
# 이순신: 92

# enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")
# 0: 홍길동
# 1: 이순신
```

### range 패턴
```python
list(range(5))        # [0, 1, 2, 3, 4]
list(range(1, 6))     # [1, 2, 3, 4, 5]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]
list(range(5, 0, -1)) # [5, 4, 3, 2, 1]
```

### 기출 포인트
> - **출제 패턴**: map/filter + lambda 조합으로 리스트 변환 후 출력 추적
> - **핵심**: map과 filter는 iterator를 반환하므로 `list()`로 변환해야 리스트가 됨
> - **주의**: range(1, 6)은 1~5 (6 미포함). filter 조건이 True인 원소만 남음
> - **reduce**: `from functools import reduce` 필요. 누적 연산

### 연결 개념
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 리스트컴프리헨션)
- 관련 카드: `pg-language-018` (Python 리스트 심화 — 리스트 조작 메서드)
