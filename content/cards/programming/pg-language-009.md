---
id: "pg-language-009"
subject: "PG"
chapter: "C언어 프로그래밍"
title: "C언어 문자열 처리"

difficulty: 3
priority: 2
tags: [C언어, 문자열, strlen, strcpy, strcmp, 문자배열, NULL종료]
quiz:
  type: "blank"
  question: |
    다음 코드의 출력 결과를 쓰시오.
    ```c
    #include <stdio.h>
    #include <string.h>
    int main() {
        char str[] = "ENGINEER";
        int len = strlen(str);
        for (int i = 0; i < len / 2; i++) {
            char tmp = str[i];
            str[i] = str[len - 1 - i];
            str[len - 1 - i] = tmp;
        }
        printf("%s", str);
        return 0;
    }
    ```
  answer: "REENIGNE"
---

## C언어 문자열 처리

### 핵심 개념
C언어에서 문자열은 **NULL 문자(`\0`)로 끝나는 문자 배열**이다. 문자열 리터럴 `"abc"`는 내부적으로 `{'a','b','c','\0'}` 4바이트를 차지한다. `<string.h>` 라이브러리의 함수들로 문자열을 조작하며, 코드 추적 문제에서 인덱스와 문자 교환이 핵심이다.

### 키워드
- **strlen(s)**: 문자열 길이 반환 (NULL 문자 제외). `"abc"` → 3
- **strcpy(dst, src)**: src를 dst에 복사
- **strcmp(s1, s2)**: 사전순 비교. 같으면 0, s1<s2이면 음수, s1>s2이면 양수
- **strcat(dst, src)**: dst 뒤에 src 이어붙이기
- **NULL 종료(`\0`)**: 모든 C 문자열의 끝을 표시. sizeof와 strlen 차이의 원인

### 문자열 뒤집기 트레이싱
```
원본: E  N  G  I  N  E  E  R  (len=8, len/2=4)
i=0: [0]↔[7]  E↔R → R  N  G  I  N  E  E  E
i=1: [1]↔[6]  N↔E → R  E  G  I  N  E  N  E
i=2: [2]↔[5]  G↔E → R  E  E  I  N  G  N  E
i=3: [3]↔[4]  I↔N → R  E  E  N  I  G  N  E
결과: REENIGNE
```

### sizeof vs strlen
```c
char s[] = "Hello";
printf("%lu", sizeof(s));  // 6 (NULL 포함)
printf("%lu", strlen(s));  // 5 (NULL 미포함)
```

### 문자 단위 조작
```c
char s[] = "Hello";
for (int i = 0; s[i] != '\0'; i++) {
    if (s[i] >= 'a' && s[i] <= 'z')
        s[i] -= 32;  // 소문자 → 대문자
}
printf("%s", s);  // HELLO
```

### 문자열 비교
```c
char a[] = "apple";
char b[] = "banana";
if (strcmp(a, b) < 0)
    printf("a가 사전순으로 앞");  // 이 줄 실행
```

### 기출 포인트
> - **기출 패턴**: 문자 배열을 for문으로 조작한 후 출력 결과 추적
> - **빈출 유형**: 문자열 뒤집기, 대소문자 변환, 특정 문자 개수 세기
> - **주의**: `char *s = "abc"`는 문자열 리터럴(수정 불가), `char s[] = "abc"`는 배열(수정 가능)
> - **아스키코드**: 'A'=65, 'a'=97, '0'=48. 대소문자 차이 = 32

### 연결 개념
- 관련 카드: `pg-language-007` (C언어 배열과 반복문)
- 관련 카드: `pg-language-001` (C언어 포인터 기초 — 문자열과 포인터)
