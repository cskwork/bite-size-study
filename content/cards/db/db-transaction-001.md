---
id: "db-transaction-001"
subject: "DB"
chapter: "transaction"
title: "트랜잭션 ACID 특성과 TCL (COMMIT, ROLLBACK, SAVEPOINT)"

difficulty: 3
priority: 2
tags: [트랜잭션, ACID, TCL, COMMIT, ROLLBACK, SAVEPOINT, Atomicity, Consistency, Isolation, Durability, 기출빈출]
quiz:
  type: "blank"
  question: "트랜잭션의 ACID 특성 중, 트랜잭션 실행 중에는 다른 트랜잭션이 그 중간 결과에 접근할 수 없도록 하는 특성을 ______이라 한다."
  answer: "고립성(Isolation) — 동시에 실행되는 트랜잭션들이 서로 간섭하지 못하도록 격리한다 (2024-1회, 2025-1회 기출)"
---

## 트랜잭션 ACID 특성과 TCL (COMMIT, ROLLBACK, SAVEPOINT)

### 핵심 개념
트랜잭션은 데이터베이스의 **논리적 작업 단위**로, 하나의 트랜잭션 내 연산은 모두 성공하거나 모두 실패해야 한다. ACID는 트랜잭션의 신뢰성을 보장하는 4가지 특성의 약자이며, TCL(Transaction Control Language)은 트랜잭션 상태를 제어하는 명령어 집합이다.

### 키워드
- **Atomicity(원자성)**: 트랜잭션의 연산은 모두 실행되거나(ALL) 하나도 실행되지 않아야(NOTHING) 함. 부분 완료 없음
- **Consistency(일관성)**: 트랜잭션 실행 전후 데이터베이스가 항상 **일관된 상태**(무결성 제약조건 만족)를 유지해야 함
- **Isolation(고립성/격리성)**: 실행 중인 트랜잭션의 중간 결과는 다른 트랜잭션이 **접근 불가**; 격리 수준(READ UNCOMMITTED ~ SERIALIZABLE)으로 조절
- **Durability(지속성/영속성)**: COMMIT된 트랜잭션의 결과는 시스템 장애가 발생해도 **영구 반영**됨 (로그, 백업으로 보장)
- **COMMIT**: 트랜잭션의 모든 변경을 **영구 저장**하고 종료
- **ROLLBACK**: 트랜잭션의 변경 사항을 **취소**하고 이전 상태로 복구; SAVEPOINT 지정 시 부분 복구 가능
- **SAVEPOINT**: 트랜잭션 내 특정 지점을 저장; `ROLLBACK TO SAVEPOINT 이름`으로 그 지점까지만 되돌림

### 기출 포인트
> **2024-1회, 2025-1회**: ACID 각 특성의 정의를 설명하거나 빈칸으로 제시하는 문제 반복 출제. 특히 원자성(Atomicity)과 고립성(Isolation)을 혼동하는 오답이 많음. DDL은 AUTO COMMIT이므로 ROLLBACK 불가, DML은 명시적 COMMIT 전까지 ROLLBACK 가능하다는 차이도 출제됨.

### 연결 개념
- 관련 카드: `db-sql-003` (DML과 트랜잭션), `db-integrity-001` (무결성과 일관성)
