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

### 왜 배우나
요리를 하다가 불이 날 수도 있다. 그렇다고 가스 밸브 앞에 평생 붙어 있을 수는 없다. 대신 "불이 나면 소화기를 든다, 어쨌든 마지막엔 밸브를 잠근다"는 계획을 미리 정해 두면 된다. 프로그램도 똑같다. 파일이 없거나, 0으로 나누거나, 배열 범위를 벗어나는 사고를 예외(exception)라고 한다. 예외가 터질 때마다 프로그램이 꺼져버리면 곤란하니까, 미리 대응 계획을 박아 두는 장치가 예외처리(exception handling)다.

### 핵심 개념
예외란 프로그램이 실행되는 중에 생기는 비정상 상황이다. Java는 이걸 try·catch·finally 세 구간으로 나눠서 다룬다.

**try 블록**은 "사고가 날 수도 있는 코드"를 감싸는 구간이다. 블록(block)은 `{ }`로 묶은 코드 덩어리를 말한다. try 안에서 예외가 생기면, 그 지점 뒤의 try 코드는 건너뛰고 바로 catch로 점프한다.

**catch 블록**은 예외 종류(타입)를 하나 지정해서 잡는다. 예를 들어 `catch (ArithmeticException e)`는 "산술 오류만 받는다"는 뜻이다. 해당 종류의 예외가 날아오면 여기 코드가 실행된다.

**finally 블록**은 사고가 났든 안 났든 무조건 실행되는 뒷정리 구간이다. 파일 닫기, 네트워크 끊기처럼 "반드시 해야 하는 일"을 여기에 쓴다.

catch를 여러 개 쌓을 수도 있다. 이때 주의점 하나. 상위 타입인 `Exception`은 맨 아래로 내려야 한다. 위에 두면 모든 예외를 먼저 삼켜서 아래 catch가 무용지물이 된다.

### 시각화
```
┌──────────────────────────────────────────────┐
│              예외 없는 경우                    │
│                                              │
│  try 전체 실행 ──→ finally 실행 ──→ 다음 코드 │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│              예외 발생 시                      │
│                                              │
│  try 일부 실행                                │
│       │                                      │
│       ╳ ← 예외 발생! (이후 try 코드 건너뜀)   │
│       │                                      │
│       ▼                                      │
│  catch 블록 실행 ──→ finally 실행 ──→ 다음    │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│         다중 catch 매칭 순서                   │
│                                              │
│  예외 발생                                    │
│    │                                         │
│    ├─ catch(ArithmeticException)  ← 먼저 비교 │
│    ├─ catch(ArrayIndex...Exception) ← 그 다음 │
│    └─ catch(Exception)           ← 마지막     │
│         (가장 넓은 범위는 맨 아래)             │
└──────────────────────────────────────────────┘
```

### 이웃 개념 구분
- **throw vs throws**: `throw`는 "지금 예외를 터뜨려라"는 명령. `throws`는 메서드 이름 옆에 붙여 "이 메서드 쓰면 이런 예외 날 수 있어요"라고 미리 알리는 표시.
- **Checked vs Unchecked**: Checked(IOException 계열)는 컴파일러가 처리를 강제한다. Unchecked(RuntimeException 계열)는 강제하지 않는다. 즉 Checked는 안 잡으면 아예 빌드가 안 된다.
- **예외 vs 에러(Error)**: Exception은 프로그램이 복구해 볼 만한 사고. Error(OutOfMemoryError 등)는 보통 손쓸 수 없는 시스템 급 실패.

### 키워드
- **예외(exception)**: 프로그램 실행 중 발생하는 비정상 상황
- **try**: 예외가 발생할 수 있는 코드를 감싸는 블록
- **catch(예외타입 변수)**: 지정한 타입의 예외를 잡아서 처리하는 블록
- **finally**: 예외 발생 여부와 무관하게 반드시 실행되는 블록. 자원 해제(파일 닫기 등) 용도
- **throw**: 예외를 명시적으로 발생시키는 키워드
- **throws**: 메서드 선언부에서 "이 메서드가 발생시킬 수 있는 예외 타입"을 명시
- **RuntimeException**: 실행 시점에 발생하는 예외의 상위 클래스. 컴파일러가 처리를 강제하지 않음(Unchecked)

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

### 스스로 가르쳐보기
> 예외처리를 한 번도 안 들어본 친구에게 try·catch·finally를 본인만의 일상 비유(요리, 운전, 여행 가방 싸기 등)로 설명해 보세요. 예외가 터졌을 때와 안 터졌을 때, 실행 순서가 어떻게 달라지는지까지 한 흐름으로 이어서 말해보는 것이 핵심입니다.

체크포인트:
- [ ] 예외가 터진 뒤의 try 코드는 건너뛴다는 점을 말했는가
- [ ] catch가 예외 타입별로 갈라진다는 점을 말했는가
- [ ] finally는 예외 여부와 무관하게 항상 실행된다는 점을 말했는가
- [ ] finally에 return을 쓰면 try·catch의 return을 덮는다는 함정을 말했는가

### 기출 포인트
> - **2025-1회**: `a/b` (b=0)에서 ArithmeticException 발생 → catch 실행 후 finally 실행. 답: 출력1출력5
> - **출제 패턴**: try 블록 내 예외 발생 지점 이후 코드는 실행되지 않음. catch-finally 순서 추적
> - **핵심**: 예외 발생 시 try의 나머지 코드는 **건너뜀**. finally는 **무조건 실행**
> - **주의**: finally에 return이 있으면 try/catch의 return을 덮어씀

### 연결 개념
- 관련 카드: `pg-language-003` (Java 상속과 오버라이딩 — 예외 클래스도 상속 구조)
- 관련 카드: `pg-language-006` (Java 인터페이스와 추상클래스)
