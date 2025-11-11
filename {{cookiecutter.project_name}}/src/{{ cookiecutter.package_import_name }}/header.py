"""header.py
Information about this package.

This module contains metadata about the {{ cookiecutter.package_name }} package, including version information, author details, and
licensing information. It serves as a central location for package metadata that can be imported and used by other
modules in the package.
"""

# Header #
__package_name__ = "{{ cookiecutter.package_import_name }}"

__author__ = "{{ cookiecutter.author }}"
__credits__ = ["{{ cookiecutter.author }}"]
__maintainer__ = "{{ cookiecutter.author }}"
__email__ = "{{ cookiecutter.email }}"

__copyright__ = "Copyright {{ cookiecutter.copyright_year }}, {{ cookiecutter.author }}"
__license__ = "{{ cookiecutter.license }}"

__version__ = "{{ cookiecutter.version }}"
__status__ = "{{ cookiecutter.development_status }}"

__all__ = [
    "__author__",
    "__copyright__",
    "__credits__",
    "__email__",
    "__license__",
    "__maintainer__",
    "__package_name__",
    "__status__",
    "__version__",
]
