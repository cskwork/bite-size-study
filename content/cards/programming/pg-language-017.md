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

### 왜 배우나
가게에서 "사과,바나나,체리"라고 적힌 종이 한 장을 받았다. 이걸 과일 이름별로 정리하려면 쉼표마다 가위질을 해야 한다. 다시 묶으려면 풀칠이 필요하다. 프로그램 속 문자열 가공도 똑같다. 쉼표로 자르기, 하이픈으로 다시 잇기, "바나나"를 "포도"로 갈아끼우기. 이런 작업을 한 줄로 끝내라고 Python이 미리 준비해 둔 도구가 문자열 메서드다. `split()`은 가위, `join()`은 풀, `replace()`는 지우개 겸 펜, `strip()`은 양쪽 공백 털이개라고 기억하면 편하다.

### 핵심 개념
Python 문자열은 **불변(immutable)**이다. 즉 한번 만들어지면 그 내용을 절대 바꿀 수 없다. 모든 문자열 메서드는 원본을 건드리지 않는다. 대신 새로운 문자열(또는 리스트)을 만들어서 돌려준다.

시험에서 가장 자주 나오는 세 메서드는 이것이다.

- **`split(구분자)`**: 문자열을 구분자 기준으로 잘라서 **리스트(list)** 로 돌려준다. 리스트는 여러 값을 순서대로 담는 자료구조다.
- **`join(리스트)`**: 리스트 속 요소들을 구분자로 이어 붙여 **문자열(str)** 로 돌려준다. split과 정반대 방향의 일이다.
- **`replace(old, new)`**: 문자열 속 `old`를 `new`로 바꾼 새 문자열을 돌려준다. 주의할 점은 "처음 하나만"이 아니라 "매칭되는 전부"를 바꾼다는 것이다.

호출 순서 하나 더 기억해 두자. `join`은 구분자 문자열이 주인이다. `"-".join(['a','b'])`처럼 쓴다. 리스트에 점을 찍는 게 아니다. 이 세 메서드를 연달아 붙이는 체인(chain) 형태가 기출 단골이다.

### 시각화
```
┌─ split → join → replace 체인 흐름 ────────────────────┐
│                                                       │
│  "apple,banana,cherry"                                │
│         │                                             │
│         ▼  split(",")                                 │
│  ['apple', 'banana', 'cherry']   ← 리스트(list)       │
│         │                                             │
│         ▼  "-".join(...)                              │
│  "apple-banana-cherry"           ← 문자열(str)        │
│         │                                             │
│         ▼  replace("banana", "grape")                 │
│  "apple-grape-cherry"            ← 새 문자열(str)     │
└───────────────────────────────────────────────────────┘

┌─ join 호출 방식 주의 ─────────────────────────────────┐
│                                                       │
│   ✗  리스트.join(구분자)    ← 틀린 방식               │
│   ✓  구분자.join(리스트)    ← 올바른 방식             │
│                                                       │
│   "-".join(['a','b','c'])  →  "a-b-c"                 │
└───────────────────────────────────────────────────────┘
```

### 이웃 개념 구분
- **split vs join**: split은 문자열을 잘라 리스트로 만들기. join은 리스트를 묶어 문자열로 만들기. 방향이 정반대다.
- **find vs index**: 둘 다 위치를 찾는다. 다만 없을 때 `find()`는 -1을 돌려주고, `index()`는 ValueError를 던진다.
- **strip vs replace**: `strip()`은 양쪽 가장자리의 공백만 털어낸다. `replace(" ", "")`는 가운데 공백까지 전부 없앤다.

### 키워드
- **split(구분자)**: 구분자(separator) 기준으로 문자열을 잘라 리스트(list)로 반환. `"a,b,c".split(",")` → `['a','b','c']`
- **join(리스트)**: 리스트의 요소들을 구분자로 이어 붙여 하나의 문자열로 반환. `"-".join(['a','b'])` → `"a-b"`
- **replace(old, new)**: 모든 old를 new로 치환한 새 문자열 반환. `"aab".replace("a","x")` → `"xxb"`
- **find(str)**: str이 처음 나타나는 인덱스(위치 번호, 0부터 시작)를 반환. 없으면 -1
- **upper() / lower()**: 모든 글자를 대문자/소문자로 변환한 새 문자열 반환
- **strip()**: 양쪽 공백(빈칸, 탭, 줄바꿈)을 제거한 새 문자열 반환. `lstrip()`은 왼쪽만, `rstrip()`은 오른쪽만
- **count(str)**: 문자열 안에서 str이 몇 번 나타나는지 횟수 반환
- **startswith(str) / endswith(str)**: 문자열이 str로 시작/끝나는지 True 또는 False 반환
- **불변(immutable)**: 한번 만들어진 문자열의 내용을 바꿀 수 없는 성질. 메서드는 항상 새 문자열을 만듦

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

### 스스로 가르쳐보기
> Python을 처음 보는 친구에게 split과 join을 "가위와 풀"이 아닌 본인만의 새로운 비유로 설명해 보세요. 이어서 `"apple,banana,cherry"`가 `split → join → replace`를 거치며 어떤 타입으로 바뀌는지 단계별로 짚어 주세요.

체크포인트:
- [ ] split의 반환 타입이 리스트라는 점을 말할 수 있는가
- [ ] join은 구분자 문자열이 주어가 된다는 점을 말할 수 있는가
- [ ] join의 반환 타입이 문자열이라는 점을 말할 수 있는가
- [ ] replace가 매칭된 모든 부분을 바꾼다는 점을 짚었는가

### 기출 포인트
> - **매회 출제**: split → join → replace 등 메서드 체인 결과 추적
> - **출제 패턴**: 문자열 조작 후 출력값 쓰기. 인덱싱/슬라이싱과 혼합 출제
> - **핵심**: split은 리스트 반환, join은 문자열 반환. 반환 타입에 주의
> - **주의**: replace는 **모든** 매칭을 치환 (첫 번째만이 아님)

### 연결 개념
- 관련 카드: `pg-language-014` (Java String 메서드 — substring, charAt 비교)
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 슬라이싱)
