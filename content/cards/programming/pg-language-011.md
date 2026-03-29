---
id: "pg-language-011"
subject: "PG"
chapter: "Java 프로그래밍"
title: "Java 예외처리 try-catch-finally"

difficulty: 3
priority: 3
tags: [Java, 예외처리, try, catch, finally, Exception, 기출직접출제]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```java
    public class Main {
        public static void main(String[] args) {
            try {
                int[] arr = {1, 2, 3};
                System.out.print(arr[1] + " ");
                arr[5] = 10;
                System.out.print("X ");
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.print("E ");
            } finally {
                System.out.print("F");
            }
        }
    }
    ```
  answer: "2 E F"
---

## Java 예외처리 try-catch-finally

### 핵심 개념
Java의 예외처리는 **try-catch-finally** 구조로 런타임 오류를 제어한다. try 블록에서 예외가 발생하면 **즉시 실행이 중단**되고 catch 블록으로 이동한다. finally 블록은 **예외 발생 여부와 관계없이 항상 실행**된다.

### 키워드
- **try**: 예외가 발생할 수 있는 코드 블록
- **catch(예외타입 변수)**: 해당 타입의 예외를 포착하여 처리
- **finally**: 예외 발생 여부와 무관하게 반드시 실행 (자원 해제 용도)
- **throw**: 예외를 명시적으로 발생시킴
- **throws**: 메서드 선언부에서 발생 가능한 예외를 명시

### 주요 예외 클래스
```
Exception
├── RuntimeException (Unchecked)
│   ├── ArithmeticException (0으로 나누기)
│   ├── ArrayIndexOutOfBoundsException (배열 범위 초과)
│   ├── NullPointerException (null 참조)
│   ├── NumberFormatException (숫자 변환 실패)
│   └── ClassCastException (잘못된 형변환)
└── IOException, SQLException 등 (Checked)
```

### 실행 흐름 정리
```
[예외 없는 경우]  try 전체 → finally → try 다음 코드
[예외 발생 시]    try 일부 → catch → finally → try 다음 코드
[catch에서 return] catch → finally (finally가 return을 덮어씀)
```

### finally와 return
```java
static int func() {
    try {
        return 1;
    } catch (Exception e) {
        return 2;
    } finally {
        return 3;  // finally의 return이 최종 반환값
    }
}
// func() → 3
```

### 다중 catch
```java
try {
    // 코드
} catch (ArithmeticException e) {
    System.out.print("산술");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.print("배열");
} catch (Exception e) {
    System.out.print("기타");  // 상위 타입은 마지막에
}
```

### 기출 포인트
> - **2025-1회**: `a/b` (b=0)에서 ArithmeticException 발생 → catch 실행 후 finally 실행. 답: 출력1출력5
> - **출제 패턴**: try 블록 내 예외 발생 지점 이후 코드는 실행되지 않음. catch-finally 순서 추적
> - **핵심**: 예외 발생 시 try의 나머지 코드는 **건너뜀**. finally는 **무조건 실행**
> - **주의**: finally에 return이 있으면 try/catch의 return을 덮어씀

### 연결 개념
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — 예외 클래스도 상속 구조)
- 관련 카드: `pg-language-006` (Java 인터페이스와 추상클래스)
