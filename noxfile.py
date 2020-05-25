from pathlib import Path

import nox

LINE_LENGTH = 120
FLAKE8_IGNORE = [
    "E203",
    "E231",
    "W503",
]


@nox.session
def tests(session):
    session.install(".")
    session.install("pytest")
    session.run("pytest", "tests.py")


@nox.session
def lint(session):
    session.install("flake8", "black", "isort")

    source_files = list(map(str, Path(".").glob("*.py")))

    session.run("black", "--target-version", "py38", "--line-length", f"{LINE_LENGTH}", "--check", *source_files)
    session.run(
        "flake8",
        "--max-line-length",
        f"{LINE_LENGTH}",
        "--extend-ignore",
        ",".join(FLAKE8_IGNORE),
        "--show-source",
        *source_files,
    )
    session.run(
        "isort",
        "--multi-line",
        "3",
        "--trailing-comma",
        "--force-grid-wrap",
        "0",
        "--use-parentheses",
        "--line-width",
        f"{LINE_LENGTH}",
        "--check-only",
        *source_files,
    )
