# Anthony's Python Style Guide: Unit Tests

## Table of Contents

- [1 Background](#1-background)
- [2 pytest](#2-pytest)
- [3 Directory Hierarchy](#3-directory-hierarchy)
- [4 Test Structure](#4-test-structure)
  - [4.1 Test Classes](#41-test-classes)
  - [4.2 Test Methods](#42-test-methods)
  - [4.3 Test Suites](#43-test-suites)
    - [4.3.1 Base Test Suites](#431-base-test-suites)
    - [4.3.2 Concrete Test Suites](#432-concrete-test-suites)
  - [4.4 Main](#44-main)
- [5 Test Semantics and Syntax](#5-test-semantics-and-syntax)
  - [5.1 Assertions](#51-assertions)
  - [5.2 Fixtures](#52-fixtures)
  - [5.3 Test Doubles](#53-test-doubles)
- [6 Test Execution](#6-test-execution)


## 1 Background

Unit tests are used to verify the correctness of the code being tested to ensure that it is working as expected.
Typically, unit tests are written to verify individual components of the code.

Test suites are collections of related tests that validate a specific component, feature, or functionality of the
software. They help organize tests logically and provide a structured way to verify multiple aspects of the code. Test
suites can inherit from base test suites to provide consistent testing patterns across similar components.

Unit tests and test suites should follow the guidelines set forth by the general styleguide such as the code
organization, file structure, naming conventions, docstrings, and other standard practices in:

- [Code File Layout](code_file_layout.md) - For file organization and structure
- [Syntactic Guidelines](syntax.md) - For naming conventions, docstrings, and code formatting
- [Semantics Guidelines](semantics.md) - For general code organization principles

The guidelines in this document are supplemental to the general guidelines and focus on test-specific code to ensure
consistency, maintainability, and effectiveness of the test suite across the project.


## 2 pytest

**pytest** testing framework is the preferred framework for Python projects, as it provides more features and
flexibility than python's unittest library.

In pytest, tests can be created by defining a test function with a `test_` prefix. pytest can then run the tests using
its Python or command line interface and display diagnostics about the tests. Additionally, the pytest API offers an
extensive array of options for customizing the run conditions and diagnostic information of these tests. For more
information on pytest, see the [pytest documentation](https://docs.pytest.org/en/latest/).

The pytest package has many features, and this styleguide will offer guidance on how to use them.


## 3 Directory Hierarchy

Base Test Suites or test suites which cover general implements should be located in the package source codes under
`testsuite`. Under normal circumstances, test suites should not be placed in the project source as only developers need
test suites; not package users. However, given that PYPI currently does not support alternate package installations.
These test suites should be included in the source to allow developers using PYPI to expand or create their own test
suites.

Example:
```
src/
  templatepackage/                  # The main source package
    testsuite/
      bases/
        __init__.py
        basetestsuite.py
        ...
      __init__.py
      objecttestsuite.py
      ...
```

Concrete Test Suites and unit tests for individual or specific components should be organized in a directory structure
outside the source code that mirrors the package structure. This makes it easy for users to find tests relevant to the
specific components they're interested in. It also allows pytest to automatically discover tests when running the tests
using the `pytest` command.

- Each major package should have its own directory under the `tests/` directory
- Subpackages should have their own subdirectories when they contain multiple components
- Additional subdirectories can be used to group tests by functionality.
- Related tests should be grouped together in the same directory
- Filenames should start with descriptive name followed by `_test` (e.g., `name_test.py`).
- Additional files can be used to contain fixtures, test doubles, test base classes, or other test-specific code.

Example:
```
tests/
  bases/                        # Tests for the bases package
    collections/                # Tests for the bases.collections subpackage
      baseobject_test.py
    basecallable_test.py
    sentinelobject_test.py
    ...
  cachingtools/                 # Tests for the cachingtools package
    caches/                     # Tests for the cachingtools.caches subpackage
    cachingobject_test.py
    ...
```


## 4 Test Structure

The purpose of test code is to not only verify that the code is working as expected, but also provide a set of tools for
testing extensions of the code. For example, a class may outline functionality that is not implemented yet or may be
changed in the future, but the test code should still verify that the class is working as expected.

In pytests, tests themselves can be organized into classes and sub-classed which can be used to parameterize tests or
create test suites to verify different implementations of the code.

For creating documentation, follow the general docstring guidelines in [Syntactic Guidelines](syntax.md),
section 2.10, with special attention to section 2.10.1.1 for test modules.


### 4.1 Test Classes

Test classes should be used to group related test methods and even create test suites. Base test classes should be
created to provide consistent testing patterns across the project.

Test classes should inherit from appropriate base test classes to ensure consistent testing patterns across the project.

Guidelines:
- Test classes should inherit from an appropriate base test class/suite
- Test classes should include a descriptive docstring explaining what is being tested
- Test classes should contain most of their resources within their scope so the resource may be changed to suit different test variations.
  - Test involving defining classes should either be defined as inner classes or defined elsewhere and assigned to a class attribute.
  - Test involving defining functions should either be defined as inner functions or defined elsewhere and assigned to a class attribute.

For test method naming and organization, follow the general method guidelines in [Syntactic Guidelines](syntax.md)
and [Code File Layout](code_file_layout.md).


### 4.2 Test Methods

Test methods should be designed to test a specific aspect of the class or function being tested. Each test method should
be focused, independent, and provide clear feedback when it fails.

Guidelines:
- Test methods should be named with a `test_` prefix followed by a descriptive name of what is being tested
- Test methods should include a descriptive docstring explaining what is being tested
- Test methods should use type hints for parameters and return values
- Test methods should be independent and not rely on the state from other tests
- Test methods should be focused on testing a single aspect of behavior
- Test methods should include assertions to verify the expected behavior
- Test methods should handle both normal and edge cases
- Test methods can use attributes provided by the test class (allows more options as a test suite)

Example:
```python
def test_deepcopy(self, test_object: 'TestBaseObject.BaseTestObject') -> None:
    """Test the deep copy behavior of BaseObject.

    This test verifies that deepcopy creates a new object with new mutable attributes
    but the same immutable attributes.

    Args:
        test_object: A fixture providing a BaseTestObject instance.
    """
    # Perform the operation being tested
    new = copy.deepcopy(test_object)

    # Assert the expected behavior
    assert new is not test_object
    assert id(new.immutable) == id(test_object.immutable)
    assert id(new.mutable) != id(test_object.mutable)
    assert new.mutable == test_object.mutable
```

When creating test methods that test similar functionality across different implementations, consider using parameterized tests
to reduce code duplication and ensure consistent testing.


### 4.3 Test Suites

Test suites, in this style guide, are Test Classes designed to function as test suites: a collection of related tests
that validate a specific component, feature, or functionality of the software.

Guidelines:
- Group related test cases together
- Provide common setup and teardown functionality
- Share fixtures and utility methods
- Enable test parameterization
- Allow for extension and reuse
- Maintain consistent testing patterns

Base test suites should be created for common testing patterns, such as:

- Class testing (verifying class instantiation and behavior)
- Performance testing (benchmarking and profiling)
- Integration testing (testing component interactions)
- API testing (verifying interface contracts)

Test suites should be organized hierarchically, with more specific test suites inheriting from more general base test
suites to build up complex testing functionality while maintaining consistent testing patterns. The base hierarchy in
this style guide consists of Base Test Suites and Concrete Test Suites.


#### 4.3.1 Base Test Suites

Base Test Suites are test suites contain a collection of tests for validating a component, feature, or functionality of
the software with a focus on testing general aspects of the component, feature, or functionality.

Typically, a Base Test Suites have a target to test such as `TestClass` or `test_target` and will be composed of
abstract and concrete methods which test the target against various unit tests which the target must pass. Establishing
a test target allows subclassed test suites to interchange test targets to validate. The concrete tests defined in a
Base Test Suite ensure that test targets are tested similarly, while the abstract tests enforce that certain test must
be done, but the implementation of the test can be defined in a more test suite.

It is not required, but the `templatepackage` package provides base test suites which server as a great foundation for test
suites. These classes provide common functionality and ensure consistency across tests.

- `BaseTestSuite`: The abstract base class for all test suites
- `BaseClassTestSuite`: For testing Classes
- `BaseFunctionTestSuite`: For testing Functions
- `BasePerformanceTestSuite`: For testing performance

Guidelines:
- Inherit from test suites which are related to the target
- If there are multiple relevant test suites, then multiple inherit and/or mixin classes should be used
- If there is no relevant test suite to inherit from, then inherit a base test suite
- Ensure there is an attribute that will be the target for testing; it may be defined in a parent test suite
- Ensure the annotations for the test target match what will be tested
- Abstract methods should be used when:
  - The implementation details depend on the specific class or function being tested
  - The test is required for all subclasses, but the implementation varies
  - The test requires specific knowledge about the class or function being tested that can't be generalized
  - The test suite wants to enforce that certain tests must be implemented by subclasses
- Concrete methods should be used when:
  - The implementation can be shared across all subclasses
  - The test behavior is consistent regardless of the specific class or function being tested
  - The test can be implemented in a general way that works for all subclasses
  - The test suite wants to provide a default implementation that subclasses can optionally override
- Generic test suites can be named similar to `BaseOjectTestSuite` where the component being validated should be
  inserted between Base and TestSuite
- Specific test suites which define most of the suite's implementation can be named similar to `ObjectTestSuite` where
  the component being tested is before TestSuite

Example:
```python
# Classes #
class BaseObjectTestSuite(BaseClassTestSuite):
    """Base test suite for children of BaseObject.

    This class provides common test functionality for child class of BaseObject, including tests for copying and
    pickling. Subclasses should set the TestClass attribute and may override or extend the test methods.

    Attributes:
        TestClass: The class that the test suite is testing.
    """

    # Attributes #
    TestClass: Type[BaseObject] | None = None

    # Instance Methods #
    # Fixtures
    @abstractmethod
    @pytest.fixture
    def test_object(self) -> BaseObject:
        """Create a test object."""
        # This is abstract because each subclass needs to create a specific instance
        # of the class being tested, which requires knowledge of that specific class.

    # Tests
    @abstractmethod
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Test that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This is abstract because different classes have different constructor
        # signatures and initialization requirements.

    def test_copy(self, test_object: BaseObject) -> None:
        """Test the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
        """
        # This is a concrete implementation because the copy behavior is consistent
        # across all BaseObject subclasses.
        obj_copy = copy.copy(test_object)
        assert obj_copy is not test_object
        assert isinstance(obj_copy, type(test_object))
        # Additional assertions specific to the BaseObject copy behavior
```


#### 4.3.2 Concrete Test Suites

Concrete Test Suites are subclasses of Base Test Suites and focus on validating tests defined by the Base Test Suite and
creating tests which may pertain only to a specific test target.

Guidelines:
- Should inherit from a Base Test Suite
- Should be named with a `Test` prefix followed by the name of the class or component being tested
- Test classes should contain most of their resources within their scope so the resource may be changed to suit different test variations.
  - Test involving defining classes should either be defined as inner classes or defined elsewhere and assigned to a class attribute.
  - Test involving defining functions should either be defined as inner functions or defined elsewhere and assigned to a class attribute.
- Test classes should define a test target attribute that points to the class being tested such that the tested class
  can interchanged with other similar classes which will be tested using the same test suite.

Example:
```python
# Classes #
class BaseTestObject(BaseObject):
    """A subclass of BaseObject for testing purposes."""
    def __init__(self, x: int = 5):
        self.x = x

# Test Suite #
class TestBaseObject(BaseObjectTestSuite):
    """Test the BaseObject class.

    This class tests the functionality of the BaseObject class, which is the base class for all objects in the
    templatepackage package. It creates a test subclass of BaseObject to test with.
    """

    # Attributes #
    TestClass: Type[BaseObject] | None = TestBaseObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self) -> BaseObject:
        """Create a test object."""
        return self.TestClass(10)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Test that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        instance = self.TestClass()
        assert isinstance(instance, self.TestClass)

    def test_copy(self, test_object: BaseObject) -> None:
        """Test the copy behavior of the object.

        This test verifies that copy creates a new object with the same attributes.

        Args:
            test_object: A fixture providing a test object instance.
        """
        obj_copy = copy.copy(test_object)
        assert obj_copy.x == 10
```


### 4.4 Main

Test files should include a `__main__` block for running the tests directly. Mainly it sets the run options for pytest
for the tests in the file.

Example:
```python
# Main #
if __name__ == "__main__":
    pytest.main(["-v", "-s"])
```


## 5 Test Semantics and Syntax

Tests should conform to the semantics and syntax described in[Semantics Guidelines](semantics.md) and
[Syntactic Guidelines](syntax.md), but in some cases it may be necessary to deviate from the general
guidelines. The following sections describe semantics and syntax which take precedence over the general styleguide.


### 5.1 Assertions

Assertions are a base Python feature that allows for checking the state of a program at runtime and are used by pytest
as the primary means of verifying test conditions. Assertions are discouraged in source code because they do not conform
to Python's error handling principles. However, assertions are permitted for debugging, testing, examples, and tutorials
because assertions are good for explaining the behavior of a program, and in these scenarios error handling
is managed by the user rather than the program.

Guidelines:
- Each test should include at least one assertion
- Assertions should be specific and verify a single aspect of behavior
- Use appropriate assertion methods for the type of comparison being made
- Include descriptive error messages in assertions to make test failures more informative

Example:
```python
# Simple assertions
assert result == expected
assert instance is not None

# More complex assertions
assert id(new.immutable) == id(test_object.immutable)
assert id(new.mutable) != id(test_object.mutable)
assert unpickled.immutable == test_object.immutable
assert unpickled.mutable == test_object.mutable
assert unpickled is not test_object
```


### 5.2 Fixtures

Fixtures are a powerful feature of pytest that allow for setup and teardown of test environments.

Guidelines:
- Fixtures should be used for setting up test environments and creating test objects
- Fixtures should be defined at the appropriate scope (function, class, module, or session)
- Fixtures should include a descriptive docstring explaining their purpose and return value
- Fixtures should use type hints for parameters and return values
- Common fixtures should be defined in base test modules
- Fixtures should be organized under a `# Fixtures` comment

Example:
```python
# Fixtures
@pytest.fixture
def test_object(self) -> 'TestBaseObject.BaseTestObject':
    """Create a test object instance for use in tests.

    Returns:
        BaseTestObject: An instance of the test class.
    """
    return self.class_()

@pytest.fixture
def tmp_dir(tmpdir: Any) -> Path:
    """A pytest fixture that turns the tmpdir into a Path object.

    Args:
        tmpdir: A pytest tmpdir fixture.

    Returns:
        Path: A pathlib.Path object representing the temporary directory.
    """
    return Path(tmpdir)
```

### 5.3 Test Doubles

Test doubles (mocks, stubs, fakes, etc.) are used to isolate the code being tested from its dependencies.

Guidelines:
- Use test doubles to isolate the code being tested from its dependencies
- Use the appropriate type of test double for the situation:
  - Stubs: Return predefined values
  - Mocks: Verify interactions
  - Fakes: Simplified implementations
  - Spies: Record interactions
- Use pytest's monkeypatch fixture for patching functions and methods
- Use unittest.mock for creating mock objects
- Reset or tear down test doubles after use

Example:
```python
def test_with_mock(self, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test with a mock object.

    This test uses a mock object to verify that the correct method is called.

    Args:
        monkeypatch: A pytest fixture for patching functions and methods.
    """
    # Create a mock object
    mock = unittest.mock.Mock()

    # Patch a method to use the mock
    monkeypatch.setattr(self.class_, "some_method", mock)

    # Call the method that should use the patched method
    instance = self.class_()
    instance.method_under_test()

    # Verify the mock was called correctly
    mock.assert_called_once_with(expected_args)
```


## 6 Test Execution

Tests should be easy to run and provide clear feedback on failures.

Guidelines:
- Tests should be runnable using pytest
- Tests should be runnable individually or as part of a test suite
- Tests should provide clear error messages on failure
- Tests should clean up after themselves
- Tests should not depend on the order of execution

Running tests:
```bash
# Run all tests
pytest

# Run tests in a specific file
pytest tests/bases/test_baseobject.py

# Run a specific test
pytest tests/bases/test_baseobject.py::TestBaseObject::test_deepcopy

# Run tests with verbose output
pytest -v

# Run tests with output capturing disabled
pytest -s
```
