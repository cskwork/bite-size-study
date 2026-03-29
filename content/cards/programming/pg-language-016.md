---
id: "pg-language-016"
subject: "PG"
chapter: "Python 프로그래밍"
title: "Python 클래스와 상속"

difficulty: 3
priority: 2
tags: [Python, 클래스, 상속, super, __init__, 다형성, 오버라이딩]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```python
    class Parent:
        def __init__(self):
            self.x = 1
        def f(self):
            self.x += 1

    class Child(Parent):
        def __init__(self):
            super().__init__()
            self.x += 10
        def f(self):
            super().f()
            self.x += 100

    c = Child()
    c.f()
    print(c.x)
    ```
  answer: "112"
---

## Python 클래스와 상속

### 핵심 개념
Python의 클래스는 `class` 키워드로 정의하며, 상속은 `class Child(Parent)` 형태로 선언한다. `__init__`은 생성자 역할을 하며, `super()`로 부모 클래스의 메서드를 호출한다. 메서드 오버라이딩 시 동적 바인딩이 적용된다.

### 키워드
- **class**: 클래스 정의 키워드
- **self**: 인스턴스 자기 자신을 가리키는 참조 (Java의 `this`)
- **__init__(self)**: 생성자. 객체 생성 시 자동 호출
- **super()**: 부모 클래스 참조. `super().__init__()`, `super().f()` 형태
- **상속**: `class Child(Parent):` — 부모의 속성과 메서드를 물려받음
- **다중 상속**: `class C(A, B):` — Python은 다중 상속 허용 (MRO 순서)
- **오버라이딩**: 부모 메서드와 같은 이름으로 자식에서 재정의

### 트레이싱
```
c = Child()
  → Parent.__init__: self.x = 1
  → Child.__init__: self.x = 1 + 10 = 11

c.f()
  → Parent.f (super().f()): self.x = 11 + 1 = 12
  → Child.f: self.x = 12 + 100 = 112

출력: 112
```

### 기본 클래스 구조
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def grade(self):
        if self.score >= 90: return 'A'
        elif self.score >= 80: return 'B'
        else: return 'C'

s = Student("홍길동", 85)
print(s.grade())  # B
```

### 다형성 예시
```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rect(3, 4)]
for s in shapes:
    print(s.area())
# 78.5
# 12
```

### 기출 포인트
> - **출제 패턴**: 부모-자식 클래스 간 메서드 호출 순서와 속성값 변화 추적
> - **핵심**: `super().__init__()` 호출 여부에 따라 부모 속성 초기화 달라짐
> - **주의**: Python의 `self`는 명시적으로 첫 번째 매개변수에 작성해야 함
> - **다중 상속 MRO**: Method Resolution Order에 따라 호출 순서 결정

### 연결 개념
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — Java vs Python 비교)
- 관련 카드: `pg-language-004` (Python 핵심 문법 — 기본 문법)
