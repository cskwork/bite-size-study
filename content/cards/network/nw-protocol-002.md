---
id: "nw-protocol-002"
subject: "NW"
chapter: "protocol"
title: "TCP vs UDP 비교"
difficulty: 1
tags: [TCP, UDP, 전송계층, 연결지향, 비연결]
quiz:
  type: "ox"
  question: "UDP는 비연결형 프로토콜로 신뢰성은 낮지만, 3-Way Handshake 과정이 없어 실시간 스트리밍 등 속도가 중요한 서비스에 적합하다."
  answer: "O"
---

## TCP vs UDP 비교

### 핵심 개념
TCP(Transmission Control Protocol)와 UDP(User Datagram Protocol)는 전송 계층(L4)의 대표적인 프로토콜이다. TCP는 연결 지향형으로 신뢰성 있는 데이터 전송을 보장하고, UDP는 비연결형으로 빠른 전송 속도에 초점을 맞춘다. 서비스 특성에 따라 적절한 프로토콜을 선택해야 한다.

### 키워드
- **TCP 연결 수립**: 3-Way Handshake(SYN → SYN+ACK → ACK)로 연결 설정. 4-Way Handshake(FIN → ACK → FIN → ACK)로 연결 해제
- **TCP 특징**: 연결 지향, 순서 보장(시퀀스 번호), 흐름 제어(슬라이딩 윈도우), 혼잡 제어, 오류 복구(재전송). 사용 예: HTTP, FTP, SMTP, SSH
- **UDP 특징**: 비연결형, 순서 미보장, 오류 복구 없음, 헤더 단순(8바이트). 속도 우선. 사용 예: DNS, DHCP, SNMP, 실시간 스트리밍(RTP), VoIP, 온라인 게임
- **포트 번호**: TCP/UDP 모두 포트 번호로 프로세스를 식별. Well-known 포트(0~1023): HTTP(80), HTTPS(443), FTP(21), SSH(22), DNS(53), SMTP(25)
- **신뢰성 vs 속도**: TCP는 확인응답(ACK)으로 전달 보장하므로 오버헤드 큼. UDP는 확인 과정 없이 전송하여 실시간성 확보

### 기출 포인트
> TCP와 UDP의 차이를 표 형태로 비교하는 문제가 빈출된다. 특히 **3-Way Handshake**의 순서(SYN→SYN+ACK→ACK)와 **4-Way Handshake** 해제 과정이 서술형으로 출제된다. Well-known 포트 번호와 프로토콜 매칭 문제도 빈번하다. UDP 사용 사례로 **DNS**(53번 포트)가 자주 출제되며, TCP의 흐름 제어 방식인 **슬라이딩 윈도우**도 출제 범위에 포함된다.

### 연결 개념
- 관련 카드: `nw-protocol-001`
- 관련 카드: `nw-security-001`
