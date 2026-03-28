---
id: "nw-protocol-001"
subject: "NW"
chapter: "protocol"
title: "OSI 7계층 모델"

difficulty: 3
priority: 3
tags: [OSI, 7계층, 프로토콜, PDU, 네트워크]
quiz:
  type: "blank"
  question: "전송 계층의 PDU는 ___이다."
  answer: "세그먼트"
---

## OSI 7계층 모델

### 핵심 개념
OSI(Open Systems Interconnection) 7계층 모델은 국제표준화기구(ISO)가 제정한 네트워크 통신의 표준 참조 모델이다. 통신 과정을 7개 계층으로 분리하여 각 계층이 독립적으로 기능을 수행하며, 계층 간 인터페이스를 통해 데이터를 전달한다. 각 계층은 고유한 PDU(Protocol Data Unit) 이름을 가진다.

### 키워드
- **물리 계층(L1)**: 비트(Bit) 전송. 전기적/기계적 신호 변환. 리피터, 허브. RS-232, X.21
- **데이터링크 계층(L2)**: 프레임(Frame) 단위 전송. 오류 검출/흐름 제어. 스위치, 브리지. HDLC, PPP, 이더넷
- **네트워크 계층(L3)**: 패킷(Packet) 라우팅. 논리 주소(IP) 지정. 라우터. IP, ICMP, ARP, OSPF, RIP
- **전송 계층(L4)**: 세그먼트(Segment) 단위. 종단 간(End-to-End) 신뢰성 보장. TCP, UDP. 포트 번호 사용
- **세션/표현/응용 계층(L5~L7)**: 세션 관리(L5), 데이터 변환·암호화·압축(L6), 사용자 인터페이스 제공(L7). HTTP, FTP, SMTP, DNS, SSH, TLS

### 기출 포인트
> 각 계층의 PDU 명칭(비트→프레임→패킷→세그먼트→데이터)은 빈칸 채우기로 빈출된다. 계층별 대표 프로토콜과 장비를 매칭하는 문제도 자주 출제된다. 특히 **ARP**(IP→MAC 변환, L3)와 **이더넷**(L2), **TCP/UDP**(L4)의 계층 위치를 정확히 구분해야 한다. 데이터 캡슐화(Encapsulation) 과정에서 각 계층이 헤더를 추가하는 순서도 중요하다.

### 연결 개념
- 관련 카드: `nw-protocol-002`
- 관련 카드: `nw-security-001`
