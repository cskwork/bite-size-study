"""Structural checks for the static quiz site in docs/quiz.

The site has no build step, so these tests guard the contracts quiz.js and
sw.js rely on: numbered question cards, the shared script, the deck registry,
and the offline precache list.
"""

import json
import re
from pathlib import Path

import pytest

SITE = Path(__file__).resolve().parent.parent / "docs" / "quiz"
DECK_PAGES = [
    "java", "python", "c", "algorithm", "sql", "db",
    "network", "os", "software-engineering", "uml", "newtech", "integration",
]


def read(name):
    return (SITE / name).read_text(encoding="utf-8")


def registry():
    src = read("quiz.js")
    return {m.group(1): int(m.group(2)) for m in re.finditer(r"\{ id: '([\w-]+)', name: '[^']+', total: (\d+) \}", src)}


@pytest.mark.parametrize("deck", DECK_PAGES)
def test_deck_page_contract(deck):
    html = read(f"{deck}.html")
    ids = re.findall(r'<div class="question-card" id="q-(\d+)" data-q="(\d+)">', html)
    assert ids, "question cards must be numbered"
    numbers = [int(a) for a, b in ids]
    assert numbers == list(range(1, len(numbers) + 1))
    assert all(a == b for a, b in ids)
    assert html.count("<details>") == len(numbers), "every card needs an answer"
    assert f'<body data-deck="{deck}"' in html
    assert '<script src="quiz.js" defer></script>' in html
    assert "onclick=" not in html and "onchange=" not in html
    assert "data-filter=\"wrong\"" in html
    assert registry()[deck] == len(numbers), "quiz.js total must match the page"


def test_registry_covers_all_decks_and_totals():
    reg = registry()
    assert set(reg) == set(DECK_PAGES)
    assert sum(reg.values()) == 130


def test_hub_links_every_deck():
    html = read("index.html")
    assert "<body data-hub>" in html
    for deck in DECK_PAGES:
        assert f'data-deck-card="{deck}"' in html
        assert f'href="{deck}.html"' in html
    for img in re.findall(r"<img [^>]*>", html):
        assert 'alt="' in img


def test_service_worker_precache_exists():
    sw = read("sw.js")
    for path in re.findall(r"'\./([^']+)'", sw):
        assert (SITE / path).exists(), path
    for deck in DECK_PAGES:
        assert f"'./{deck}.html'" in sw


def test_manifest_icons_exist():
    manifest = json.loads(read("manifest.json"))
    for icon in manifest["icons"]:
        assert (SITE / icon["src"]).exists()
