---
name: 정보처리기사 실기 퀴즈
description: Ring-bound study decks for the 정보처리기사 practical exam; flip a card, grade it in red pen.
colors:
  desk: "#dde5ee"
  desk-deep: "#cbd7e3"
  card-stock: "#ffffff"
  paper-2: "#f3f6f9"
  card-edge: "#c7d1dd"
  hairline: "#e3e8ee"
  ballpoint-ink: "#18202c"
  ink-2: "#465163"
  ink-3: "#5f6b7c"
  grading-red: "#cf2b22"
  red-soft: "#fde9e6"
  stock-code-yellow: "#f6ef77"
  stock-data-mint: "#a6d9c3"
  stock-theory-coral: "#f48a7f"
  stock-new-lilac: "#c9b8f4"
  stock-exam-cobalt: "#2f538c"
  ink-code: "#6a6000"
  ink-data: "#1d6b51"
  ink-theory: "#a8352a"
  ink-new: "#5a43b3"
  night-desk: "#11141a"
  night-card: "#1b2029"
  night-ink: "#e8ecf2"
  night-red: "#ff8a80"
typography:
  display:
    fontFamily: "SUIT Variable, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 5.4vw, 4.5rem)"
    fontWeight: 800
    lineHeight: 1.04
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "SUIT Variable, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "clamp(2rem, 6vw, 3.25rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.035em"
  title:
    fontFamily: "SUIT Variable, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 800
    lineHeight: 1.3
    letterSpacing: "-0.025em"
  body:
    fontFamily: "SUIT Variable, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "SUIT Variable, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
    lineHeight: 1.4
  code:
    fontFamily: "D2Coding, SF Mono, JetBrains Mono, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.65
  pen:
    fontFamily: "Nanum Pen Script, cursive"
    fontSize: "1.35rem"
    fontWeight: 400
    lineHeight: 1.2
rounded:
  tag: "6px"
  control: "10px"
  button: "12px"
  card: "14px"
  deck: "16px"
  cover: "20px"
  pill: "999px"
spacing:
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1.25rem"
  lg: "1.75rem"
  xl: "2.5rem"
components:
  button-primary:
    backgroundColor: "{colors.ballpoint-ink}"
    textColor: "{colors.card-stock}"
    rounded: "{rounded.button}"
    padding: "0 1.4rem"
    height: "52px"
  button-review:
    backgroundColor: "{colors.card-stock}"
    textColor: "{colors.grading-red}"
    rounded: "{rounded.button}"
    padding: "0 1.4rem"
    height: "52px"
  grade-button:
    backgroundColor: "{colors.card-stock}"
    textColor: "{colors.ballpoint-ink}"
    rounded: "{rounded.control}"
    padding: "0 1.05rem 0 0.8rem"
    height: "44px"
  grade-button-pressed:
    backgroundColor: "{colors.red-soft}"
    textColor: "{colors.ballpoint-ink}"
    rounded: "{rounded.control}"
  filter-chip-selected:
    backgroundColor: "{colors.ballpoint-ink}"
    textColor: "{colors.desk}"
    rounded: "{rounded.pill}"
    height: "34px"
  question-card:
    backgroundColor: "{colors.card-stock}"
    textColor: "{colors.ballpoint-ink}"
    rounded: "{rounded.card}"
  topic-tag:
    textColor: "{colors.ballpoint-ink}"
    rounded: "{rounded.tag}"
    padding: "0.15rem 0.6rem"
---

# Design System: 정보처리기사 실기 퀴즈

## Overview

**Creative North Star: "The Ring-Bound Deck"**

Every subject is a 단어장 deck of dyed card stock on a steel ring, and every problem is a white card on that ring. The candidate reads the card, works it out by hand, flips it down from the ring to see the back, and grades it with a red ballpoint: a circle for right, a cross for wrong. The interface is the desk those decks lie on: a cool laminate ground, paper that casts soft shadows, and the stack of remaining cards visible under every cover.

The system is an Operate surface first. Problems, code and answers carry the page; colour lives in the covers and in the four subject dyes, never in chrome. Light mode is a daytime desk; dark mode is the same desk at night under a lamp, with its own key art.

**Key Characteristics:**
- Card stock, rings and punched holes are the structure, not decoration.
- Four subject dyes plus one exam cobalt; grading red is the only other hue.
- Korean-first typography with `keep-all` line breaking.
- One signature motion: the answer face swings down from the ring hinge.

## Colors

A cool desk-laminate neutral field, white card stock, ballpoint ink, one grading red, and a small set of card-stock dyes that encode the subject group.

### Primary
- **Grading Red** (grading-red): answers, the ○ / ✕ marks, "틀린 문제" actions and the pressed grade state. In dark mode it lifts to night-red for contrast.
- **Ballpoint Ink** (ballpoint-ink): all body text, the primary button, selected filter and current nav tab.

### Secondary
- **Subject dyes** (stock-code-yellow, stock-data-mint, stock-theory-coral, stock-new-lilac): deck covers, hub decks, nav swatches, graded tally slots. Group mapping: code (Java, Python, C, 알고리즘), data (SQL, DB설계), theory (네트워크, 운영체제, 소프트웨어공학, UML), new (신기술).
- **Deck inks** (ink-code, ink-data, ink-theory, ink-new): the dye darkened to read on white, for question numbers and key-term headings.

### Tertiary
- **Exam Cobalt** (stock-exam-cobalt): only the 통합 모의고사 deck; white text sits on it.

### Neutral
- **Desk** (desk / desk-deep): page ground, top bar, holes punched through cards.
- **Card Stock** (card-stock) and **Paper 2** (paper-2): cards, code wells, inline code.
- **Card Edge / Hairline** (card-edge, hairline): stack edges, dashed dividers, control outlines.
- **Ink 2 / Ink 3** (ink-2, ink-3): secondary copy and quiet labels (both pass AA on card stock).

### Named Rules
**The Four Dyes Rule.** Subject colour comes only from the four stock dyes and exam cobalt, assigned by subject group. Never add a per-subject hue.

**The Red Pen Rule.** Grading red means "graded" or "answer". Do not use it for decoration, links or errors unrelated to grading.

## Typography

**Display Font:** SUIT Variable (with Apple SD Gothic Neo, Malgun Gothic)
**Body Font:** SUIT Variable
**Label/Mono Font:** D2Coding / SF Mono stack for code and answers; Nanum Pen Script (subset to 함, 정, 답) for handwritten labels

**Character:** A firm Korean workhorse sans set heavy for deck names, plain for reading; code in a monospace that handles Hangul; a single handwritten pen voice for the red-pen labels.

### Hierarchy
- **Display** (800, clamp(2.5rem, 5.4vw, 4.5rem), 1.04): hub hero headline only.
- **Headline** (800, clamp(2rem, 6vw, 3.25rem), 1.1): deck cover title on subject pages.
- **Title** (800, 1.25rem, 1.3): deck names, question numbers.
- **Body** (400–600, 1rem–1.0625rem, 1.7): problem text and explanations, max 68–70ch.
- **Label** (700, 0.8125rem): tags, tally, filters.

### Named Rules
**The Keep-All Rule.** Korean text uses `word-break: keep-all`; never let a word split mid-syllable-block.

**The Pen Is Rare Rule.** The pen face appears only for "정답" and "함정" labels. It never sets sentences.

## Layout

Single reading column of 880px for subject pages; 1200px container for the hub. The top bar holds the brand and a horizontally scrolling deck nav (desktop) or a two-column menu (≤768px). A sticky deck bar sits under it with the tally, the 전체 / 안 푼 문제 / 틀린 문제 filter and 기록 지우기; on phones the tally slots hide and the filter spans the width.

The hub opens on the key-art desk band (full-bleed, copy on the left third, image cropped right on phones and placed above the copy), then deck groups in an auto-fill grid (min 245px) with the mock-exam deck spanning the full row, then the ruled study-tips sheet.

## Elevation & Depth

Depth is paper on a desk: soft, offset ambient shadows, plus the visible edges of the cards stacked beneath a cover.

### Shadow Vocabulary
- **Card rest** (`0 1px 1px rgba(24,32,44,.06), 0 10px 24px -14px rgba(24,32,44,.28)`): every card and sheet.
- **Card lift** (`0 2px 3px rgba(24,32,44,.08), 0 18px 36px -18px rgba(24,32,44,.4)`): hover on hub decks, targeted card.
- **Deck stack edges** (two negative-spread offset layers of card/paper colour with a 1px edge line under the cover): only on covers and hub decks, where they depict the physical stack.

### Named Rules
**The Stack Only Rule.** Offset, zero-blur layers are allowed only to draw the cards under a cover. Nowhere else.

## Shapes

Rounded card stock: tags 6px, controls 10px, buttons 12px, cards 14px, hub decks 16px, covers 20px, filters and nav tabs fully round. Every card carries a punched hole at the top-left; covers and decks also carry the steel ring.

## Components

### Buttons
- **Shape:** gently rounded (12px), 52px tall.
- **Primary:** ballpoint ink with white text ("이어서 풀기"); in dark mode it becomes code-yellow with ink text.
- **Review:** white with red text and a red 1.5px ring ("틀린 문제 다시 보기"), shown only when misses exist.
- **Hover / Focus:** 2px lift with a deeper shadow; focus is a 2px ink outline at 3px offset.

### Chips
- **Style:** filter group is a white pill track; the selected chip fills with ink.
- **Topic tag:** deck-tinted background, ink text, 6px corners.

### Cards / Containers
- **Question card:** white stock, 14px corners, card-rest shadow, punched hole left of the question number, dashed divider under the header, red-pen mark in the right corner once graded.
- **Answer face:** the deck tint (22% dye over card in light, 11% in dark); the answer sits in a red-outlined box labelled "정답" in pen; "함정" notes sit under a dashed rule.
- **Key-term sheet:** one white sheet with ruled rows instead of a grid of cards.

### Navigation
- **Deck nav:** each link carries a small swatch of its subject dye; the current page is an ink-filled pill with `aria-current="page"`. On phones it opens from a 44px toggle as a two-column list and closes on Escape.

### Grade control (signature)
Two labelled buttons after the explanation: "맞았어요" with a hand-drawn ○ and "틀렸어요" with a hand-drawn ✕, both in grading red. Pressing one draws the same mark on the card corner (stroke animation), fills the tally slot, and saves to localStorage. Pressing it again clears the grade.

## Do's and Don'ts

### Do:
- **Do** take subject colour from the group dye (see The Four Dyes Rule).
- **Do** keep answers in the code face inside the red-outlined 정답 box, preserving line breaks for multi-line output.
- **Do** give every new card-like surface the punched hole, and every deck cover the ring.
- **Do** provide a dark-mode value for every new token; dark mode is a night desk, not an inverted page.

### Don't:
- **Don't** add gamification (points, streaks, badges); grading is a private red-pen mark.
- **Don't** use colored left borders thicker than 1px on steps, notes or callouts.
- **Don't** use gradient text, glass panels or eyebrow labels above headings.
- **Don't** introduce a sixth dye or a second accent hue.
