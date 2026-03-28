---
id: "nw-security-001"
subject: "NW"
chapter: "security"
title: "보안 공격 유형"

difficulty: 3
priority: 3
tags: [보안, DoS, DDoS, SQL인젝션, XSS, CSRF, 스니핑]
quiz:
  type: "choice"
  question: "웹 애플리케이션에서 사용자가 입력한 스크립트가 다른 사용자의 브라우저에서 실행되어 쿠키나 세션 정보를 탈취하는 공격 기법은?\n(1) SQL Injection\n(2) XSS(Cross-Site Scripting)\n(3) CSRF(Cross-Site Request Forgery)\n(4) 스니핑(Sniffing)"
  answer: "2"
---

## 보안 공격 유형

### 핵심 개념
네트워크 및 웹 보안 공격은 시스템의 가용성, 기밀성, 무결성을 위협하는 행위이다. 정보처리기사에서는 각 공격의 원리, 대상, 대응 방법을 구분할 수 있어야 한다. 공격 유형은 서비스 거부 공격, 인젝션 공격, 세션 탈취 공격, 네트워크 도청 등으로 분류된다.

### 키워드
- **DoS/DDoS**: 서비스 거부 공격. DoS는 단일 공격자가, DDoS는 다수의 좀비 PC(봇넷)가 대량 트래픽을 보내 서비스를 마비시킴. SYN Flood, Smurf, Land Attack, Ping of Death 등
- **SQL Injection**: 입력 필드에 악의적인 SQL 구문을 삽입하여 데이터베이스를 비정상적으로 조작. 대응: PreparedStatement(매개변수화 쿼리), 입력 값 검증
- **XSS(Cross-Site Scripting)**: 악성 스크립트를 웹 페이지에 삽입하여 다른 사용자의 브라우저에서 실행. 쿠키·세션 탈취. 대응: 입출력 값 이스케이프 처리, CSP 헤더
- **CSRF(Cross-Site Request Forgery)**: 인증된 사용자가 자신의 의지와 무관하게 공격자가 의도한 요청을 서버에 전송하게 만드는 공격. 대응: CSRF 토큰, Referer 검증
- **스니핑(Sniffing)**: 네트워크상의 패킷을 도청하여 정보를 수집. 대응: 암호화 통신(HTTPS, VPN), 스위칭 환경 사용

### 기출 포인트
> 각 공격 유형의 정의를 제시하고 공격 이름을 묻는 문제가 빈출된다. 특히 **SQL Injection**과 **XSS**의 차이(DB 조작 vs 브라우저 스크립트 실행), **DoS**와 **DDoS**의 차이(단일 vs 분산)를 명확히 구분해야 한다. DDoS 세부 공격인 **SYN Flood**(TCP 3-Way Handshake 악용, 대량 SYN 패킷 전송)와 **Smurf Attack**(ICMP 브로드캐스트 악용)도 서술형으로 출제된다.

### 연결 개념
- 관련 카드: `nw-security-002`
- 관련 카드: `nw-protocol-001`
