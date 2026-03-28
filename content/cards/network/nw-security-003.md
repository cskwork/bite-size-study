---
id: "nw-security-003"
subject: "NW"
chapter: "네트워크 보안 공격"
title: "네트워크 보안 공격 (SYN Flooding, Smurf, Watering Hole, 세션 하이재킹)"

difficulty: 3
priority: 3
tags: [SYN-Flooding, Smurf, WateringHole, 세션하이재킹, DoS, DDoS, TCP, 3-way-handshake]
quiz:
  type: "blank"
  question: "TCP 3-way handshake의 취약점을 이용해 서버의 백로그 큐를 가득 채워 서비스를 마비시키는 공격은 ___ 공격이다."
  answer: "SYN Flooding"
---

## 네트워크 보안 공격 (SYN Flooding, Smurf, Watering Hole, 세션 하이재킹)

### 핵심 개념
네트워크 보안 공격은 DoS/DDoS 계열(SYN Flooding, Smurf)과 세션/접근 탈취 계열(세션 하이재킹, Watering Hole)로 구분된다. 각 공격의 원리(어떤 취약점을 이용하는가)와 방어 방법이 시험 핵심이다. TCP 3-way handshake 취약점을 이용한 SYN Flooding은 가장 빈출 주제다.

### 키워드

**SYN Flooding (SYN 플러딩)**
- **원리**: TCP 3-way handshake 취약점 이용. 다수의 SYN 패킷을 위조된 IP로 전송 → 서버가 SYN-ACK을 보내도 ACK 미수신 → 서버의 백로그(backlog) 큐 고갈
- **분류**: DoS/DDoS 공격
- **방어**: SYN Cookie, 방화벽 필터링, 연결 임계값 설정

**Smurf 공격 (스머프)**
- **원리**: 출발지 IP를 피해자 IP로 위조 후, 브로드캐스트 주소로 ICMP Echo Request 전송 → 네트워크 내 모든 호스트가 피해자에게 Reply 집중
- **분류**: DDoS (증폭 공격, Amplification Attack)
- **방어**: 라우터에서 외부→내부 브로드캐스트 패킷 차단

**Watering Hole (워터링 홀)**
- **원리**: 공격 대상이 자주 방문하는 웹사이트를 사전에 악성코드로 감염시켜 대기 → 피해자가 방문 시 자동 감염
- **분류**: 표적형 공격 (APT 계열)
- **방어**: 웹 브라우저/플러그인 최신 패치, 행위 기반 탐지

**세션 하이재킹 (Session Hijacking)**
- **원리**: 합법적인 사용자의 인증된 세션 ID를 탈취하여 해당 세션에 무단 참여
- **취약점**: TCP 시퀀스 번호 예측, 세션 ID 스니핑
- **방어**: HTTPS 사용, 세션 ID 재생성(로그인 후), HttpOnly/Secure 쿠키 속성

### TCP 3-way Handshake 흐름 (SYN Flooding 이해 필수)
```
클라이언트         서버
    → SYN         (연결 요청)
    ← SYN-ACK     (응답, 서버 백로그에 대기 상태 등록)
    → ACK         (연결 확립)
```
SYN Flooding: ACK를 보내지 않아 서버 백로그가 가득 찬다.

### 기출 포인트
> **2025-2회**: SYN Flooding 공격 원리 출제 — "TCP 3-way handshake 취약점 이용"
> **2025-1회**: 세션 하이재킹 출제 — "인증된 세션을 가로채는 공격"
> **2024-1회**: Watering Hole 출제 — "자주 방문하는 사이트를 감염시켜 대기"
> **2024-3회**: Smurf 공격 출제 — "브로드캐스트 주소를 이용한 증폭 DDoS"

### 연결 개념
- 관련 카드: `nw-security-001` (보안 공격 유형 — 전체 분류 체계)
- 관련 카드: `nw-protocol-002` (TCP vs UDP — 3-way handshake 원리)
