{{ cookiecutter.package_name }}
===============================

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit|

.. |PyPI| image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.package_name }}/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/{{ cookiecutter.package_name }}.svg
   :target: https://pypi.org/project/{{ cookiecutter.package_name }}/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}
   :target: https://pypi.org/project/{{ cookiecutter.package_name }}
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/{{ cookiecutter.package_name }}
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/blob/main/LICENSE
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/{{ cookiecutter.project_name }}/latest.svg?label=Read%20the%20Docs
   :target: https://{{ cookiecutter.project_name }}.readthedocs.io/
   :alt: Read the documentation at https://{{ cookiecutter.project_name }}.readthedocs.io/
.. |Tests| image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/workflows/Tests/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/actions?query=workflow%3ATests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


Features
--------

Add a description of the package here!

Requirements
------------

* Python 3.14 or later

Installation
------------

You can install *{{ cookiecutter.package_name }}* via pip_ from PyPI_:

.. code:: console

   $ pip install {{ cookiecutter.package_name }}


Documentation
-------------

For comprehensive guides, see the full documentation on Read the Docs:
https://{{ cookiecutter.project_name }}.readthedocs.io/

The documentation includes a user guide, API reference, tutorials, and examples to help you get productive quickly.

For project-wide conventions and contribution standards, refer to `Anthony's Python Style Guide`_.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the {{cookiecutter.license.replace("-", " ")}} License, *{{ cookiecutter.package_name }}* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

Project Organization: `Anthony's Python Style Guide`_ based on `The Google Style Guide`_ and `Hypermodern Python`_ by `Claudio Jolowicz`_.

.. _pip: https://pip.pypa.io/
.. _PyPI: https://pypi.org/
.. _file an issue: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/issues
.. _Anthony's Python Style Guide: https://github.com/AnthonyTechnologies/python-styleguide
.. _The Google Style Guide: https://google.github.io/styleguide/pyguide.html
.. _Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _Claudio Jolowicz: https://github.com/cjolowicz
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
