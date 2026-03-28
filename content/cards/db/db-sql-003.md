---
id: "db-sql-003"
subject: "DB"
chapter: "sql"
title: "DML 명령어 (SELECT, INSERT, UPDATE, DELETE)"

difficulty: 3
priority: 3
tags: [DML, SELECT, INSERT, UPDATE, DELETE, SQL, 데이터조작어, 기출빈출]
quiz:
  type: "blank"
  question: "다음 SQL에서 빈칸을 채우시오.\n\n```sql\n______ INTO 학생(학번, 이름)\n______ 편입생.학번, 편입생.이름\nFROM 편입생\nWHERE 학년 = 1;\n```"
  answer: "INSERT, SELECT — INSERT INTO...SELECT 구문으로 다른 테이블에서 데이터를 조회하여 삽입한다 (2024-2회 기출)"
---

## DML 명령어 (SELECT, INSERT, UPDATE, DELETE)

### 핵심 개념
DML(Data Manipulation Language, 데이터 조작어)은 테이블에 저장된 **데이터를 조회·삽입·수정·삭제**하는 SQL 명령어다. DDL과 달리 **자동 커밋되지 않으며** COMMIT/ROLLBACK으로 트랜잭션을 제어할 수 있다. SELECT 구문의 절 순서는 시험 단골 출제 포인트다.

### 키워드
- **SELECT 작성(문법) 순서**: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY` (순서 암기 필수)
- **SELECT 실행 순서**: `FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY` (작성 순서와 다름에 주의)
- **INSERT 두 가지 형태**: `INSERT INTO 테이블(컬럼) VALUES(값)` (직접 삽입) vs `INSERT INTO 테이블(컬럼) SELECT ... FROM ...` (조회 결과 삽입)
- **UPDATE**: `UPDATE 테이블 SET 컬럼=값 WHERE 조건` — WHERE 생략 시 전체 행 수정
- **DELETE**: `DELETE FROM 테이블 WHERE 조건` — WHERE 생략 시 전체 행 삭제 (TRUNCATE와 달리 ROLLBACK 가능, 로그 남김)
- **서브쿼리**: WHERE, FROM, SELECT 절에서 중첩 SELECT 사용 가능; 상관 서브쿼리는 외부 쿼리 행마다 실행

### 기출 포인트
> **2024-2회**: INSERT INTO...SELECT 구문에서 INSERT와 SELECT 키워드 빈칸 채우기로 출제됨. VALUES를 쓰는 단순 삽입과 SELECT를 쓰는 복사 삽입의 차이를 반드시 구분할 것. SELECT 절의 실행 순서(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)와 작성 순서를 혼동하지 말 것.

### 연결 개념
- 관련 카드: `db-sql-001` (DDL), `db-sql-004` (집계함수·GROUP BY), `db-transaction-001` (COMMIT/ROLLBACK)
