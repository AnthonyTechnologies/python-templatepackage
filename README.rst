python-templatepackage
======================

A Cookiecutter template for python projects that follow
`Anthony's Python Style Guide <https://github.com/AnthonyTechnologies/python-styleguide>`_. It scaffolds a
fully‑configured project with packaging, testing, formatting, documentation, and continuous integration.

Features
--------
- Modern packaging with ``pyproject.toml`` (uv by default)
- Typed package layout under ``src/`` with ``py.typed``
- Preconfigured tests (``pytest`` + ``nox`` sessions)
- Linting/formatting with Ruff, isort, and Black conventions
- Documentation skeleton (Sphinx/reStructuredText)
- Example module structure and ``__init__`` exports
- Optional license selection (MIT, Apache‑2.0, GPL‑3.0)
- Editor, pre‑commit, and GitHub workflow configuration templates

Contents
------------
At the repository root (this template):

- ``cookiecutter.json`` – variables and defaults used during generation
- ``README.rst`` – you are here; describes the template
- ``LICENSE`` – license for this template repository
- ``{{cookiecutter.project_name}}/`` – the project skeleton that Cookiecutter copies

Within the generated project skeleton (key paths):

- ``pyproject.toml`` – packaging and tool configuration
- ``noxfile.py`` – automated sessions for tests, lint, docs
- ``src/{{ cookiecutter.package_import_name }}/`` – your package code
- ``tests/`` – unit tests
- ``docs/`` – Sphinx documentation skeleton
- ``examples/`` – example scripts
- ``docs/python-styleguide/`` – the style guide referenced by this template

Quick Start
-----------

Requirements:

- Python 3.14+
- ``pip``
- ``cookiecutter``
- ``uv``

Install Cookiecutter:

.. code-block:: console

   pip install cookiecutter

Install uv:

.. code-block:: console

   pip install uv

Generate a new project from this template (choose one):

1) Local path (clone/download this repository first):

.. code-block:: console

   cookiecutter /path/to/python-templatepackage

2) Git URL (no local clone needed):

.. code-block:: console

   cookiecutter https://github.com/AnthonyTechnologies/python-templatepackage

During generation, you will be prompted for a few values. The most important are:

- ``package_name``: The distribution and base import name (e.g. ``awesome-lib``)
- ``package_import_name``: Derived automatically from ``package_name``
- ``project_name``: The repository/project name (default: ``python-{{ cookiecutter.package_name }}``)
- ``license``: One of MIT, Apache-2.0, GPL-3.0
- ``development_status``: Trove classifier reflecting maturity

If you want to add Anthony's Style Guide as a git submodule, first ensure the new project is a git repository then:

.. code-block:: console

   git submodule add https://github.com/AnthonyTechnologies/python-styleguide.git docs/python-styleguide

Customization
-------------

Adjust defaults in ``cookiecutter.json`` to fit your standards (e.g., default license, classifiers, or organization).

Contributing
------------

Issues and pull requests are welcome. If you extend the template, consider updating the documentation and tests in the
skeleton to keep generated projects consistent.

License
-------

This template repository is provided under the terms of the ``LICENSE`` file at the repository root. Generated projects
will include the license you select when running Cookiecutter.
