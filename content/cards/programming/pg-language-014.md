---
id: "pg-language-014"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java String 메서드"

difficulty: 3
priority: 3
tags: [Java, String, substring, charAt, length, indexOf, 문자열, 기출빈출]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    public class Main {
        public static void main(String[] args) {
            String s = "Information";
            System.out.print(s.substring(0, 4));
            System.out.print(s.charAt(5));
            System.out.print(s.length());
        }
    }
    ```
  answer: "Infom11"
---

## Java String 메서드

### 왜 배우나
"2025-01-15"에서 연도만 꺼내고 싶다. "  홍길동  "의 양쪽 빈칸을 털고 싶다. 이메일 주소에서 `@` 뒤만 잘라내고 싶다. 프로그램은 이런 글자 가공 작업을 하루에도 수백 번씩 한다. 글자 하나하나 반복문으로 뜯으면 코드가 길어지고 실수가 많아진다. Java는 String 클래스(문자열 전용 도구 상자)에 자주 쓰는 기능을 메서드(method)로 미리 박아 두었다. `length()`로 글자 수 세기, `substring()`으로 일부 오려내기, `charAt()`으로 특정 위치의 한 글자만 꺼내기.

### 핵심 개념
String은 Java에서 문자열을 다루는 클래스(class)다. 클래스는 "설계도"라고 이해하면 된다.

**가장 큰 특성은 불변(immutable)**이다. 한번 만들어진 문자열의 내용은 절대 바뀌지 않는다. `replace()`나 `substring()`을 호출해도 원본은 그대로다. 대신 바뀐 결과가 담긴 새 문자열이 따로 만들어져 돌아온다.

**인덱스는 0부터 센다.** 인덱스(index)는 문자 한 개의 위치 번호다. `"abc"`에서 a는 0번, b는 1번, c는 2번이다.

**substring(start, end)는 end 미포함이다.** `substring(0, 4)`는 0, 1, 2, 3번 위치까지만 가져간다. 4번 위치는 안 들어간다. 이 규칙이 시험 단골 함정이다.

**문자열 비교는 `==`가 아니라 `equals()`다.** `==`는 "같은 객체(메모리 주소)를 가리키냐"를 묻고, `equals()`는 "글자 내용이 같냐"를 묻는다. `new String("hello")`로 새로 만든 문자열과 기존 `"hello"`를 `==`로 비교하면 false가 나온다. 내용은 같아도 서로 다른 객체이기 때문이다.

### 시각화
```
┌─ "Information" 인덱스 맵 ─────────────────┐
│                                           │
│  위치:  0  1  2  3  4  5  6  7  8  9  10  │
│  글자:  I  n  f  o  r  m  a  t  i  o  n   │
│                                           │
│  substring(0, 4) → I n f o = "Info"       │
│                    ↑─────↑                │
│                  start  end(미포함)        │
│                                           │
│  charAt(5) → 'm'                          │
│  length()  → 11 (글자 수)                  │
└───────────────────────────────────────────┘

┌─ == vs equals 차이 ───────────────────────┐
│                                           │
│  String a = "hello";  ─┐                  │
│  String b = "hello";  ─┤→ 문자열 풀(같은  │
│                        │   객체를 공유)    │
│  a == b  → true                           │
│                                           │
│  String c = new String("hello"); → 별도   │
│  a == c      → false (다른 객체)          │
│  a.equals(c) → true  (내용 동일)          │
└───────────────────────────────────────────┘
```

### 이웃 개념 구분
- **substring vs charAt**: `substring()`은 여러 글자를 잘라 문자열(String)로 돌려준다. `charAt()`은 딱 한 글자를 문자(char)로 돌려준다. 반환 타입 자체가 다르다.
- **`==` vs `equals()`**: `==`는 "같은 객체냐"를 묻는 참조 비교. `equals()`는 "내용이 같냐"를 묻는 값 비교. 문자열은 언제나 `equals()`.
- **length() vs length**: 문자열은 `s.length()`(괄호 있음). 배열은 `arr.length`(괄호 없음). 시험에서 자주 뒤집어 낸다.

### 키워드
- **String**: Java에서 문자열을 다루는 클래스. 불변(immutable)
- **length()**: 문자열의 글자 수를 반환. `"abc".length()` → 3
- **charAt(index)**: 해당 인덱스(위치 번호, 0부터 시작)의 문자 하나를 반환. `"abc".charAt(1)` → 'b'
- **substring(start, end)**: start부터 end-1까지의 부분 문자열을 반환. end는 미포함. `"abcde".substring(1,4)` → "bcd"
- **substring(start)**: start부터 끝까지 반환. `"abcde".substring(2)` → "cde"
- **indexOf(str)**: str이 처음 나타나는 인덱스를 반환. 없으면 -1
- **toUpperCase() / toLowerCase()**: 대문자/소문자 변환
- **replace(old, new)**: old를 new로 치환한 새 문자열 반환
- **split(regex)**: 구분자(regex)로 분리하여 String 배열로 반환
- **trim()**: 양쪽 공백을 제거한 새 문자열 반환
- **equals(str)**: 문자열 내용을 비교하여 같으면 true 반환

### 트레이싱
```
s = "Information"  (인덱스: I=0, n=1, f=2, o=3, r=4, m=5, a=6, t=7, i=8, o=9, n=10)
substring(0, 4) → "Info"  (0,1,2,3번 문자)
charAt(5) → 'm'
length() → 11
출력: Infom11
```

### 자주 출제되는 메서드 체인
```java
String s = "Hello World";
// 공백 기준 분리
String[] arr = s.split(" ");  // {"Hello", "World"}
System.out.print(arr[0]);     // Hello

// 치환
String r = s.replace("World", "Java");  // "Hello Java"

// 인덱스 검색
int idx = s.indexOf("World");  // 6
int not = s.indexOf("xyz");    // -1
```

### == vs equals
```java
String a = "hello";
String b = "hello";
String c = new String("hello");

System.out.println(a == b);       // true  (문자열 풀 같은 참조)
System.out.println(a == c);       // false (new로 별도 객체)
System.out.println(a.equals(c));  // true  (내용 비교)
```

### 스스로 가르쳐보기
> Java를 처음 보는 친구에게 `"Information".substring(0, 4)`가 왜 "Info"로 나오는지 본인만의 비유(책갈피, 자 한 뼘, 가위질 등)로 설명해 보세요. 이어서 `==`와 `equals()`가 왜 다른 질문을 하는 연산인지 한 문장으로 정리해 보세요.

체크포인트:
- [ ] substring의 end 인덱스가 미포함이라는 규칙을 말할 수 있는가
- [ ] 인덱스가 0부터 시작한다는 점을 짚었는가
- [ ] `==`는 주소 비교, `equals()`는 내용 비교임을 구분했는가
- [ ] 문자열은 불변이라 메서드가 원본을 바꾸지 않는다는 점을 말했는가

### 기출 포인트
> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제
> - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값
> - **핵심**: substring(start, end)에서 **end 인덱스는 미포함**
> - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

### 연결 개념
- 관련 카드: `pg-language-009` (C언어 문자열 처리 — strlen, strcmp와 비교)
- 관련 카드: `pg-language-017` (Python 문자열 메서드 — split, replace 등 비교)
