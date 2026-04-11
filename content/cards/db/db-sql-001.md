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

### 왜 배우나
이사 간 집에 옷장도 책상도 없다면 옷과 책을 둘 곳이 없다. 데이터베이스도 똑같다. 데이터를 넣기 전에 표(테이블)부터 만들어 두어야 한다. 나중에 주소 칸이 좁으면 늘리고, 필요 없어진 칸은 지워야 한다. 이런 "그릇 만들기" 작업을 담당하는 언어가 DDL(Data Definition Language, 데이터 정의어)이다. DDL이 없으면 데이터베이스는 아무 일도 시작할 수 없다.

### 핵심 개념
DDL은 데이터베이스의 구조, 즉 스키마(Schema — 표의 이름·열·타입 같은 뼈대)를 만들고 바꾸고 지우는 SQL(Structured Query Language) 명령어 모음이다.

DDL이 다루는 대상은 테이블, 뷰(View, 가상 테이블), 인덱스(Index, 검색 속도를 높이는 색인), 스키마 등이다.

한 가지 중요한 특성은 **자동 커밋**이다. DDL은 실행하는 순간 바로 확정되어 되돌릴 수 없다. 즉 ROLLBACK(되돌리기)이 불가능하다. 실수로 DROP 한 번이면 끝이니 조심해야 한다.

### 시각화
```
DDL 명령어 네 가지와 하는 일:

CREATE ──▶ 새 표(테이블) 만들기        "옷장을 새로 산다"
ALTER  ──▶ 기존 표 구조 변경            "서랍을 추가/제거한다"
DROP   ──▶ 표 자체를 완전 삭제          "옷장째로 버린다"
TRUNCATE ▶ 표는 남기고 데이터만 전부 삭제 "옷장은 두고 옷만 다 버린다"

⚠ 네 명령 모두 자동 커밋 → ROLLBACK 불가
```

### 이웃 개념 구분
- **DDL vs DML**: DDL은 구조(표 자체)를 다루고 DML(Data Manipulation Language, 데이터 조작어)은 데이터(표 안의 값)를 다룬다. DDL은 자동 커밋, DML은 ROLLBACK 가능.
- **DROP vs TRUNCATE vs DELETE**: DROP은 표와 데이터를 통째로 삭제. TRUNCATE는 표는 남기고 데이터만 전부 삭제(자동 커밋). DELETE는 조건을 붙일 수 있고 ROLLBACK도 가능하다.

### 키워드
- **CREATE**: 테이블·뷰·인덱스 같은 객체를 새로 만든다. 예: `CREATE TABLE 학생 (학번 INT PRIMARY KEY, 이름 VARCHAR(20) NOT NULL);`
- **ALTER**: 기존 객체의 구조를 바꾼다. `ADD`(열 추가), `MODIFY`(열 타입 변경), `DROP COLUMN`(열 삭제), `RENAME`(이름 변경).
- **DROP**: 객체를 구조째 삭제한다. `CASCADE`는 참조하는 객체까지 함께 지우고, `RESTRICT`는 참조가 남아 있으면 삭제를 거부한다.
- **TRUNCATE**: 테이블의 모든 데이터만 지우고 구조는 그대로 둔다. 로그를 남기지 않아 ROLLBACK 불가.
- **제약조건(Constraint)**: PRIMARY KEY(기본키), FOREIGN KEY(외래키), UNIQUE(유일값), NOT NULL(빈값 금지), CHECK(값 조건), DEFAULT(기본값). CREATE나 ALTER 시점에 함께 정의한다.

### 스스로 가르쳐보기
**DDL을 처음 듣는 친구에게 "이 네 명령이 각각 무슨 일을 하는지" 30초 안에 비유로 설명한다면 어떻게 말하시겠어요?** 옷장·공책·이사 같은 일상 비유 하나를 골라 본인 문장으로 먼저 풀어 본 뒤 아래 항목을 점검해 보자.

체크포인트:
- [ ] CREATE·ALTER·DROP·TRUNCATE 각각의 역할을 한 줄로 말할 수 있는가
- [ ] DROP과 TRUNCATE의 차이를 "구조까지 지우는가"로 구분할 수 있는가
- [ ] DDL은 자동 커밋, DML은 ROLLBACK 가능이라는 차이를 말할 수 있는가
- [ ] CASCADE와 RESTRICT의 의미를 설명할 수 있는가

### 기출 포인트
> DDL vs DML vs DCL 분류가 단골로 나온다. **DDL = CREATE/ALTER/DROP/TRUNCATE**, **DML = SELECT/INSERT/UPDATE/DELETE**, **DCL = GRANT/REVOKE**. TRUNCATE가 DDL이라 자동 커밋된다는 점, CASCADE/RESTRICT가 DROP의 참조 무결성 처리 옵션이라는 점을 꼭 구분하라.

### 연결 개념
- 관련 카드: `db-sql-002` (JOIN), `db-modeling-001` (정규화)
