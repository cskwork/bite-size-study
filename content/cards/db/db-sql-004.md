---
id: "db-sql-004"
subject: "DB"
chapter: "sql"
title: "집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)"

difficulty: 3
priority: 3
tags: [집계함수, GROUP BY, HAVING, COUNT, SUM, AVG, MAX, MIN, NULL처리, 기출빈출]
quiz:
  type: "choice"
  question: "다음 테이블에서 각 SQL의 결과값을 고르시오.\n\n점수 컬럼 데이터: 80, NULL, 70, NULL, 90\n\n(1) COUNT(*) = ?\n(2) COUNT(점수) = ?\n(A) (1)=5, (2)=5\n(B) (1)=5, (2)=3\n(C) (1)=3, (2)=3\n(D) (1)=3, (2)=5"
  answer: "(B) (1)=5, (2)=3 — COUNT(*)는 NULL 포함 전체 행 수, COUNT(컬럼)은 NULL 제외 (2025-3회 기출)"
---

## 집계함수와 GROUP BY (COUNT, SUM, AVG, MAX, MIN, HAVING)

### 핵심 개념
집계함수(Aggregate Function)는 여러 행을 하나의 결과값으로 요약한다. **NULL 처리 규칙**이 함수마다 다르며 이 차이가 매회 출제된다. GROUP BY와 함께 사용하면 그룹별 집계가 가능하고, 그룹 조건 필터링은 WHERE가 아닌 **HAVING**을 사용해야 한다.

### 키워드
- **COUNT(\*)**: NULL을 포함한 **전체 행 수** 반환
- **COUNT(컬럼)**: 해당 컬럼에서 **NULL을 제외**한 행 수 반환
- **SUM / AVG / MAX / MIN**: 모두 NULL을 **자동 제외**하고 계산 (AVG는 NULL 제외 후 나눔)
- **GROUP BY**: 지정 컬럼의 값이 같은 행끼리 묶어 집계; SELECT에는 GROUP BY 컬럼 또는 집계함수만 올 수 있음
- **HAVING vs WHERE**: WHERE는 **그룹화 이전** 행 필터, HAVING은 **그룹화 이후** 집계 결과 필터
- **실행 순서**: FROM → WHERE → GROUP BY → 집계함수 적용 → HAVING → SELECT → ORDER BY

### 기출 포인트
> **2025-3회**: COUNT(*)와 COUNT(컬럼명)의 NULL 처리 차이 문제 출제. AVG 계산 시 NULL이 포함된 경우 분모가 달라지는 함정 주의. HAVING 절에서 집계함수를 조건으로 쓸 수 있지만 WHERE 절에서는 불가능하다는 점도 빈출 포인트.

### 연결 개념
- 관련 카드: `db-sql-003` (DML·SELECT), `db-sql-002` (JOIN과 함께 쓰는 집계)
