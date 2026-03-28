---
id: "se-cost-001"
subject: "SE"
chapter: "소프트웨어 비용 산정"
title: "소프트웨어 비용 산정 기법 (COCOMO, FP, PUTNAM, LOC)"

difficulty: 3
priority: 2
tags: [비용산정, COCOMO, FunctionPoint, PUTNAM, LOC, 소프트웨어공학, Organic, SemiDetached, Embedded]
quiz:
  type: "blank"
  question: "COCOMO 모델에서 운영체제 개발이나 실시간 처리 등 복잡도가 가장 높은 모드는 __________ 모드이다."
  answer: "Embedded(임베디드)"
---

## 소프트웨어 비용 산정 기법

### 핵심 개념
소프트웨어 비용 산정은 개발에 필요한 자원, 기간, 비용을 예측하는 활동이다. 크게 수학적 모델(LOC, COCOMO, PUTNAM)과 기능 기반 모델(Function Point)로 구분된다. 각 모델의 특성과 COCOMO 3가지 모드, FP 계산 요소를 정확히 구분하는 것이 출제 포인트다.

### 키워드
- **LOC(Lines of Code)**: 원시 코드 라인 수를 기반으로 비용 산정 — 단순하나 언어 의존적
- **COCOMO(Constructive Cost Model)**: LOC 기반 비용 산정 모델 — Boehm 제안, 3가지 모드로 구분
  - **Organic(유기형)**: 5만 라인 이하, 소규모 팀, 친숙한 환경 — 낮은 복잡도
  - **Semi-detached(반분리형)**: 30만 라인 이하, 중간 규모, 혼합 경험 팀 — 중간 복잡도
  - **Embedded(임베디드형)**: 30만 라인 초과, 실시간/OS 개발, 강한 제약 — 높은 복잡도
- **Function Point(기능 점수)**: 소프트웨어 기능의 수를 기반으로 산정 — 언어 독립적, 5가지 요소(입력·출력·조회·파일·인터페이스)
- **PUTNAM**: 소프트웨어 생명주기 전 과정에 걸친 자원 분포를 Rayleigh 분포로 산정 — 대형 프로젝트 적합

### 기출 포인트
> - **2024-1회**: COCOMO 3가지 모드 — Organic/Semi-detached/Embedded 정의 및 구분
> - FP의 5가지 계산 요소: **외부 입력(EI), 외부 출력(EO), 외부 조회(EQ), 내부 논리 파일(ILF), 외부 인터페이스 파일(EIF)**
> - COCOMO 복잡도 순서: Organic(낮음) < Semi-detached(중간) < Embedded(높음)
> - PUTNAM 모델은 "Rayleigh 분포"가 키워드 — 시간에 따른 인력 투입 곡선

### 연결 개념
- 관련 카드: `se-requirements-001` (요구사항 및 UML — 프로젝트 초기 단계)
- 관련 카드: `se-architecture-001` (소프트웨어 아키텍처 — 설계 단계)
