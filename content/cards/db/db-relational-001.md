---
id: "db-relational-001"
subject: "DB"
chapter: "relational-model"
title: "관계대수 연산 (SELECT, PROJECT, JOIN, DIVISION)"

difficulty: 3
priority: 2
tags: [관계대수, SELECT, PROJECT, JOIN, DIVISION, 릴레이션, 기호, 기출빈출]
quiz:
  type: "blank"
  question: "다음 관계대수 기호와 연산명을 매칭하시오.\n\n① σ(시그마) = ______\n② π(파이) = ______\n③ ⋈ = ______\n④ ÷ = ______"
  answer: "① 셀렉트(SELECT/선택) — 행 필터, ② 프로젝트(PROJECT/프로젝션) — 열 추출, ③ 조인(JOIN) — 두 릴레이션 결합, ④ 디비전(DIVISION) — S의 모든 튜플에 대응되는 R의 튜플 반환"
---

## 관계대수 연산 (SELECT, PROJECT, JOIN, DIVISION)

### 핵심 개념
관계대수(Relational Algebra)는 릴레이션을 다루는 **절차적 형식 언어**로, SQL의 이론적 기반이다. 각 연산의 기호(σ, π, ⋈, ÷)와 의미, 결과 릴레이션의 형태를 정확히 알아야 한다. SQL의 WHERE절은 σ에, SELECT 컬럼 지정은 π에 대응된다.

### 키워드
- **σ (시그마, SELECT/선택)**: 조건을 만족하는 **행(Tuple) 추출**. `σ학년=1(학생)` → 학년이 1인 행만 반환. SQL의 WHERE에 해당
- **π (파이, PROJECT/프로젝션)**: 지정한 **열(Attribute) 추출**. `π이름,학과(학생)` → 이름과 학과 컬럼만 반환. SQL의 SELECT 컬럼 지정에 해당
- **⋈ (조인, JOIN)**: 두 릴레이션을 **공통 속성 기준**으로 결합. 자연 조인(Natural Join)은 같은 이름의 속성으로 자동 조인하고 중복 컬럼 제거
- **÷ (디비전, DIVISION)**: R ÷ S — S의 **모든 튜플에 대응**되는 R의 튜플을 반환. "모든 X를 수강한 학생"처럼 전체 포함 조건에 사용
- **합집합(∪), 교집합(∩), 차집합(-)**: 같은 스키마를 가진 릴레이션 간 집합 연산
- **카티션 프로덕트(×)**: 두 릴레이션의 모든 조합(Degree 합산, Cardinality 곱셈)

### 기출 포인트
> **2025-2회**: π(파이) 프로젝션 연산 결과 릴레이션 구하기 출제. **2025-3회**: DIVISION(÷) 연산 결과 구하기 출제. σ와 π를 혼동하는 오답이 많으므로 "σ=행 선택(WHERE), π=열 선택(SELECT)"으로 대응시켜 암기할 것. 관계대수는 SQL 이론 문제로 변형 출제되기도 함.

### 연결 개념
- 관련 카드: `db-relation-001` (릴레이션 구성요소), `db-sql-002` (SQL JOIN과 관계대수 JOIN 대응)
