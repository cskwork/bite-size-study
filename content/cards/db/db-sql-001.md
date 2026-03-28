---
id: "db-sql-001"
subject: "DB"
chapter: "sql"
title: "DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)"

difficulty: 3
priority: 3
tags: [DDL, CREATE, ALTER, DROP, TRUNCATE, SQL, 데이터정의어]
quiz:
  type: "choice"
  question: "다음 중 DDL(Data Definition Language)에 해당하지 않는 것은?\n(1) CREATE\n(2) ALTER\n(3) UPDATE\n(4) TRUNCATE"
  answer: "(3) UPDATE — UPDATE는 DML(Data Manipulation Language)에 해당한다"
---

## DDL 명령어 (CREATE, ALTER, DROP, TRUNCATE)

### 핵심 개념
DDL(Data Definition Language, 데이터 정의어)은 데이터베이스 **스키마(구조)**를 정의, 변경, 삭제하는 SQL 명령어 집합이다. DDL 명령어는 실행 즉시 **자동 커밋(Auto Commit)**되므로 ROLLBACK이 불가능하다. 대상은 테이블, 뷰, 인덱스, 스키마, 도메인 등이다.

### 키워드
- **CREATE**: 테이블, 뷰, 인덱스 등 객체 생성. `CREATE TABLE 학생 (학번 INT PRIMARY KEY, 이름 VARCHAR(20) NOT NULL);`
- **ALTER**: 기존 객체 구조 변경. `ADD`(컬럼 추가), `MODIFY`(컬럼 타입 변경), `DROP COLUMN`(컬럼 삭제), `RENAME`(이름 변경)
- **DROP**: 객체 완전 삭제(구조+데이터). `CASCADE`는 참조하는 모든 객체 함께 삭제, `RESTRICT`는 참조 객체 있으면 삭제 거부
- **TRUNCATE**: 테이블의 **모든 데이터만 삭제**(구조 유지). DROP과 달리 테이블 자체는 남으며, DELETE와 달리 로그를 남기지 않아 ROLLBACK 불가
- **제약조건**: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT — CREATE/ALTER 시 함께 정의

### 기출 포인트
> DDL vs DML vs DCL 분류가 단골 출제된다. **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = SELECT/INSERT/UPDATE/DELETE**, **DCL = GRANT/REVOKE**. TRUNCATE는 DDL이므로 AUTO COMMIT 된다는 점, CASCADE/RESTRICT 옵션은 DROP에서 참조 무결성 처리 방식이라는 점을 구분할 것.

### 연결 개념
- 관련 카드: `db-sql-002` (JOIN), `db-modeling-001` (정규화)
