Anthony's Python Style Guide
============================

Overview
--------
This repository contains a practical, opinionated Python style guide that remixes the official Google Python Style Guide
and augments it with additional guidance for modern Python projects. It is intended to be copy‑pasted or referenced
directly in projects to keep code consistent, readable, and maintainable. The structure is a fork of the
`Google Style Guide`_ and `Hypermodern Python`_ by `Claudio Jolowicz`_.

Design Goals
------------
- Readability
- Consistency
- Modularity
- Project Tools Integration

Contents
--------
The guide is split into focused documents that can be read independently:

`Syntax <syntax.md>`_: ``syntax.md`` — formatting, naming, imports, typing, docstrings, comments, strings, exceptions, comprehensions, decorators, default arguments, and more.

`Semantics <semantics.md>`_: ``semantics.md`` — program structure and behavior guidelines such as mutable global state, function length, nested classes/functions, lexical scoping, and threading.

`Project Structure <project_structure.md>`_: ``project_structure.md`` — a reusable repository layout for source, tests, docs, examples, tutorials, and configurations.

`Code & File Layout <code_file_layout.md>`_: ``code_file_layout.md`` — how to organize modules and files internally (headers, imports, definitions order, etc.).

`Documentation <documentation.md>`_: ``documentation.md`` — Sphinx recommendations and configuration notes for building docs, including autodoc, autosummary, napoleon, intersphinx, and sphinx‑click.

`Project Tools <project_tools.md>`_: ``project_tools.md`` — guidance for pre‑commit, nox, coverage, editorconfig, CI, and related developer tooling.

`Unit Tests <unit_tests.md>`_: ``unit_tests.md`` — testing mindset and structure, including pytest conventions and fixtures.

`Performance Tests <performance_tests.md>`_: ``performance_tests.md`` — approaches for measuring and guarding performance characteristics.

`Examples <examples.md>`_: ``examples.md`` — runnable or illustrative examples showing how to apply the style.

`Tutorials <module_tutorials.md>`_: ``module_tutorials.md`` and ``package_tutorials.md`` — step‑by‑step learning paths for adopting the conventions.

Quick Start
-----------
- Projects should first review the high‑level expectations in Syntax and Semantics: `syntax.md <syntax.md>`_ and `semantics.md <semantics.md>`_.
- Repositories should be structured following Project Structure: `project_structure.md <project_structure.md>`_.
- Tooling should be configured following Project Tools and Documentation guidance: `project_tools.md <project_tools.md>`_ and `documentation.md <documentation.md>`_.
- Tests should be kept close to the code and mirror the package structure: `unit_tests.md <unit_tests.md>`_.
- The other documents guidelines should be considered in addition to the first one listed here.
- This style guide can be added into the project under ``docs/python-styleguide/`` as described in: `project_structure.md <project_structure.md>`_.

License
-------
Distributed under the terms of the `MIT license`_, *python-styleguide* is free and open source software.

Contributing
------------
- Proposals for clarifications or updates should reference the section being changed and provide brief rationale.

Related Resources
-----------------
- Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
- Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
- PEP 8: https://peps.python.org/pep-0008/
- Sphinx: https://www.sphinx-doc.org/

.. _Google Style Guide: https://google.github.io/styleguide/pyguide.html
.. _Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _Claudio Jolowicz: https://github.com/cjolowicz
.. _MIT license: https://opensource.org/licenses/MIT
