"""bite-size-study CLI — Typer 기반 통합 진입점."""

from __future__ import annotations

from typing import Optional

import typer

app = typer.Typer(
    name="bite",
    help="Neuroscience-powered micro-learning CLI",
    no_args_is_help=False,
    add_completion=False,
)


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context) -> None:
    """인자 없이 실행하면 인터랙티브 메뉴를 표시한다."""
    if ctx.invoked_subcommand is None:
        from bite_size_study.menu import run_interactive_menu

        run_interactive_menu()


@app.command()
def start() -> None:
    """학습 세션을 시작한다."""
    from bite_size_study.session import run_session

    run_session()


@app.command()
def progress() -> None:
    """과목별 학습 진행률을 표시한다."""
    from bite_size_study.session import show_progress

    show_progress()


@app.command()
def cards() -> None:
    """전체 카드 목록을 표시한다."""
    from bite_size_study.core import load_all_cards
    from bite_size_study.paths import load_progress
    from bite_size_study.ui import console

    all_cards = load_all_cards()
    studied = load_progress()["cards"]
    console.print(f"\n  총 {len(all_cards)}장의 카드가 있습니다.\n")
    for card in all_cards:
        status = "✓" if card["id"] in studied else "○"
        console.print(
            f"  {status} [{card.get('subject', '?')}] {card['title']} ({card['id']})"
        )


@app.command()
def stats() -> None:
    """스트릭 통계를 표시한다."""
    from bite_size_study.streak import show_streak_stats

    show_streak_stats()


@app.command()
def calendar(
    year: Optional[int] = typer.Option(None, "--year", "-y", help="연도"),
    month: Optional[int] = typer.Option(None, "--month", "-m", help="월 (1-12)"),
) -> None:
    """월간 학습 캘린더를 표시한다."""
    from bite_size_study.streak import show_calendar

    show_calendar(target_year=year, target_month=month)


@app.command()
def heatmap() -> None:
    """최근 7주 학습 히트맵을 표시한다."""
    from bite_size_study.streak import show_weekly_heatmap

    show_weekly_heatmap()


@app.command()
def init(
    path: Optional[str] = typer.Argument(
        None, help="카드덱을 생성할 경로 (기본: content/cards/new-deck)"
    ),
) -> None:
    """새 카드덱을 초기화한다. 템플릿과 예시 카드를 생성."""
    from bite_size_study.paths import ROOT

    deck_name = path or "new-deck"
    deck_path = ROOT / "content" / "cards" / deck_name
    if deck_path.exists():
        typer.echo(f"  이미 존재하는 경로입니다: {deck_path}")
        raise typer.Exit(code=1)

    deck_path.mkdir(parents=True)

    example_card = (
        '---\n'
        f'id: "{deck_name}-001"\n'
        f'subject: "{deck_name.upper()[:2]}"\n'
        f'title: "Example Card"\n'
        'difficulty: 1\n'
        'priority: 2\n'
        'quiz:\n'
        '  type: "blank"\n'
        '  question: "Fill in the ___"\n'
        '  answer: "blank"\n'
        '---\n'
        '\n'
        '## Example Card\n'
        '\n'
        '### Key Concepts\n'
        '- Edit this card or add more .md files to this directory.\n'
    )
    (deck_path / f"{deck_name}-001.md").write_text(example_card, encoding="utf-8")

    typer.echo(f"\n  카드덱이 생성되었습니다: {deck_path}")
    typer.echo(f"  예시 카드: {deck_path / f'{deck_name}-001.md'}")
    typer.echo("  카드를 추가하려면 이 디렉토리에 .md 파일을 만드세요.\n")


def run() -> None:
    """pyproject.toml entry point."""
    app()
