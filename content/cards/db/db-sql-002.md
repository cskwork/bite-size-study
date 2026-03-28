---
id: "db-sql-002"
subject: "DB"
chapter: "sql"
title: "JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)"

difficulty: 3
priority: 3
tags: [JOIN, INNER JOIN, OUTER JOIN, CROSS JOIN, SELF JOIN, SQL]
quiz:
  type: "blank"
  question: "두 테이블의 모든 행을 조합하여 카티션 곱(Cartesian Product)을 생성하는 조인은 ___ JOIN이다"
  answer: "CROSS"
---

## JOIN 종류 (INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF)

### 핵심 개념
JOIN은 두 개 이상의 테이블을 **공통 속성(조인 조건)**을 기준으로 결합하여 하나의 결과 집합을 생성하는 연산이다. 조인 조건에 따라 포함되는 행의 범위가 달라지며, 이를 통해 정규화로 분리된 테이블 간의 관계를 복원하여 조회할 수 있다.

### 키워드
- **INNER JOIN**: 양쪽 테이블에서 조인 조건이 **일치하는 행만** 반환. 가장 기본적인 조인 (교집합 개념)
- **LEFT (OUTER) JOIN**: 왼쪽 테이블의 **모든 행** + 오른쪽에서 일치하는 행 반환. 일치 없으면 오른쪽은 NULL
- **RIGHT (OUTER) JOIN**: 오른쪽 테이블의 **모든 행** + 왼쪽에서 일치하는 행 반환. 일치 없으면 왼쪽은 NULL
- **FULL OUTER JOIN**: 양쪽 테이블의 **모든 행** 반환. 일치하지 않는 행은 상대쪽이 NULL (합집합 개념)
- **CROSS JOIN**: 조인 조건 없이 양쪽 테이블의 **모든 행 조합**(카티션 곱). A테이블 m행 x B테이블 n행 = m*n행
- **SELF JOIN**: **같은 테이블**을 자기 자신과 조인. 별칭(Alias)을 사용하여 구분. 예: 사원-관리자 관계 조회

### 기출 포인트
> INNER JOIN과 OUTER JOIN의 차이, 특히 LEFT/RIGHT에서 NULL이 채워지는 위치를 정확히 이해해야 한다. CROSS JOIN의 결과 행 수(m*n)를 계산하는 문제가 출제된다. 또한 **자연 조인(NATURAL JOIN)**은 같은 이름의 속성을 자동으로 조인 조건으로 사용하며, **동등 조인(EQUI JOIN)**은 `=` 연산자를 사용하는 조인임을 구분할 것.

### 연결 개념
- 관련 카드: `db-sql-001` (DDL), `db-optimization-001` (인덱스)
