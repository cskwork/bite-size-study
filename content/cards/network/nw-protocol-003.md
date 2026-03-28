---
id: "nw-protocol-003"
subject: "NW"
chapter: "응용 계층 프로토콜"
title: "응용 계층 프로토콜 (HTTP, HTTPS, FTP, SMTP, DNS, SNMP, SSH)"

difficulty: 3
priority: 3
tags: [프로토콜, 포트번호, HTTP, FTP, SMTP, DNS, SNMP, SSH, 응용계층]
quiz:
  type: "blank"
  question: "SSH는 포트 ___번을 사용하며, 원격 접속 시 데이터를 ___ 처리한다."
  answer: "22, 암호화"
---

## 응용 계층 프로토콜 (HTTP, HTTPS, FTP, SMTP, DNS, SNMP, SSH)

### 핵심 개념
OSI 7계층 중 응용 계층(Layer 7)에 위치한 프로토콜들은 각각 고유한 포트 번호와 기능을 가진다. 정보처리기사 시험에서는 프로토콜 약어, 포트 번호, 역할의 매핑이 반드시 출제된다. 특히 SSH(22), HTTP(80), HTTPS(443), FTP(20/21), SMTP(25), DNS(53), SNMP(161) 조합은 핵심 암기 대상이다.

### 키워드

| 프로토콜 | 포트 | 계층 | 설명 |
|---------|------|------|------|
| **HTTP** | 80 | 응용(7) | HyperText Transfer Protocol, 웹 통신 (비암호화) |
| **HTTPS** | 443 | 응용(7) | HTTP + TLS/SSL, 웹 암호화 통신 |
| **FTP** | 20(데이터), 21(제어) | 응용(7) | 파일 전송 프로토콜 |
| **SMTP** | 25 | 응용(7) | 이메일 송신 (Simple Mail Transfer Protocol) |
| **POP3** | 110 | 응용(7) | 이메일 수신 (서버에서 삭제) |
| **IMAP** | 143 | 응용(7) | 이메일 수신 (서버에 유지) |
| **DNS** | 53 | 응용(7) | 도메인 이름 → IP 주소 변환 |
| **SNMP** | 161 | 응용(7) | 네트워크 장비 모니터링/관리 |
| **SSH** | 22 | 응용(7) | 암호화된 원격 접속 (Secure Shell) |
| **Telnet** | 23 | 응용(7) | 원격 접속 (비암호화, SSH로 대체됨) |
| **DHCP** | 67(서버)/68(클라이언트) | 응용(7) | IP 주소 자동 할당 |

### 기출 포인트
> **2025-2회**: SSH 포트 번호 22 직접 출제 — "SSH가 사용하는 포트 번호는?"
> **매회 반복**: 프로토콜 약어와 포트 번호 매핑 (특히 FTP 20/21 이중 포트 주의)
> **혼동 주의**: FTP는 20(데이터 전송)과 21(제어 명령) 두 포트를 사용함
> **SMTP vs POP3**: SMTP는 **송신(25)**, POP3는 **수신(110)** — 방향으로 구분

### 연결 개념
- 관련 카드: `nw-protocol-001` (OSI 7계층 모델)
- 관련 카드: `nw-security-002` (암호화 방식 — HTTPS/SSH의 TLS/SSL)
