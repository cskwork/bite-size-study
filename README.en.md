<p align="center">
  <img src="docs/assets/logo.png" alt="bite-size-study" width="120">
</p>

<h1 align="center">bite-size-study</h1>

<p align="center">
  <strong>Neuroscience-powered micro-learning CLI</strong><br>
  5 minutes a day, 2 cards at a time. The system keeps you going even when you don't feel like it.
</p>

<p align="center">
  <a href="https://github.com/cskwork/bite-size-study/actions/workflows/ci.yml"><img src="https://github.com/cskwork/bite-size-study/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/cskwork/bite-size-study/blob/main/LICENSE"><img src="https://img.shields.io/github/license/cskwork/bite-size-study" alt="License"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/coverage-85%25-brightgreen" alt="Coverage">
</p>

<p align="center">
  English | <a href="README.md">한국어</a>
</p>

---

<p align="center">
  <img src="docs/assets/demo.gif" alt="bite-size-study demo" width="600">
</p>

## Why bite-size-study?

Most study tools assume **"more is better."** Neuroscience says the opposite.

| Principle | Research Basis | How It's Applied |
|-----------|---------------|-----------------|
| **Micro-habits** | 2-Minute Rule (BJ Fogg) | 2--3 cards per session, 5 min |
| **Spaced repetition** | Ebbinghaus forgetting curve | Review scheduling by comprehension |
| **Streak effect** | Visible progress = 3.6x motivation | GitHub-style contribution calendar |
| **Temptation bundling** | Dopamine pairing (10--51% improvement) | Post-study rewards |
| **If-Then planning** | Eliminates decision fatigue (d=0.65) | Configurable trigger anchors |
| **Identity shift** | Behavior -> identity loop (r=0.55) | Session start messages |

> While Anki decides **what** to review, bite-size-study makes you **actually start.**

## Features

- **Interactive menu** -- Arrow-key navigation, all features in one screen
- **Quiz system** -- True/false, fill-in-the-blank, multiple choice
- **XP & Levels** -- Gamified progression with dopamine-driven design
- **Streak tracking** -- Consecutive study days + reward linking
- **Study calendar** -- GitHub contribution graph-style monthly heatmap
- **Subject progress** -- Visual progress bars per subject
- **Priority-based** -- Cards tagged by exam frequency, high-priority first
- **Markdown cards** -- YAML frontmatter + Markdown body

## Quick Start

```bash
# Install
pip install bite-size-study

# Or install from source
git clone https://github.com/cskwork/bite-size-study.git
cd bite-size-study
pip install -e .

# Run
bite
```

## Usage

```bash
bite              # Interactive menu (recommended)
bite start        # Start study session
bite progress     # Subject progress overview
bite cards        # List all cards
bite stats        # Streak statistics
bite calendar     # Monthly study calendar
bite heatmap      # 7-week heatmap
bite init         # Initialize a new card deck
```

## Create Your Own Cards

Add Markdown files under `content/cards/`:

```markdown
---
id: "my-001"
subject: "CS"
title: "Big O Notation"
difficulty: 2          # 1: basic, 2: intermediate, 3: advanced
priority: 3            # 3: every exam, 2: frequent, 1: occasional
quiz:
  type: "blank"        # ox, blank, choice
  question: "The time complexity of binary search is O(___)"
  answer: "log n"
---

## Big O Notation

### Key Concepts
- O(1): Constant time
- O(log n): Binary search
- O(n): Linear scan
- O(n log n): Merge sort
```

## Configuration

Customize the learning system in `config.yaml`:

```yaml
session:
  daily_cards: 3            # New cards per day
  max_review_cards: 5       # Max review cards per day
  min_session_minutes: 5    # Minimum session length

anchors:                    # If-Then triggers
  - trigger: "When I have morning coffee"
    action: "Read 2 cards"

identity:
  message: "I am a developer who grows every day."

rewards:                    # Streak rewards
  daily: "A favorite drink"
  streak_7: "1 hour of favorite content"
  streak_30: "Buy something I've wanted"
```

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Typer](https://typer.tiangolo.com/) | CLI framework |
| [Rich](https://rich.readthedocs.io/) | Terminal UI (panels, tables, markdown) |
| [PyYAML](https://pyyaml.org/) | Card parsing + config |
| [pytest](https://pytest.org/) | Test framework |

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

Whether it's new cards, bug fixes, or feature ideas -- all contributions are appreciated.

## License

[MIT](LICENSE) -- Use and modify freely.
