---
id: "mt-config-001"
subject: "MT"
chapter: "config"
title: "형상관리(SCM) 절차와 도구"

difficulty: 3
priority: 2
tags: [형상관리, SCM, Git, SVN, CVS, 형상식별, 형상통제, 형상감사]
quiz:
  type: "ox"
  question: "형상 통제(Configuration Control)는 형상 항목의 변경 요청을 검토하고 승인하여 현재 기준선(Baseline)에 반영하는 활동이다."
  answer: "O"
---

## 형상관리(SCM) 절차와 도구

### 핵심 개념
형상관리(Software Configuration Management, SCM)는 소프트웨어 개발 산출물의 변경 사항을 체계적으로 관리하는 활동이다. 형상 항목의 식별부터 변경 통제, 감사, 기록까지 4단계 절차로 수행되며, 소프트웨어의 무결성과 추적성을 보장한다.

### 키워드
- **형상 식별(Identification)**: 관리 대상 형상 항목(Configuration Item)을 선정하고 고유 식별자를 부여. 소스코드, 설계서, 테스트 문서 등이 형상 항목이 됨
- **형상 통제(Control)**: 변경 요청(Change Request)을 접수·분석·승인. **형상통제위원회(CCB, Configuration Control Board)**가 변경 승인/거부 결정. 기준선(Baseline) 관리
- **형상 감사(Audit)**: 기준선 변경이 제대로 이루어졌는지 검증. 형상 항목의 무결성 확인. 형상 상태와 명세 간 일치 여부 점검
- **형상 기록/보고(Status Accounting)**: 형상 항목의 현재 상태와 변경 이력을 기록·보고. 누가, 언제, 무엇을, 왜 변경했는지 추적
- **SCM 도구**: **Git**(분산형, 브랜치 기반, 현재 가장 많이 사용), **SVN(Subversion)**(중앙집중형, 디렉토리 단위 버전 관리), **CVS**(중앙집중형, 파일 단위 관리, 초기 도구). 분산형 vs 중앙집중형: Git은 로컬 저장소에 전체 이력 보유, SVN/CVS는 서버에만 이력 존재

### 기출 포인트
> 형상관리 4단계 절차(식별→통제→감사→기록)의 순서와 각 단계의 정의를 빈칸 채우기로 묻는 문제가 매우 빈출된다. 특히 **형상통제위원회(CCB)**의 역할, **기준선(Baseline)**의 개념이 서술형으로 출제된다. Git과 SVN의 차이(분산 vs 중앙집중)를 묻는 문제도 자주 나온다. 형상관리 절차 암기법: "식통감기" (식별-통제-감사-기록).

### 연결 개념
- 관련 카드: `mt-quality-001`
- 관련 카드: `mt-testing-002`
