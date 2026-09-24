# Product

<!-- impeccable:product-schema 1 -->

> Written unattended during the 2026-09 revamp. No interview channel was available, so every fact below is inferred from the shipped site and repository and marked **(inferred)** where it is not directly visible in the code or copy.

## Platform

web

## Users

- Korean candidates preparing for the 정보처리기사 실기 (Engineer Information Processing, practical exam). **(inferred)** Mostly university students, job seekers and junior developers.
- They study in short sessions: on a phone during commutes, or at a desk with a laptop the weeks before the exam. **(inferred)** The site ships as an installable PWA with an offline service worker, which supports this.
- Job: work through exam-style short-answer problems, check the answer and the step-by-step trace, and come back to the ones they got wrong.

## Product Purpose

A free, no-login practice set: 12 subject pages and 130 problems (10 per subject, 20 in the integrated mock exam) covering code-output tracing (Java, Python, C), SQL, network/security, OS, software engineering, DB design, algorithms, UML/design patterns and new-tech terms. Success means a candidate can predict code output and recall terms under exam pressure, and knows which problems still need work.

## Positioning

Every problem is written in the practical exam's own format (write the output, complete the SQL, name the term) and every answer carries a traced explanation with explicit "trap" notes. It is not a flashcard app and not a multiple-choice drill.

## Operating Context

- Paper-style self-check: read the problem, work it out by hand, then reveal the answer. There is no auto-grading of free text.
- Progress lives only in the browser (localStorage). No accounts, no server.
- Static HTML/CSS/JS in `docs/quiz`, deployed to Vercel project `quiz`.

## Capabilities and Constraints

- 13 static pages: `index.html` hub + 12 subject pages. Shared `style.css`, `sw.js`, `manifest.json`.
- Problems are hand-authored HTML (`.question-card` with `<details>` answer). Content and meaning must be preserved.
- No build step, no framework, no backend. No analytics or tracking.
- Offline support via service worker must keep working.

## Brand Commitments

- Name: "정보처리기사 실기 퀴즈", short name "실기퀴즈". Korean-language UI.
- Voice: plain, encouraging study-coach tone ("합격을 응원합니다").

## Evidence on Hand

- 130 authored problems with answers, traces and trap notes in the subject pages.
- Six study tips on the hub page.
- No testimonials, pass rates, user counts or official affiliation. Do not invent them. The site is not affiliated with 한국산업인력공단 / Q-Net.

## Product Principles

1. The problem is the product: code, tables and answers must read perfectly on a phone.
2. Honest self-check: the candidate grades themself; the UI makes that fast and remembers it.
3. Exam realism over gamification: no points, streak hype or badges.
4. Works offline, loads instantly, costs nothing.

## Accessibility & Inclusion

- Korean body text at comfortable size, WCAG AA contrast, full keyboard use of answer reveal and self-grading, reduced-motion support.
