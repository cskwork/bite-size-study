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

### 왜 배우나
식당에 메뉴판과 주방은 있는데 손님이 주문도 못 하고, 음식도 못 받고, 주문 취소도 안 된다면 그 식당은 문을 열 수 없다. DDL로 표 구조를 만들어 뒀다면, 이제 실제로 주문(INSERT)·음식 내오기(SELECT)·수정(UPDATE)·취소(DELETE)를 할 차례다. 이 네 가지를 맡은 언어가 DML(Data Manipulation Language, 데이터 조작어)이다. 특히 SELECT는 가장 자주 쓰이면서 **작성 순서와 실행 순서가 다르다**는 함정이 있어 시험 단골이다.

### 핵심 개념
DML은 표에 저장된 데이터를 **조회·삽입·수정·삭제**하는 SQL 명령어다. DDL과 달리 자동 커밋되지 않는다. 즉 COMMIT(확정)과 ROLLBACK(되돌리기)으로 트랜잭션(Transaction, 하나로 묶인 작업 단위)을 제어할 수 있다.

특히 SELECT는 "사람이 쓰는 순서"와 "데이터베이스가 실제로 처리하는 순서"가 다르다. 이 차이가 시험에서 반복해서 나온다.

### 시각화
```
DML 명령어 네 가지:

SELECT ──▶ 데이터 조회 (읽기)      "장부에서 찾아보기"
INSERT ──▶ 데이터 삽입 (쓰기)      "장부에 새 줄 추가"
UPDATE ──▶ 데이터 수정 (고치기)    "장부의 기존 값 변경"
DELETE ──▶ 데이터 삭제 (지우기)    "장부에서 줄 지우기"

⚠ 네 명령 모두 ROLLBACK 가능 (DDL과 다름)

SELECT 절 순서 비교:
  작성 순서: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
  실행 순서: FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY
             ~~~                                             ~~~~~~
             데이터를 먼저 가져온 뒤                        마지막에 열 선택
```

### 이웃 개념 구분
- **DML vs DDL**: DML은 데이터(값)를 다루고 DDL은 구조(표 자체)를 다룬다. DML은 ROLLBACK 가능, DDL은 자동 커밋.
- **DELETE vs TRUNCATE**: DELETE는 DML이라 WHERE로 고른 행만 지울 수 있고 ROLLBACK도 된다. TRUNCATE는 DDL이라 전체만 지워지고 ROLLBACK 불가.

### 키워드
- **SELECT 작성 순서**: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY`. 사람이 코드를 쓰는 순서다.
- **SELECT 실행 순서**: `FROM → WHERE → GROUP BY → 집계함수 → HAVING → SELECT → ORDER BY`. 데이터베이스가 내부적으로 처리하는 순서. 작성 순서와 다르다.
- **INSERT 두 형태**: `INSERT INTO 표(열) VALUES(값)`은 값을 직접 넣는다. `INSERT INTO 표(열) SELECT ... FROM ...`은 다른 표에서 조회한 결과를 그대로 넣는다.
- **UPDATE**: `UPDATE 표 SET 열=값 WHERE 조건`. WHERE를 빼면 모든 행이 바뀐다.
- **DELETE**: `DELETE FROM 표 WHERE 조건`. WHERE를 빼면 모든 행이 지워진다. TRUNCATE와 달리 ROLLBACK 가능하고 로그도 남는다.
- **서브쿼리(Subquery)**: SELECT 안에 또 다른 SELECT를 넣은 것. WHERE·FROM·SELECT 절 모두에서 쓸 수 있다. 상관 서브쿼리(Correlated Subquery)는 바깥 쿼리의 행마다 안쪽 쿼리가 다시 실행된다.

### 스스로 가르쳐보기
**"SELECT 문은 사람이 쓰는 순서와 컴퓨터가 실행하는 순서가 다르다"** 이 한 문장을 친구에게 본인만의 비유로 설명해 보자. 주방 주문서, 택배 배송, 조립 설명서 같은 비유가 떠오를 것이다. 먼저 본인 문장으로 풀어 본 뒤 체크포인트로 점검하자.

체크포인트:
- [ ] 작성 순서 6개 절을 순서대로 말할 수 있는가
- [ ] 실행 순서가 왜 FROM부터 시작하는지 설명할 수 있는가
- [ ] UPDATE·DELETE에서 WHERE를 빠뜨리면 어떤 사고가 나는지 말할 수 있는가
- [ ] INSERT의 두 형태(VALUES vs SELECT)를 구분할 수 있는가

### 기출 포인트
> **2024-2회**: INSERT INTO...SELECT 구문에서 INSERT와 SELECT 키워드 빈칸 채우기로 출제됐다. VALUES로 직접 넣는 삽입과 SELECT로 복사해 넣는 삽입의 차이를 꼭 구분하라. SELECT의 실행 순서(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY)와 작성 순서를 혼동하지 말 것.

### 연결 개념
- 관련 카드: `db-sql-001` (DDL), `db-sql-004` (집계함수·GROUP BY), `db-transaction-001` (COMMIT/ROLLBACK)
