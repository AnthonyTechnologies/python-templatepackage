# Anthony's Python Style Guide: Documentation

## Table of Contents

- [1 Overview](#1-overview)
- [2 Project Layout and Entry Points](#2-project-layout-and-entry-points)
- [3 Sphinx Configuration](#3-sphinx-configuration)
  - [3.1 Enabled Extensions and Rationale](#31-enabled-extensions-and-rationale)
  - [3.2 HTML Theme](#32-html-theme)
  - [3.3 Intersphinx](#33-intersphinx)
  - [3.4 Type Hints and Docstring Styles](#34-type-hints-and-docstring-styles)
  - [3.5 Todos](#35-todos)
  - [3.6 Read the Docs Build Configuration](#36-read-the-docs-build-configuration)
- [4 Building the Docs](#4-building-the-docs)
  - [4.1 One‑Off Build](#41-one-off-build)
  - [4.2 Live Rebuilds During Authoring](#42-live-rebuilds-during-authoring)
  - [4.3 Cleaning Builds](#43-cleaning-builds)
- [5 Authoring Guidelines](#5-authoring-guidelines)
  - [5.1 reStructuredText vs. Markdown](#51-restructuredtext-vs-markdown)
  - [5.2 API Docs via Autodoc + Autosummary](#52-api-docs-via-autodoc--autosummary)
  - [5.3 Click CLIs](#53-click-clis)
  - [5.4 Cross-Referencing and Intersphinx](#54-cross-referencing-and-intersphinx)
  - [5.5 Source Links and Readability](#55-source-links-and-readability)
- [6 Where Things Are Configured](#6-where-things-are-configured)
- [8 Troubleshooting](#8-troubleshooting)
- [7 Style Guide](#7-style-guide)
  - [7.1 Git Submodule](#71-git-submodule)
  - [7.2 Keep It Up to Date](#72-keep-it-up-to-date)
  - [7.3 Render or Link It in Sphinx](#73-render-or-link-it-in-sphinx)


## 1 Overview

Projects use Sphinx to build documentation from reStructuredText source files and Python docstrings. Extensions are configured to:

- generate API reference pages from code (autodoc, autosummary),
- parse Google/NumPy-style docstrings (Napoleon),
- provide deep links back to source code (viewcode),
- link out to external projects like the Python standard library (intersphinx), and
- include and track TODOs during development (todo).

Command-line interface documentation is generated using sphinx-click for any Click-based CLIs.


## 2 Project Layout and Entry Points

- Documentation root: docs/
  - Sphinx configuration: docs/conf.py
  - Primary index: docs/index.rst
  - Build output: docs/_build/
- Top-level README used on the repository home page: README.rst

Docs are built and served through Nox sessions defined in noxfile.py.


## 3 Sphinx Configuration

See docs/conf.py for the authoritative configuration. Important highlights:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_click",
]

html_theme = "sphinx_rtd_theme"
```

### 3.1 Enabled Extensions and Rationale

- sphinx.ext.autodoc — imports modules and pulls in docstrings to build API pages.
- sphinx.ext.autosummary — auto-generates summary tables and stub pages for modules/classes/functions. autosummary_generate = True.
- sphinx.ext.napoleon — supports Google/NumPy docstring styles. Both napoleon_google_docstring and napoleon_numpy_docstring are enabled. Attribute annotations are included (napoleon_attr_annotations = True).
- sphinx.ext.viewcode — adds “View Source” links for documented objects, aiding traceability.
- sphinx.ext.intersphinx — cross-links to external documentation. The Python stdlib mapping is enabled.
- sphinx.ext.todo — allows .. todo:: directives. todo_include_todos = True during development.
- sphinx_click — renders documentation for Click-based CLIs declaratively.

### 3.2 HTML Theme

- Default theme: sphinx_rtd_theme (Read the Docs theme)
  - Navigation is configured for readability with navigation_depth=4 and no collapses.
- Alternative theme furo is available via the docs Nox sessions for experimentation, but the canonical build uses sphinx_rtd_theme as set in conf.py.

### 3.3 Intersphinx

- Configured mapping:
  - python → https://docs.python.org/3
- Add additional mappings in conf.py if cross-referencing external libraries becomes useful.

### 3.4 Type Hints and Docstring Styles

- autodoc_typehints = "description" — Sphinx/Napoleon shows type hints in the parameter/returns sections instead of inline signatures to improve readability for long types.
- Google and NumPy docstring styles are both supported; prefer Google style for new content unless aligning with an established convention in a specific module.

### 3.5 Todos

- .. todo:: directives are included in builds (todo_include_todos = True). Use sparingly and convert todos into issues as work is planned.

### 3.6 Read the Docs Build Configuration

Read the Docs (RTD) builds are configured via a YAML file located at docs/.readthedocs.yaml. Typical key settings:

- version: 2 — RTD’s v2 configuration schema.
- build:
  - os: ubuntu-20.04 — Linux image used for builds.
  - tools.python: "3.12" — Python version used on RTD.
- sphinx:
  - configuration: docs/conf.py — RTD invokes Sphinx with this config file.
- formats: all — Build all supported formats (HTML, PDF via LaTeX, and EPUB).
- python.install:
  - requirements: docs/requirements.txt — Additional doc-specific dependencies are installed from this pinned file.
  - path: . — Installs the project itself into the RTD environment so autodoc can import modules.

Notes and recommendations:
- Keep docs/requirements.txt aligned with extensions and themes configured in docs/conf.py (e.g., sphinx, sphinx-rtd-theme, sphinx-click; optional furo, myst-parser). Pin versions to ensure reproducible RTD builds.
- Local builds via nox -s docs-build / nox -s docs do not use .readthedocs.yaml; they rely on noxfile.py’s session dependencies. When changing Sphinx extensions or themes, update both the nox sessions and docs/requirements.txt to keep parity with RTD.
- If the location of conf.py or the Python version changes, reflect those changes in docs/.readthedocs.yaml to avoid RTD build failures.


## 4 Building the Docs

All commands are executed via Nox to ensure reproducibility.

### 4.1 One‑Off Build

- Build static HTML into docs/_build:
  - nox -s docs-build
- Optional: pass extra sphinx-build options after the session name:
  - nox -s docs-build -- -W  # treat warnings as errors

### 4.2 Live Rebuilds During Authoring

- Serve docs with live reload on changes:
  - nox -s docs
- A browser window opens by default; this behavior can be disabled by removing --open-browser in noxfile.py or by overriding with positional arguments.

### 4.3 Cleaning Builds

- The docs-build and docs sessions remove docs/_build before each run. If a fully clean environment is needed, also delete any cached auto-generated API stubs that may have been created locally.


## 5 Authoring Guidelines

### 5.1 reStructuredText vs. Markdown

- The canonical format is reStructuredText (.rst). The docs use index.rst and standard Sphinx/ReST directives.
- Although the docs sessions install myst-parser, it is not currently enabled in conf.py. If enabling Markdown is desired in the future, add "myst_parser" to extensions and follow MyST’s syntax rules. Until then, prefer .rst.

### 5.2 API Docs via Autodoc + Autosummary

- Keep public APIs well-documented with complete docstrings. autosummary_generate is enabled, which can generate index pages and per-object stubs when you include autosummary tables in .rst files.
- Provide clear type hints; they will be rendered in the description sections.
- For module organization and public/private boundaries, follow the guidance in semantics.md and project_structure.md. Only public objects should be included in user-facing API pages.

### 5.3 Click CLIs

- For Click-based CLIs, document commands using sphinx-click directives.
- Example usage in a .rst file:

  .. code-block:: rst

     Command-line Interface
     ----------------------

     .. click:: package.module:cli
        :prog: tool-name
        :show-nested:

- The token package.module:cli should be replaced with the import path and callable for the project's Click entry point.

### 5.4 Cross-Referencing and Intersphinx

- Use Sphinx cross-reference roles to link to symbols:
  - :py:mod:`package.module`, :py:class:`package.Class`, :py:meth:`package.Class.method`.
- For Python stdlib references, intersphinx provides automatic links, e.g., :class:`dict`, :mod:`asyncio`.

### 5.5 Source Links and Readability

- viewcode adds “View Source” links to documented objects. Ensure source files remain readable and follow the code style guide so rendered source is approachable.


## 6 Where Things Are Configured

- docs/conf.py — Sphinx configuration (extensions, theme, intersphinx, napoleon, todo, autodoc/autosummary options).
- docs/.readthedocs.yaml — Read the Docs build configuration (Python version, OS image, Sphinx entry point, output formats, and install steps).
- noxfile.py — Sessions for building and serving the docs; installs Sphinx and selected extensions.
- pyproject.toml — Project metadata and tooling configs (ruff, mypy, coverage) that indirectly affect example code in docs.


## 7 Style Guide

Projects may also include this style guide as a Git submodule repository in docs/python-styleguide. This keeps the style
guide close to the project documentation to allow pinning known-good revision and pull updates. It is especially useful
for projects with a large number of contributors and AI Agents helping with writing code.

### 7.1 Git Submodule

Run these commands from the repository root (replace the remote URL if the fork or hosting differs):

```bash
# Add the style guide as a submodule under docs/python-styleguide
git submodule add -b main https://github.com/example-org/python-styleguide.git docs/python-styleguide

# Commit the .gitmodules entry and submodule pointer
git commit -m "docs: add python-styleguide as submodule"

# If cloning a repo that already has the submodule, initialize it with:
git submodule update --init --recursive
```

Notes:
- Submodules are pinned to a specific commit; they do not auto-track the remote branch. This is desirable for reproducible docs builds.
- If submodules are not preferred, git subtree is an alternative; however, submodules are simpler to keep read-only and clearly versioned.

### 7.2 Keep It Up to Date

To pull the latest from the style guide:

```bash
# Option A: update from the superproject, keeping the pointer fast-forwarded
git submodule update --remote --merge docs/python-styleguide

# Option B: cd into the submodule and pull explicitly
cd docs/python-styleguide
git fetch origin
git checkout main
git pull --ff-only
cd -

# Commit the updated submodule pointer in the superproject
git commit -am "docs: bump python-styleguide submodule"
```

CI/hosting considerations:
- Read the Docs: ensure submodules are fetched. In docs/.readthedocs.yaml add:

  ```yaml
  submodules:
    include:
      - docs/python-styleguide
  ```

- Other CI: ensure the checkout step initializes submodules, e.g., git submodule update --init --recursive.

### 7.3 Render or Link It in Sphinx

This repository largely uses Markdown (.md) files. To render them inside the project's Sphinx documentation:

1) Enable MyST-Parser in docs/conf.py:

```python
extensions = [
    # existing extensions...
    "myst_parser",
]
```

Ensure myst-parser is installed in the documentation environment (nox session and/or docs/requirements.txt).

2) Include the files in a toctree, for example in docs/index.rst:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Python Style Guide

      python-styleguide/README.rst
      python-styleguide/documentation.md
      python-styleguide/syntax.md
      python-styleguide/semantics.md
      python-styleguide/project_structure.md
      python-styleguide/code_file_layout.md
      python-styleguide/module_tutorials.md
      python-styleguide/package_tutorials.md
      python-styleguide/unit_tests.md
      python-styleguide/performance_tests.md
      python-styleguide/project_tools.md
      python-styleguide/examples.md

If enabling Markdown rendering is not desired, it is still possible to:
- Link to the files as plain hyperlinks (they will render on Git hosting platforms but not as Sphinx pages), or
- Include only README.rst (since it is already in ReST) and link out to the rest of the repository.


## 8 Troubleshooting

- Import errors during autodoc
  - Sphinx imports modules to extract docstrings. The configuration ensures src/ is on sys.path. If import errors occur, confirm the module is installable or visible under src/ and that any optional dependencies are available.
- Missing API pages
  - autosummary only generates pages for entries included in autosummary tables. Ensure .rst files include the relevant modules/objects, or generate stubs ahead of time if needed.
- Theme issues or missing styles
  - Confirm sphinx_rtd_theme is installed in the session environment. The nox sessions install it automatically.
- Markdown not rendering
  - MyST is not enabled by default. Use .rst or enable myst-parser in conf.py if Markdown support is required.
