"""Rich 테마, 콘솔, 공유 UI 상수."""

from __future__ import annotations

from rich.console import Console
from rich.theme import Theme

# ── 테마 ───────────────────────────────────────
theme = Theme({
    "info": "cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "danger": "bold red",
    "highlight": "bold magenta",
})
console = Console(theme=theme)

# ── 과목 이름 매핑 ─────────────────────────────
SUBJECT_NAMES: dict[str, str] = {
    "SE": "소프트웨어 설계",
    "PG": "소프트웨어 개발",
    "DB": "데이터베이스 구축",
    "NW": "시스템 통합",
    "MT": "소프트웨어 유지보수",
}

DIFFICULTY_LABELS: dict[int, str] = {
    1: "기초",
    2: "응용",
    3: "기출심화",
}
