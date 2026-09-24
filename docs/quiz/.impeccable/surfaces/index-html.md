---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["java.html"]
---

# Surface brief: 정보처리기사 실기 퀴즈 (hub + 12 subject decks)

Scope: `index.html` hub and the 12 subject pages that share `style.css`. Visitor mode: **Operate** (work a problem, reveal, self-grade, come back to misses).

Audience/job: 실기 candidates on a phone on the subway or at a desk at night; read a problem, trace it by hand, flip to the answer, mark 맞음/틀림, later review only the misses.

Decision: owner instruction "전부 다 권장대로 승인 진행하기" = proceed on recommendations; assigned direction built unattended, code-led (not recorded as a project default).

## Direction contract

THESIS: Each subject is a ring-bound 단어장 deck, and each problem is a card you flip on its ring and grade in red pen. Refuses the indigo SaaS card grid and the gamified quiz app.

OWN-WORLD: Cool desk-laminate ground, white card stock with a punched hole and a steel ring, four card-stock dyes by subject group (형광 yellow = code, mint = data, coral = theory, lilac = new tech; cobalt cover for 모의고사), ballpoint ink, one grading red. SUIT for UI and big deck titles, Nanum Pen Script only for red-pen marks, mono for code.

STORY: The visitor sees their decks and what is left, opens a deck, flips cards, marks each ○ or ✕, then filters to the ✕ cards to review.

FIRST VIEWPORT: Hub: left, headline and a "이어서 풀기" primary action with the live tally; right, the key-art of ring-bound decks. Deck page: the colored cover card at full width, subject in heavy type, a ring at top-left, card-edge tally of 10 slots, filter chips under it.

FORM: Ring-bound flashcards (단어장 링카드), position 6 on the ordered list, seed key 12c71e63. Raises: three-dye discipline (depot blind), distinct labeled state vocabulary 미풀이/맞음/틀림 (tensegrity), one color owns the cover (seedbed), every function its own labeled control (cassette deck). Signature interaction: the answer face swings down from the ring hinge (rotateX from the top edge) and grading drops a hand-drawn red ○ or ✕ on the card corner.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
