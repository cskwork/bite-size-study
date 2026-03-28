---
id: "se-integration-001"
subject: "SE"
chapter: "integration"
title: "미들웨어 유형"
difficulty: 1
tags: [미들웨어, WAS, MOM, RPC, ORB, 분산시스템]
quiz:
  type: "choice"
  question: "비동기 메시지 기반으로 송신측과 수신측의 직접 연결 없이 메시지 큐를 통해 데이터를 전달하는 미들웨어 유형은?\n(1) RPC\n(2) MOM\n(3) ORB\n(4) TP-Monitor"
  answer: "(2) MOM"
---

## 미들웨어 유형

### 핵심 개념
미들웨어(Middleware)는 분산 시스템에서 운영체제와 응용 프로그램 사이에 위치하여 통신, 데이터 관리, 트랜잭션 처리 등을 지원하는 소프트웨어이다. 클라이언트와 서버 간의 이질적 환경을 연결하는 중간 계층 역할을 수행하며, 유형에 따라 통신 방식과 적용 분야가 다르다.

### 키워드
- **WAS (Web Application Server)**: 동적 콘텐츠를 처리하는 웹 애플리케이션 서버. 트랜잭션, 보안, 세션 관리 등 제공 (예: Tomcat, WebLogic)
- **MOM (Message-Oriented Middleware)**: 메시지 큐 기반의 비동기 통신. 송수신 시점이 달라도 메시지 전달 보장 (예: RabbitMQ, Kafka)
- **RPC (Remote Procedure Call)**: 원격 프로시저를 로컬 호출처럼 사용하는 동기식 통신. 클라이언트가 원격 서버의 함수를 직접 호출
- **ORB (Object Request Broker)**: CORBA 표준 기반. 분산 객체 간 메서드 호출을 중개. 객체의 위치 투명성 제공
- **TP-Monitor (Transaction Processing Monitor)**: 대규모 온라인 트랜잭션을 안정적으로 처리. 트랜잭션 라우팅, 부하 분산 담당 (예: Tuxedo)
- **DB 미들웨어**: 클라이언트에서 원격 데이터베이스에 접근할 수 있도록 하는 미들웨어 (예: ODBC, JDBC)

### 기출 포인트
> MOM과 RPC의 차이가 핵심 출제 포인트이다. **MOM = 비동기 + 메시지 큐**, **RPC = 동기 + 원격 함수 호출**로 구분한다. WAS는 가장 범용적인 미들웨어로, 정적 웹서버와의 차이점(동적 처리 능력)을 묻는 문제도 출제된다. 암기법: **"WORM을 TP로 DB에 저장"** (WAS, ORB, RPC, MOM, TP-Monitor, DB).

### 연결 개념
- 관련 카드: `se-architecture-001`
