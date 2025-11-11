Installation
============

PyPI (pip) is the recomended way to install {{ cookiecutter.package_name | capitalize }}, but GitHub can also be used. If you want to run the examples
and Jupyter tutorials included in this repository, you should clone and install from GitHub.


PyPI
----
You can install {{ cookiecutter.package_name }} using pip:

.. code-block:: bash

   pip install {{ cookiecutter.package_name }}


GitHub
------

Install the latest code from the main branch without cloning:

.. code-block:: bash

   pip install "git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git@main"


GitHub Clone
------------

Installing a github clone can be useful for either exploring the examples and tutorials and/or contributing
{{ cookiecutter.package_name }}.

For only exlporing examples and tutorials:

.. code-block:: bash

   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
   cd {{ cookiecutter.project_name }}
   pip install .[jupyter]

For contributing/developing {{ cookiecutter.package_name }}:

.. code-block:: bash

   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
   cd {{ cookiecutter.project_name }}
   pip install -e .[dev]
