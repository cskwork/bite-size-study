---
id: "pg-language-020"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python 연산자와 형변환"

difficulty: 3
priority: 2
tags: [Python, 연산자, 형변환, 정수나눗셈, 거듭제곱, int, str, float, 기출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    a = "3"
    b = 4
    c = int(a) + b
    d = str(b) + a
    e = float(a) / b
    print(c, d, e)
    ```
  answer: "7 43 0.75"
---

## Python 연산자와 형변환

### 핵심 개념
Python에서 `+` 연산자는 숫자 간에는 덧셈, 문자열 간에는 연결(concatenation)로 동작한다. 서로 다른 타입 간 연산 시 **명시적 형변환**이 필요하며, `//`(정수 나눗셈), `**`(거듭제곱), `%`(나머지) 연산자의 동작을 정확히 이해해야 한다.

### 키워드
- **int(x)**: 정수로 변환. `int("3")` → 3, `int(3.7)` → 3 (소수점 버림)
- **float(x)**: 실수로 변환. `float("3")` → 3.0
- **str(x)**: 문자열로 변환. `str(4)` → "4"
- **//**: 정수 나눗셈 (몫). `10 // 3` → 3
- **%**: 나머지. `10 % 3` → 1
- **\*\***: 거듭제곱. `2 ** 3` → 8
- **/**: 실수 나눗셈. `10 / 3` → 3.333...
- **+**: 숫자 덧셈 또는 문자열 연결
- **\***: 숫자 곱셈 또는 문자열 반복. `"ab" * 3` → "ababab"

### 트레이싱
```
a = "3" (문자열)
b = 4 (정수)
c = int("3") + 4 = 7       (문자열→정수 후 덧셈)
d = str(4) + "3" = "43"    (정수→문자열 후 연결)
e = float("3") / 4 = 0.75  (문자열→실수 후 나눗셈)
출력: 7 43 0.75
```

### 산술 연산자 정리
```python
print(10 + 3)    # 13 (덧셈)
print(10 - 3)    # 7  (뺄셈)
print(10 * 3)    # 30 (곱셈)
print(10 / 3)    # 3.3333... (실수 나눗셈)
print(10 // 3)   # 3  (정수 나눗셈, 몫)
print(10 % 3)    # 1  (나머지)
print(10 ** 3)   # 1000 (거듭제곱)
```

### 문자열과 숫자 혼합
```python
# 문자열 + 숫자 → TypeError
# print("나이: " + 20)  ← 에러!
print("나이: " + str(20))  # 나이: 20 ✓

# 문자열 반복
print("Ha" * 3)  # HaHaHa

# 숫자 문자열 계산
print(int("10") + int("20"))  # 30
print("10" + "20")            # 1020 (연결)
```

### 비교 연산자와 논리 연산자
```python
# 비교
print(5 == 5)    # True
print(5 != 3)    # True
print(5 > 3)     # True
print(5 >= 5)    # True

# 논리
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 조합
x = 15
print(10 < x < 20)  # True (Python 연속 비교)
```

### bool 형변환
```python
# False로 변환되는 값
bool(0)      # False
bool(0.0)    # False
bool("")     # False
bool([])     # False
bool(None)   # False

# 나머지는 모두 True
bool(1)      # True
bool("abc")  # True
bool([1,2])  # True
```

### 기출 포인트
> - **출제 패턴**: 형변환 후 연산 결과 추적. int/str/float 변환이 핵심
> - **빈출 유형**: `str + int` 에러 vs `str(int) + str` 연결, `//` vs `/` 차이
> - **주의**: `int(3.7)` → 3 (내림이 아니라 소수점 버림). 음수: `int(-3.7)` → -3
> - **함정**: `"10" + "20"` = "1020" (문자열 연결), `10 + 20` = 30 (숫자 덧셈)

### 연결 개념
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 슬라이싱, 컴프리헨션)
- 관련 카드: `pg-language-010` (C언어 진수 변환 — printf 서식 비교)
