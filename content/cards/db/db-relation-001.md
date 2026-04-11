---
id: "db-relation-001"
subject: "DB"
chapter: "relational-model"
title: "릴레이션 구성 요소 (Tuple, Attribute, Domain, Degree, Cardinality)"

difficulty: 3
priority: 3
tags: [릴레이션, Tuple, Attribute, Domain, Degree, Cardinality, 관계형DB, 기출빈출]
quiz:
  type: "blank"
  question: "다음 릴레이션에 대한 설명에서 빈칸을 채우시오.\n\n학생(학번, 이름, 학과, 학년) 릴레이션에 5명의 학생 데이터가 저장되어 있다.\n\n- 이 릴레이션의 Degree(차수) = ______\n- 이 릴레이션의 Cardinality(카디널리티) = ______"
  answer: "Degree = 4 (속성/컬럼 수), Cardinality = 5 (튜플/행 수) — 2024-2회, 2025-1회 기출"
---

## 릴레이션 구성 요소 (Tuple, Attribute, Domain, Degree, Cardinality)

### 왜 배우나
엑셀 시트 하나를 떠올려 보자. 열이 몇 개이고 행이 몇 개인지, "학년" 칸에는 1~4만 들어가야 한다는 규칙이 있다. 그런데 누구는 열을 "필드"라 부르고 또 누구는 "속성"이라 부른다면 대화가 뒤엉킨다. 관계형 데이터베이스(Relational Database) 세계는 이 용어를 Tuple·Attribute·Degree·Cardinality·Domain 다섯 개로 통일해 두었다. 도서관에서 책 위치를 "3층 B서가 5번 칸"이라고 누구나 같은 말로 부르는 것과 같은 이유다.

### 핵심 개념
릴레이션(Relation)은 관계형 데이터베이스가 데이터를 담는 2차원 표를 가리키는 학술 용어다. 쉽게 말해 "테이블"과 같은 뜻이다.

릴레이션은 다섯 가지 요소로 설명한다. 가로 한 줄(행)이 **튜플(Tuple)**, 세로 한 줄(열)이 **속성(Attribute)**이다. 속성의 개수가 **차수(Degree)**, 튜플의 개수가 **카디널리티(Cardinality)**다. 각 속성이 가질 수 있는 값의 범위가 **도메인(Domain)**이다.

예를 들어 "학년" 속성의 도메인은 {1, 2, 3, 4}로 정해 둘 수 있다. 시험 핵심은 이 다섯 용어의 영문·한글 매핑, 그리고 개수를 세는 방법이다.

### 시각화
```
릴레이션(테이블): 학생
┌────────┬────────┬────────┬────────┐
│  학번  │  이름  │  학과  │  학년  │ ← Attribute(속성) = 열
├────────┼────────┼────────┼────────┤
│ 1001   │ 김민수 │ 컴공   │ 2      │ ← Tuple(튜플) = 행
│ 1002   │ 이영희 │ 경영   │ 3      │
│ 1003   │ 박지훈 │ 컴공   │ 1      │
└────────┴────────┴────────┴────────┘

Degree(차수)      = 속성(열) 수 = 4
Cardinality(카디널리티) = 튜플(행) 수 = 3
Domain(도메인)    = 학년의 허용값 = {1, 2, 3, 4}
```

### 이웃 개념 구분
- **Degree vs Cardinality**: Degree는 열(속성) 수, Cardinality는 행(튜플) 수. 가장 자주 헷갈리는 쌍이다.
- **Cardinality(릴레이션) vs Cardinality(ER 다이어그램)**: 릴레이션에서는 "행 수"를 뜻하고, ER 다이어그램(개체-관계 모델)에서는 "1:N, M:N 같은 관계 대응 수"를 뜻한다. 문제가 표를 가리키는지 관계를 가리키는지 먼저 확인하라.

### 키워드
- **Tuple(튜플)**: 릴레이션의 행. 레코드(Record) 또는 인스턴스(Instance)와 같은 뜻.
- **Attribute(속성)**: 릴레이션의 열. 필드(Field)와 같은 뜻.
- **Domain(도메인)**: 속성이 가질 수 있는 값의 범위. 예: 학년 → {1, 2, 3, 4}.
- **Degree(차수)**: 속성(열)의 개수.
- **Cardinality(카디널리티)**: 튜플(행)의 개수.
- **Null**: 아직 값을 모르거나 적용할 수 없을 때 쓰는 표시. 숫자 0이나 빈 문자열과 다르다.

### 스스로 가르쳐보기
**"학생(학번, 이름, 학과, 학년) 릴레이션에 10명이 있다"** 이 한 문장을 친구 앞에서 풀어 설명한다고 생각해 보자. 본인 입으로 Tuple·Attribute·Degree·Cardinality·Domain이 각각 무엇인지 먼저 말해 보고, 그다음 아래 체크포인트로 점검해 보자.

체크포인트:
- [ ] Degree와 Cardinality를 뒤바꾸지 않고 정확히 말했는가
- [ ] Domain을 "값의 범위"로 설명하며 구체적 예시를 들었는가
- [ ] Null이 0이나 빈 문자열과 다른 이유를 말할 수 있는가

### 기출 포인트
> 매회 1문제 이상 나오는 최빈출 주제다. **2024-2회**: Cardinality/Degree 값 계산. **2025-1회**: degree, cardinality, foreign key, domain 용어 매칭. **2025-2회**: Attribute 정의. **2025-3회**: Tuple/Instance/Cardinality 용어 문제. 영문 Degree=속성 수, Cardinality=튜플 수는 반드시 암기하라.

### 연결 개념
- 관련 카드: `db-modeling-001` (정규화), `db-integrity-001` (무결성 제약조건), `db-relational-001` (관계대수)
