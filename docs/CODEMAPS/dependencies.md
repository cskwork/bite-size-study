<!-- Generated: 2026-03-28 | Files scanned: 56 | Token estimate: ~300 -->

# Dependencies — bite-size-study

## Runtime
| Package | Version | Usage |
|---------|---------|-------|
| `rich` | ≥13.0 | TUI: Console, Panel, Table, Markdown, Prompt, Text, Theme |
| `pyyaml` | ≥6.0 | config.yaml + card frontmatter parsing |

## Dev / Test
| Package | Usage |
|---------|-------|
| `pytest` | test runner + fixtures (tmp_path, monkeypatch, capsys) |
| `pytest-cov` | coverage reporting |
| `mypy` | static type checking (`.mypy_cache/` present) |

## Standard Library (Notable)
- `json` — progress/streak persistence
- `pathlib` — cross-platform file paths
- `datetime` — streak date logic
- `random` — anchor selection

## External Services
None — fully offline, file-based CLI

## File Dependencies
```
scripts/study.py
  ← config.yaml           (session, anchors, identity, rewards, dopamine)
  ← content/cards/**/*.md  (card content with YAML frontmatter)
  ← content/subjects.yaml  (NOT imported — reference catalog only)
  ↔ data/progress.json     (read/write)
  ↔ data/streak.json       (read/write)

scripts/streak.py
  ← data/streak.json       (read-only)
  ← data/progress.json     (read-only)
```
