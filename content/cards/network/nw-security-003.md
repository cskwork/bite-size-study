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

### 왜 배우나
전화 상담실에 장난 전화 수천 통이 동시에 걸려 왔다고 해 보자. 상담원이 전부 장난 전화를 받고 있으니 진짜 고객은 연결조차 못 한다. 서버도 똑같다. 가짜 연결 요청이 쏟아지면 진짜 사용자가 앉을 자리가 없어진다. 이 카드에서 다루는 네 가지 공격(SYN Flooding, Smurf, Watering Hole, 세션 하이재킹)은 각자 다른 약점—TCP 연결 절차, ICMP 프로토콜, 웹사이트 신뢰, 세션 인증—을 노린다. 약점이 다르면 방어책도 달라진다. 그래서 구분해서 익혀야 한다.

### 핵심 개념
네트워크 보안 공격은 크게 두 계열이다.
- **서비스 거부(DoS/DDoS) 계열**: 서버를 마비시키는 것이 목적이다(SYN Flooding, Smurf).
- **접근·탈취 계열**: 시스템에 침투하거나 인증 정보를 가로채는 것이 목적이다(Watering Hole, 세션 하이재킹).

이 중 SYN Flooding은 TCP(Transmission Control Protocol, 신뢰성 있는 전송 규칙)의 연결 절차인 3-way handshake(세 단계 악수)의 빈틈을 쓴다. 그래서 handshake 절차를 먼저 이해해야 한다.

### 시각화
```
 [TCP 3-way Handshake — 정상 연결]

  클라이언트              서버
      │── SYN ──────→│  "연결해 주세요"
      │←── SYN-ACK ──│  "좋아요, 준비됐어요"  (백로그 큐에 등록)
      │── ACK ──────→│  "확인, 시작합시다"    (연결 확립)

 [SYN Flooding — 공격]

  공격자(가짜 IP)          서버
      │── SYN ──────→│  백로그 큐에 등록 ①
      │── SYN ──────→│  백로그 큐에 등록 ②
      │── SYN ──────→│  백로그 큐에 등록 ③
      :    :          :     :
      │   (ACK 안 보냄)│  큐 가득 참 → 정상 사용자 접속 불가!

 [Smurf — 증폭 공격]

  공격자 → 출발지 IP를 "피해자 IP"로 위조
      │── ICMP 요청 ──→ 브로드캐스트(네트워크 전체)
                         ↓
      호스트A ── Reply ──→ 피해자
      호스트B ── Reply ──→ 피해자  ← 수십~수백 배 증폭!
      호스트C ── Reply ──→ 피해자
```

### 이웃 개념 구분
- **SYN Flooding vs Smurf**: 둘 다 서비스 거부 공격이다. SYN Flooding은 TCP 3-way handshake의 빈틈을 이용해 서버의 대기열(백로그 큐)을 채운다. Smurf는 ICMP(Internet Control Message Protocol, 인터넷 제어 메시지 프로토콜)를 써서 네트워크 전체가 피해자에게 응답을 보내게 만든다(증폭 효과).
- **Watering Hole vs 피싱**: Watering Hole은 피해자가 자주 가는 정상 사이트를 먼저 감염시켜 "기다리는" 방식. 피싱은 가짜 사이트로 "유인하는" 방식. 접근 방향이 정반대다.

### 키워드

**SYN Flooding (SYN 플러딩)**
- **원리**: TCP 3-way handshake(세 단계 악수)의 약점을 이용. 공격자가 위조된 IP로 SYN(연결 요청) 패킷을 대량 전송 → 서버가 SYN-ACK(응답)을 보내도 ACK(확인)이 돌아오지 않음 → 서버의 백로그 큐(대기열)가 가득 참
- **분류**: DoS/DDoS(서비스 거부/분산 서비스 거부) 공격
- **방어**: SYN Cookie(쿠키 기반 인증), 방화벽 필터링, 연결 임계값 설정

**Smurf 공격 (스머프)**
- **원리**: 출발지 IP를 피해자의 IP로 위조한 뒤, 브로드캐스트 주소(네트워크 내 모든 장치에 보내는 주소)로 ICMP Echo Request(핑 요청)를 전송 → 네트워크 내 모든 장치가 피해자에게 Reply(응답)를 보냄 → 트래픽이 수십~수백 배로 증폭
- **분류**: DDoS, 증폭 공격(Amplification Attack)
- **방어**: 라우터에서 외부→내부 브로드캐스트 패킷 차단

**Watering Hole (워터링 홀)**
- **원리**: 공격 대상이 자주 방문하는 웹사이트를 사전에 악성코드로 감염시켜 대기 → 피해자가 방문하면 자동 감염. "물웅덩이에서 사냥감을 기다리는 포식자"에서 이름이 유래
- **분류**: 표적형 공격, APT(Advanced Persistent Threat, 지능형 지속 위협) 계열
- **방어**: 웹 브라우저·플러그인 최신 업데이트, 행위 기반 탐지

**세션 하이재킹 (Session Hijacking)**
- **원리**: 이미 로그인한 사용자의 세션 ID(로그인 상태를 식별하는 고유 번호)를 탈취하여 그 사용자인 척 서버에 접근
- **취약점**: TCP 시퀀스 번호(순서 번호) 예측, 세션 ID 스니핑(도청)
- **방어**: HTTPS 사용, 로그인 후 세션 ID 재발급, HttpOnly/Secure 쿠키 속성 설정

### 스스로 가르쳐보기
본인만의 한 문장 비유로 이 네 공격을 정리해 보세요. 예를 들어 "SYN Flooding은 상담실 회선 점거, Watering Hole은 단골 가게 매복..." 같은 식입니다. 그런 다음 친구에게 각 공격이 노리는 약점과 동작 방식을 말로 풀어 설명해 보세요.

체크포인트:
- TCP 3-way handshake의 세 단계(SYN → SYN-ACK → ACK)를 말하고, SYN Flooding이 어느 단계에서 멈추는지 설명할 수 있나요?
- Smurf 공격에서 트래픽이 왜 "증폭"되는지 한 줄로 말할 수 있나요?
- Watering Hole이 "기다리는" 공격, 세션 하이재킹이 "가로채는" 공격이라는 차이를 구분할 수 있나요?

### 기출 포인트
> **2025-2회**: SYN Flooding 공격 원리 출제 — "TCP 3-way handshake 취약점 이용"
> **2025-1회**: 세션 하이재킹 출제 — "인증된 세션을 가로채는 공격"
> **2024-1회**: Watering Hole 출제 — "자주 방문하는 사이트를 감염시켜 대기"
> **2024-3회**: Smurf 공격 출제 — "브로드캐스트 주소를 이용한 증폭 DDoS"

### 연결 개념
- 관련 카드: `nw-security-001` (보안 공격 유형 — 전체 분류 체계)
- 관련 카드: `nw-protocol-002` (TCP vs UDP — 3-way handshake 원리)
