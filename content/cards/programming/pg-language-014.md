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

### 핵심 개념
Java의 String은 **불변 객체(Immutable)**로, 문자열 조작 메서드는 원본을 변경하지 않고 **새로운 String을 반환**한다. substring, charAt, length 등의 메서드로 문자열을 다루며, 인덱스가 0부터 시작한다는 점이 코드 추적의 핵심이다.

### 키워드
- **length()**: 문자열 길이 반환. `"abc".length()` → 3
- **charAt(index)**: 해당 인덱스의 문자 반환. `"abc".charAt(1)` → 'b'
- **substring(start, end)**: start부터 end-1까지 부분 문자열. `"abcde".substring(1,4)` → "bcd"
- **substring(start)**: start부터 끝까지. `"abcde".substring(2)` → "cde"
- **indexOf(str)**: str이 처음 나타나는 인덱스. 없으면 -1
- **toUpperCase() / toLowerCase()**: 대소문자 변환
- **replace(old, new)**: 문자/문자열 치환
- **split(regex)**: 구분자로 분리하여 String 배열 반환
- **trim()**: 양쪽 공백 제거
- **equals(str)**: 문자열 내용 비교 (`==`는 참조 비교)

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

### 기출 포인트
> - **매회 출제**: String 메서드를 활용한 출력 결과 추적은 단골 문제
> - **출제 패턴**: substring 범위 계산, charAt 인덱스, length/indexOf 반환값
> - **핵심**: substring(start, end)에서 **end 인덱스는 미포함**
> - **주의**: `==`는 참조 비교, `equals()`는 내용 비교. 시험에서 자주 함정으로 출제

### 연결 개념
- 관련 카드: `pg-language-009` (C언어 문자열 처리 — strlen, strcmp와 비교)
- 관련 카드: `pg-language-017` (Python 문자열 메서드 — split, replace 등 비교)
