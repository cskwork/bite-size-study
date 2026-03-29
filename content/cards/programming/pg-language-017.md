---
id: "pg-language-017"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python 문자열 메서드"

difficulty: 3
priority: 3
tags: [Python, 문자열, split, join, replace, find, upper, lower, 기출빈출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    s = "apple,banana,cherry"
    a = s.split(",")
    b = "-".join(a)
    c = b.replace("banana", "grape")
    print(c)
    ```
  answer: "apple-grape-cherry"
---

## Python 문자열 메서드

### 핵심 개념
Python 문자열은 **불변(immutable)**이며, 모든 문자열 메서드는 원본을 변경하지 않고 **새로운 문자열을 반환**한다. split, join, replace는 가장 빈출되는 메서드이며, 메서드 체인으로 연속 호출하는 출력 추적이 핵심이다.

### 키워드
- **split(구분자)**: 구분자로 분리 → 리스트 반환. `"a,b,c".split(",")` → `['a','b','c']`
- **join(리스트)**: 리스트를 구분자로 결합. `"-".join(['a','b'])` → `"a-b"`
- **replace(old, new)**: 모든 old를 new로 치환. `"aab".replace("a","x")` → `"xxb"`
- **find(str)**: str의 첫 번째 인덱스 반환. 없으면 -1
- **upper() / lower()**: 대소문자 변환
- **strip()**: 양쪽 공백 제거 (lstrip, rstrip은 한쪽만)
- **count(str)**: str의 등장 횟수
- **startswith(str) / endswith(str)**: 접두사/접미사 확인 (bool)

### 트레이싱
```
s = "apple,banana,cherry"
split(",") → ['apple', 'banana', 'cherry']
"-".join(...)  → "apple-banana-cherry"
replace("banana", "grape") → "apple-grape-cherry"
```

### 슬라이싱과 문자열 메서드 혼합
```python
s = "Hello World"
print(s[0:5])         # Hello
print(s.upper())      # HELLO WORLD
print(s.lower())      # hello world
print(s.find("World"))# 6
print(s.count("l"))   # 3
```

### f-string (포맷팅)
```python
name = "홍길동"
score = 95
print(f"{name}: {score}점")  # 홍길동: 95점

# 자릿수 지정
pi = 3.141592
print(f"{pi:.2f}")  # 3.14
```

### strip 활용
```python
s = "  Hello  "
print(s.strip())   # "Hello"
print(s.lstrip())  # "Hello  "
print(s.rstrip())  # "  Hello"
```

### 기출 포인트
> - **매회 출제**: split → join → replace 등 메서드 체인 결과 추적
> - **출제 패턴**: 문자열 조작 후 출력값 쓰기. 인덱싱/슬라이싱과 혼합 출제
> - **핵심**: split은 리스트 반환, join은 문자열 반환. 반환 타입에 주의
> - **주의**: replace는 **모든** 매칭을 치환 (첫 번째만이 아님)

### 연결 개념
- 관련 카드: `pg-language-014` (Java String 메서드 — substring, charAt 비교)
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 슬라이싱)
