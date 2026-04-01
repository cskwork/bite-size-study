# 정보처리기사 실기 - Java 상속과 다형성 문제 모음

## 핵심 개념 정리

```
Parent p = new Child();
```

- **실제 객체** → Child (메모리에 올라간 본체)
- **참조 타입** → Parent (보는 시각/관점)

| 구분 | 기준 | 설명 |
|------|------|------|
| 메서드 호출 | 실제 객체(Child) | 오버라이딩 했으면 Child꺼 실행 |
| 필드(변수) 접근 | 참조 타입(Parent) | 오버라이딩 개념 없음 |
| 메서드 접근 범위 | 참조 타입(Parent) | Child에만 있는 메서드는 호출 불가 |

---

## 원본 문제: 생성자 체이닝 + 오버라이딩

### 문제
다음 코드의 실행 결과를 쓰시오.

```java
class Parent {
    int x = 100;
    Parent() {
        this(500);
    }
    Parent(int x) {
        this.x = x;
    }
    int getX() {
        return x;
    }
}

class Child extends Parent {
    int x = 4000;
    Child() {
        this(5000);
    }
    Child(int x) {
        super();
    }
    int getX() {
        return x;
    }
}

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.getX());
    }
}
```

### 해설

**생성자 호출 순서:**
1. `new Child()` → `Child()` 진입
2. `Child()` 안의 `this(5000)` → `Child(int x)` 이동 (x=5000)
3. `Child(int x)` 안의 `super()` → `Parent()` 이동
4. `Parent()` 안의 `this(500)` → `Parent(int x)` 이동 (x=500)
5. `Parent(int x)`에서 `this.x = 500` → Parent의 x = 500
6. Child로 돌아와서 필드 `int x = 4000` 초기화 → Child의 x = 4000

**p.getX() 호출:**
- p의 타입은 Parent지만 실제 객체는 Child
- getX()는 Child에서 오버라이딩 → Child의 getX() 실행
- Child의 getX()는 `return x` → Child의 x = 4000

**함정:** Child(int x)의 매개변수 x=5000은 아무데도 안 쓰임!

### 답: `4000`

---

## 변형 1: 필드 vs 메서드 차이 (★★☆☆)

### 문제
다음 코드의 (A), (B) 출력 결과를 각각 쓰시오.

```java
class Parent {
    int x = 10;
    int getX() { return x; }
}

class Child extends Parent {
    int x = 20;
    int getX() { return x; }
}

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.x);       // (A)
        System.out.println(p.getX());  // (B)
    }
}
```

### 해설
- `p.x` → 필드 접근은 **참조 타입(Parent)** 기준 → Parent의 x = 10
- `p.getX()` → 메서드 호출은 **실제 객체(Child)** 기준 → Child의 getX() → Child의 x = 20

**핵심:** 필드와 메서드의 바인딩 기준이 다르다!
- 필드: 컴파일 타임(정적 바인딩) → 참조 타입
- 메서드: 런타임(동적 바인딩) → 실제 객체

### 답: (A) `10` / (B) `20`

---

## 변형 2: super 키워드 함정 (★★★☆)

### 문제
다음 코드의 실행 결과를 쓰시오.

```java
class Parent {
    int x = 100;
    int getX() { return x; }
}

class Child extends Parent {
    int x = 200;
    int getX() { return super.x + this.x; }
}

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.getX());
    }
}
```

### 해설
- `p.getX()` → 실제 객체는 Child → Child의 getX() 실행
- `super.x` → 부모(Parent)의 x = 100
- `this.x` → 자신(Child)의 x = 200
- `100 + 200 = 300`

**핵심:** Child 객체 안에는 Parent의 x와 Child의 x가 **둘 다 존재**한다!
super와 this로 각각 접근 가능.

### 답: `300`

---

## 변형 3: 오버라이딩 안 한 경우 (★★★☆)

### 문제
다음 코드의 실행 결과를 쓰시오.

```java
class Parent {
    int x = 10;
    int getX() { return x; }
}

class Child extends Parent {
    int x = 20;
}

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.println(p.getX());
    }
}
```

### 해설
- `p.getX()` → Child에서 getX()를 오버라이딩 **안 했음**
- 따라서 Parent의 getX()가 그대로 실행됨
- Parent의 getX()는 `return x` → **Parent의 x** = 10

**함정:** Child에 x=20이 있어도, Parent의 메서드 안에서의 x는 Parent의 x를 가리킨다!
오버라이딩이 없으면 부모 메서드가 부모 필드를 읽는다.

### 답: `10`

---

## 변형 4: 생성자에서 오버라이딩 메서드 호출 - 킬러 문제 (★★★★)

### 문제
다음 코드의 실행 결과를 쓰시오. (출력 두 줄)

```java
class Parent {
    int x = 10;
    Parent() {
        display();
    }
    void display() {
        System.out.println("Parent x = " + x);
    }
}

class Child extends Parent {
    int x = 20;
    void display() {
        System.out.println("Child x = " + x);
    }
}

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        p.display();
    }
}
```

### 해설

**1줄째 출력 - 생성자 단계:**
1. `new Child()` → Child 생성자 호출 (기본 생성자)
2. Child 생성자 첫 줄에 암묵적으로 `super()` 호출 → Parent() 진입
3. Parent() 안에서 `display()` 호출
4. **이때 실제 객체는 Child** → Child의 display() 실행!
5. 하지만! Child의 `int x = 20`은 **아직 초기화 안 됨** (Parent 생성자 실행 중이라)
6. int의 기본값은 0 → `"Child x = 0"` 출력

**2줄째 출력 - main에서 호출:**
1. `p.display()` → 실제 객체는 Child → Child의 display() 실행
2. 이제는 Child의 x = 20이 초기화 완료됨
3. `"Child x = 20"` 출력

**핵심 함정:**
- 부모 생성자에서 오버라이딩된 메서드를 호출하면, 자식 메서드가 실행됨
- 그런데 자식 필드가 아직 초기화 안 된 상태! (기본값 0)
- 이것이 "생성자에서 오버라이딩 메서드 호출하면 안 되는 이유"

### 답:
```
Child x = 0
Child x = 20
```

---

## 시험 대비 체크리스트

- [ ] `Parent p = new Child()` → 필드는 Parent, 메서드는 Child 기준
- [ ] 생성자 호출 순서: 자식 → (super) → 부모 → 다시 자식
- [ ] 오버라이딩 안 하면 부모 메서드가 부모 필드를 읽음
- [ ] super.x / this.x로 부모/자식 필드 각각 접근 가능
- [ ] 부모 생성자에서 오버라이딩 메서드 호출 시 자식 필드는 아직 0 (기본값)
- [ ] 매개변수를 안 쓰는 함정에 주의 (사용 안 되는 변수 추적)
