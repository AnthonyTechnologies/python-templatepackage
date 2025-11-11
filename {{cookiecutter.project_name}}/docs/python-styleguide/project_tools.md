# Anthony's Python Style Guide: Project Tooling

## Table of Contents

- [1 Overview](#1-overview)
- [2 Pre-commit](#2-pre-commit)
  - [2.1 What It Does in a Project](#21-what-it-does-in-a-project)
  - [2.2 Installation](#22-installation)
  - [2.3 Running Hooks](#23-running-hooks)
  - [2.4 Updating Hooks](#24-updating-hooks)
- [3 Nox](#3-nox)
  - [3.1 What It Does in a Project](#31-what-it-does-in-a-project)
  - [3.2 Installation](#32-installation)
  - [3.3 Common Sessions](#33-common-sessions)
  - [3.4 Running sessions](#34-running-sessions)
- [4 Other Tools and Where They Are Configured](#4-other-tools-and-where-they-are-configured)


## 1 Overview

This document describes the core development tools used across projects and how they fit into day‑to‑day workflows.
Two orchestration tools are central:

- pre-commit — automates formatting and quick static checks on each commit/push.
- nox — automates repeatable development tasks in isolated virtual environments (tests, type checks, docs, etc.).

Configuration files for these tools also reference and configure other utilities (linters, formatters, type checkers,
documentation builders). Use this page as a map to quickly locate configurations and expected usage.


## 2 Pre-commit

pre-commit manages and runs lightweight checks before code is committed or pushed. It helps keep the repository clean
and consistent by catching issues early.

Configuration: .pre-commit-config.yaml (repository root)

### 2.1 What It Does in a Project

Current hooks configured in .pre-commit-config.yaml include:

- check-added-large-files — blocks accidentally committing very large files.
- prettier — formats supported non-Python text files (Markdown, JSON, YAML, etc.).
- check-toml — validates TOML files (e.g., pyproject.toml).
- check-yaml — validates YAML files (e.g., CI workflows).
- ruff-check — fast linter for Python with an extensive rule set.
- ruff-format — opinionated Python code formatter via Ruff.
- isort — sorts and groups imports consistently.
- end-of-file-fixer — ensures a single trailing newline.
- trailing-whitespace-fixer — removes stray trailing whitespace.

Note: Some hooks are provided through the "local" repo and run using system installs. Their behavior is governed by
per‑tool settings in pyproject.toml where applicable (e.g., [tool.ruff], [tool.isort]).

### 2.2 Installation

- Ensure Python and pip are available in the environment.
- Install pre-commit into the active environment:
  - pip install pre-commit
- Install the git hooks into the repository:
  - pre-commit install --install-hooks

### 2.3 Running Hooks

- Automatically runs on git commit and, for some hooks, on push.
- Run against all files manually:
  - pre-commit run --all-files
- Run a specific hook:
  - pre-commit run ruff-check --all-files

### 2.4 Updating Hooks

- Update hook revisions to the latest recommended versions:
  - pre-commit autoupdate


## 3 Nox

Nox provides reproducible automation by running tasks inside session‑scoped virtual environments defined in noxfile.py.

Configuration/entrypoint: noxfile.py (repository root)

### 3.1 What It Does in a Project

Nox orchestrates common dev tasks, including:

- pre-commit — runs the full pre-commit suite in a controlled virtualenv and patches installed git hooks to use it.
- safety — checks dependency vulnerability advisories.
- mypy — static type checking with strict settings.
- tests — runs test suite with coverage collection enabled by default.
- coverage — reports or combines coverage data.
- typeguard — runtime type checking during tests for additional guarantees.
- xdoctest — validates examples embedded in docstrings and modules.
- docs-build — builds Sphinx documentation.
- docs — live‑reloading Sphinx docs during development.

The default sessions list is set in noxfile.py (nox.options.sessions).

### 3.2 Installation

- Install Nox and its Poetry integration:
  - pip install nox nox-poetry

### 3.3 Common Sessions

From noxfile.py, notable sessions include:

- nox -s pre-commit — run pre-commit hooks in a managed env.
- nox -s safety — check dependencies for known vulnerabilities.
- nox -s mypy — run static type checks.
- nox -s tests — run unit tests.
- nox -s coverage -- report — show coverage report; combine if multiple files exist.
- nox -s typeguard — run tests with runtime type checking enabled.
- nox -s xdoctest — run doctests/examples.
- nox -s docs-build — build docs into docs/_build.
- nox -s docs — serve docs with live rebuilds.

### 3.4 Running Sessions

- List available sessions:
  - nox -l
- Run one session (example: tests):
  - nox -s tests
- Pass through extra arguments to tools (example: pytest options):
  - nox -s tests -- -k "pattern" -q


## 4 Other Tools and Where They Are Configured

Many tool settings are centralized in pyproject.toml under their respective [tool.*] tables:

- Ruff (lint and format) — [tool.ruff], [tool.ruff.lint], [tool.ruff.format]
  - Enforces rulesets, line length, docstyle, and formatting.
  - Directory-specific Ruff configs: some top-level directories provide a local Ruff TOML that tailors linting for their content. These files are discovered automatically by Ruff when invoked from the repository root or via pre-commit/nox, and their settings apply to files within that directory tree:
    - examples/.ruff_examples.toml — examples often relax rules suited for narrative/demo code.
    - tests/.ruff_tests.toml — tests may enable/disable rules to fit testing patterns.
    - tutorials/.ruff_tutorials.toml — tutorials may prioritize readability for learners.
  - Precedence: local directory Ruff configs extend/override the root [tool.ruff] settings from pyproject.toml for files under their directory. Keep changes minimal and well-documented inside each local file.
- isort (imports) — [tool.isort]
  - Controls grouping, line length, and headings for imports.
- mypy (type checking) — [tool.mypy]
  - Strict settings and verbose error reporting.
- coverage (test coverage) — [tool.coverage.*]
  - Paths, run behavior, and report thresholds (fail_under=100).
- pytest (test runner) — configured primarily via nox; use standard CLI flags in sessions.
- xdoctest (doctest runner) — invoked via nox sessions; uses defaults unless flags are passed.
- Sphinx and extensions (documentation) — configured via docs/conf.py and session args in nox; extensions include sphinx, sphinx-click, sphinx-rtd-theme, furo, myst-parser.
- typeguard (runtime type checks) — enabled via the dedicated nox session.
- safety (dependency security) — executed via its nox session.
- pyupgrade and pep8-naming — available in dev dependencies and typically run through pre-commit or CI when configured.

Files of interest:

- pyproject.toml — central configuration for ruff, isort, mypy, coverage, and packaging metadata.
- .pre-commit-config.yaml — hook definitions for formatting, linting, and file hygiene.
- noxfile.py — automation entrypoint for development sessions.

