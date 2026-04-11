python-templatepackage
======================

This is a Cookiecutter template for Python projects that follow
`Anthony's Python Style Guide <https://github.com/AnthonyTechnologies/python-styleguide>`_. It scaffolds a
fully‑configured project with packaging, testing, formatting, documentation, and continuous integration.

Features
--------
- Modern packaging with ``pyproject.toml`` (uv by default)
- Preconfigured tests (``pytest`` + ``nox`` sessions)
- Linting/formatting with Ruff, isort, and Black conventions
- Documentation skeleton (Sphinx/reStructuredText)
- Example module structure and ``__init__`` exports
- Optional license selection (MIT, Apache‑2.0, GPL‑3.0)
- Editor, pre‑commit, and GitHub workflow configuration templates
- [Bonus: Can add `.agents <https://github.com/AnthonyTechnologies/.agents>`_ as a submodule for agentic workflow directives]

Contents
--------
At the repository root (this template):

- ``cookiecutter.json`` – variables and defaults used during generation
- ``README.rst`` – describes the template
- ``LICENSE`` – license for this template repository
- ``{{cookiecutter.project_name}}/`` – the project skeleton that Cookiecutter copies

Within the generated project skeleton (key paths):

- ``pyproject.toml`` – packaging and tool configuration
- ``noxfile.py`` – automated sessions for tests, lint, docs
- ``src/{{ cookiecutter.package_import_name }}/`` – package code
- ``tests/`` – unit tests
- ``docs/`` – Sphinx documentation skeleton
- ``examples/`` – example scripts
- ``docs/python-styleguide/`` – the style guide referenced by this template

Quick Start
-----------

**Requirements**

- ``uv``
- Python 3.14+
- ``cookiecutter``

**1 Install uv**

Either follow the instructions on the uv website https://docs.astral.sh/uv/getting-started/installation/ or use these
commands from the website.

macOS and Linux

.. code-block:: console

   curl -LsSf https://astral.sh/uv/install.sh | sh

Windows

.. code-block:: console

   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

**2 Install Python**

.. code-block:: console

    uv python install


**3 Install Cookiecutter**

.. code-block:: console

   uv pip install cookiecutter

**4 Run Cookiecutter**

To generate a new project, either clone this repository and run cookiecutter on that directory or have cookiecutter run
from the GitHub URL.

Local path (clone/download this repository first):

.. code-block:: console

   cookiecutter /path/to/python-templatepackage

GitHub URL (no local clone needed):

.. code-block:: console

   cookiecutter https://github.com/AnthonyTechnologies/python-templatepackage

During generation, there will be prompts for a few values. The most important are:

- ``package_name``: The distribution and base import name (e.g. ``awesome-lib``)
- ``package_import_name``: Derived automatically from ``package_name``
- ``project_name``: The repository/project name (default: ``python-{{ cookiecutter.package_name }}``)
- ``license``: One of MIT, Apache-2.0, GPL-3.0
- ``development_status``: Trove classifier reflecting maturity

**5 Optional Style Guide**

`Anthony's Python Style Guide <https://github.com/AnthonyTechnologies/python-styleguide>`_ can be added as a git submodule.

First ensure the new project is a git repository, then:

.. code-block:: console

   git submodule add https://github.com/AnthonyTechnologies/python-styleguide.git docs/python-styleguide

**6 Optional .agents**

The `.agents <https://github.com/AnthonyTechnologies/.agents>`_ agent directives can be added as a git submodule.

1. First ensure the new project is a git repository, then:

.. code-block:: console

   git submodule add https://github.com/AnthonyTechnologies/.agents.git .agents

2. Update the pointer paths in ``.agents/languages/python.md`` to point to the correct locations (i.e., ``@../../docs/python-styleguide/style_guide_summary.md``).

   **Example:**

.. code-block:: console

   python -c "import pathlib; p=pathlib.Path('.agents/languages/python.md'); p.write_text(p.read_text(encoding='utf-8').replace('../python-styleguide/', '../docs/python-styleguide/'), encoding='utf-8')"

Customization
-------------

This cookiecutter template can be customized to include personal defaults which can be adjusted in ``cookiecutter.json``
(e.g., default license, classifiers, or organization). When customizing, it is suggested to create a fork of this
repository.


License
-------

This template repository is provided under the terms of the ``LICENSE`` file at the repository root. Generated projects
will include the license selected when running Cookiecutter.
