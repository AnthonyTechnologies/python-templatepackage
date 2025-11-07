Installation
============

PyPI (pip) is the recomended way to install Templatepackage, but Github can also be used. If you want to run the examples
and Jupyter tutorials included in this repository, you should clone and install from GitHub.


PyPI
----
You can install templatepackage using pip:

.. code-block:: bash

   pip install templatepackage


GitHub
------

Install the latest code from the main branch without cloning:

.. code-block:: bash

   pip install "git+https://github.com/AnthonyTechnologies/python-templatepackage.git@main"


GitHub Clone
------------

Installing a github clone can be useful for either exploring the examples and tutorials and/or contributing
templatepackage.

For only exlporing examples and tutorials:

.. code-block:: bash

   git clone https://github.com/AnthonyTechnologies/python-templatepackage.git
   cd python-templatepackage
   pip install .[jupyter]

For contributing/developing templatepackage:

.. code-block:: bash

   git clone https://github.com/AnthonyTechnologies/python-templatepackage.git
   cd python-templatepackage
   pip install -e .[dev]
