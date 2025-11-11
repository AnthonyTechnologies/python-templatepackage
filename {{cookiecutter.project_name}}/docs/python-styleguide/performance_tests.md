# Anthony's Python Style Guide: Performance Tests

## Table of Contents

- [1 Background](#1-background)
- [2 Directory Hierarchy](#2-directory-hierarchy)
- [3 Performance Test Structure](#3-performance-test-structure)
  - [3.1 Base Performance Classes](#31-base-performance-classes)
  - [3.2 Performance Test Classes](#32-performance-test-classes)
  - [3.3 Test Methods](#33-test-methods)
- [4 Performance Test Semantics and Syntax](#4-performance-test-semantics-and-syntax)
- [5 Common Patterns](#5-common-patterns)
  - [5.1 Comparing with Standard Library](#51-comparing-with-standard-library)
  - [5.2 Comparing Implementation Variants](#52-comparing-implementation-variants)
  - [5.3 Measuring Overhead](#53-measuring-overhead)


## 1 Background

Performance testing is a critical aspect of software development that ensures code not only functions correctly but also
executes efficiently. These tests help identify performance regressions, validate optimizations, and ensure that
implementations meet performance requirements.

The performance tests in this guide are designed around the unit testing framework described in
[Unit Tests](unit_tests.md) as test performance should be tested against individual components of the code similar to
unit tests.

Unlike unit tests that verify functional correctness, performance tests measure execution time, memory usage, and other
performance metrics. They often compare the performance of custom implementations against standard library equivalents
or previous versions to ensure that optimizations are effective and that new features don't introduce performance
regressions.

Performance tests are not required for all modules and classes, but they should be created for any that may have a
significant performance impact.

This document focuses on performance test-specific aspects. For general code organization, file structure, naming
conventions, docstrings, and other standard practices, please refer to:

- [Code File Layout](code_file_layout.md) - For file organization and structure
- [Syntactic Guidelines](syntax.md) - For naming conventions, docstrings, and code formatting
- [Semantics Guidelines](semantics.md) - For general code organization principles
- [Unit Tests](unit_tests.md) - For general testing practices and patterns


### 2 Directory Hierarchy

Performance Tests mostly follow the Unit Test Directory Hierarchy with some differences.

Performance Base Test Suites or performance test suites which cover general implements should be located in the package
source codes under `testsuite`, along with the other unit test suites. Under normal circumstances, test suites should
not be placed in the project source as only developers need test suites; not package users. However, given that PYPI
currently does not support alternate package installations. These test suites should be included in the source to allow
developers using PYPI to expand or create their own test suites.

Example:
```
src/
  baseobjects/                  # The main source package
    testsuite/
      bases/
        __init__.py
        basetestsuite.py
        baseperformancetestsuite.py
        ...
      __init__.py
      objecttestsuite.py
      objectperformancetestsuite.py
      ...
```

Concrete Performance Test and performance test for individual or specific components should follow a specific directory
structure to separate them from regular unit tests:

- Each module should have a corresponding `performance` directory in the `tests` directory
- Performance tests for a module should be placed in the corresponding `performance` directory
- Filenames should start with descriptive name followed by `_performance` (e.g., `name_performance.py`).
- Additional files can be used to contain fixtures, test doubles, performance base classes, or other performance-specific code.

Example:
```
tests/
  bases/                            # Tests for the bases package
    performance/                    # Performance tests for the bases package
      baseobject_performance.py
      basecallable_performance.py
      ...
  cachingtools/
    performance/
      ...
```


## 3 Performance Test Structure

The purpose of performance tests is to not only measure the performance components of the code but also provide a set
of tools for measuring the performance of extensions to the code. The structure of performance tests should follow the
structure described in [Unit Tests](unit_tests.md).


### 3.1 Performance Test Classes

Performance test classes should be used to group related test methods and even create test suites as described in
[Unit Tests](unit_tests.md), section 4.1, with the following additional requirements specific to performance testing:

- Test classes should define comparison objects that match the functionality of the test objects but use standard library or alternative implementations
- Test classes should define performance-specific attributes like `timeit_runs` and `speed_tolerance`


### 3.3 Performance Test Methods

Performance test methods should follow the general test method guidelines in [Unit Tests](unit_tests.md), with the
following additional requirements specific to performance testing:

- Test methods should be focused on measuring a specific performance aspect (speed, memory usage, etc.)
- Test methods should include performance-specific assertions that verify metrics meet requirements
- Test methods should include detailed performance reporting for analysis
- Assert that the percentage comparison is below the threshold
- Use different thresholds for different types of operations if necessary

Example:
```python
def test_copy_speed(self, test_object: "TestBaseObject.BaseTestObject") -> None:
    """Test the performance of the copy method of BaseObject.

    This test compares the speed of BaseObject.copy() with the standard copy.copy() function.

    Args:
        test_object: A fixture providing a BaseTestObject instance.
    """
    normal = self.NormalObject()

    def normal_copy() -> None:
        copy.copy(normal)

    # Calculate the mean time in microseconds for the new implementation
    new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    mean_new = new_time / self.timeit_runs * 1000000

    # Calculate the mean time in microseconds for the old implementation
    old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
    mean_old = old_time / self.timeit_runs * 1000000
    percent = (mean_new / mean_old) * 100

    # Print the performance comparison
    print(f"\nNew: {mean_new:.3f} μs ({percent:.3f}% of old function time)")
    assert percent < self.speed_tolerance
```


### 3.3 Performance Test Suites

Performance Test Suites, in this style guide, are Test Classes designed to function as test suites: a collection of
related tests that assay the performance of a specific component, feature, or functionality of the software. Performance
Test Suites should follow the general test suite guidelines in [Unit Tests](unit_tests.md).

Test suites should be organized hierarchically, with more specific test suites inheriting from more general base test
suites to build up complex testing functionality while maintaining consistent testing patterns. The base hierarchy in
this style guide consists of Base Performance Test Suites and Concrete Test Suites.


#### 3.3.1 Base Performance Test Suites

Base Performance Test Suites are test suites contain a collection of tests assaying the performance of a component,
feature, or functionality of the software with a focus on testing general aspects of the component, feature, or
functionality. Generally, Base Performance Test Suites follow the guidelines in [Unit Tests](unit_tests.md).

As in [Unit Test](unit_tests.md), a Base Performance Test Suites have a target to test such as `TestClass` or
`test_target` and will be composed of abstract and concrete methods which test the target against various unit tests
which the target must pass. Establishing a test target allows subclassed test suites to interchange test targets to
assay performance.

The concrete performance tests defined in a Base Performance Test Suites ensure that test targets are
tested similarly, while the abstract tests enforce that certain test must be done, but the implementation of the test
can be defined in a more specific test suite.

Abstract methods should be used when:
- The implementation details depend on the specific class or function being tested
- The test is required for all subclasses, but the implementation varies
- The test requires specific knowledge about the class or function being tested that can't be generalized
- The test suite wants to enforce that certain tests must be implemented by subclasses

Concrete methods should be used when:
- The implementation can be shared across all subclasses
- The test behavior is consistent regardless of the specific class or function being tested
- The test can be implemented in a general way that works for all subclasses
- The test suite wants to provide a default implementation that subclasses can optionally override

It is not required, but the `baseobjects` package provides base performance test suites which server as a great
foundation for performance test suites. These classes provide common functionality and ensure consistency across
performance tests.

- `BasePerformanceTestSuite`: The abstract base class for performance tests


Additional Guidelines:
- Generic test suites can be named similar to `BaseOjectPerformanceTestSuite` where the component being validated
  should be inserted between Base and PerformanceTestSuite
- Specific test suites which define most of the suite's implementation can be named similar to
  `ObjectPerformanceTestSuite` where the component being tested is before PerformanceTestSuite

Example:
```python
class WrapperPerformanceTestSuite(BasePerformanceTestSuite, BaseClassTestSuite):
    """A base test suite which assays the performance of wrapper classes.

    This is a base test suite that concrete subclasses should implement abstract methods and assign attributes.

    Attributes:
        ExampleOne: A class which the wrapper class will wrap.
        ExampleTwo: A another class which the wrapper class will wrap.
        _base_time: The time it takes to run a simple function call for a baseline of 100 million iterations.
        call_speed: The baseline speed of a simple function call in microseconds.
        timeit_runs: The number of runs to use for timeit measurements.
        speed_tolerance: The maximum percentage of time a new implementation can take compared to the old one.
        TestClass: The main wrapper class to be assayed.
    """
     # Class Definitions #
    class ExampleOne:
        """An example class for testing wrappers.

        This class has attributes and methods that can be wrapped by wrapper classes.
        """
        def __init__(self) -> None:
            """Initialize with attributes."""
            self.one = "one"
            self.two = "one"
            self.common = "example_one"

        def __eq__(self, other: Any) -> bool:
            """Always return True for equality comparison."""
            return True

        def method(self) -> str:
            """Return a string identifying this class.

            Returns:
                A string identifying this class.
            """
            return "one"

        def __str__(self) -> str:
            """Return a string representation of this class."""
            return "ExampleOne"

    class ExampleTwo:
        """Another example class for testing wrappers.

        This class has different attributes and methods than ExampleOne.
        """
        def __init__(self) -> None:
            """Initialize with attributes."""
            self.one = "two"
            self.three = "two"
            self.common = "example_two"

        def function(self) -> str:
            """Return a string identifying this class.

            Returns:
                A string identifying this class.
            """
            return "two"

        def __str__(self) -> str:
            """Return a string representation of this class."""
            return "ExampleTwo"

    # Attributes #
    speed_tolerance: int = 150

    TestClass: Any = None

    # Instance Methods #
    # Fixtures
    @abstractmethod
    @pytest.fixture
    def test_object(self) -> Any:
        """Create a test object.

        Returns:
            A wrapper object with ExampleOne and ExampleTwo objects.
        """
        # This is abstract because each subclass needs to create a specific instance
        # of the wrapper class being tested, which requires knowledge of that specific class.

    @pytest.fixture
    def test_example_one(self) -> ExampleOne:
        """Create a test ExampleOne object.

        Returns:
            An ExampleOne object.
        """
        # This is concrete because it can be implemented in a general way that works
        # for all subclasses. The ExampleOne class is defined in this test suite.
        return self.ExampleOne()

    @pytest.fixture
    def test_example_two(self) -> ExampleTwo:
        """Create a test ExampleTwo object.

        Returns:
            An ExampleTwo object.
        """
        # This is concrete because it can be implemented in a general way that works
        # for all subclasses. The ExampleTwo class is defined in this test suite.
        return self.ExampleTwo()

    # Tests
    @abstractmethod
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Test that instances of the class can be created.

        This is an abstract method that must be implemented by subclasses.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This is abstract because different wrapper classes have different constructor
        # signatures and initialization requirements.

    def test_attribute_access_speed(self, test_wrapper: Any, test_example_one: ExampleOne) -> None:
        """Test the performance of attribute access through DynamicWrapper.

        This test compares the speed of accessing attributes through DynamicWrapper with direct attribute access.

        Args:
            test_wrapper: A fixture providing a DynamicWrapperTestObject.
            test_example_one: A fixture providing an ExampleOne object.
        """
        # This is concrete because the attribute access performance test can be implemented
        # in a general way that works for all wrapper classes. The test measures the overhead
        # of accessing attributes through the wrapper compared to direct access, which is a
        # common performance concern for all wrapper classes.
        def wrapper_access() -> None:
            _ = test_wrapper.one
            _ = test_wrapper.two
            _ = test_wrapper.common

        def direct_access() -> None:
            _ = test_example_one.one
            _ = test_example_one.two
            _ = test_example_one.common

        # Calculate the mean time in microseconds for the wrapper access
        new_time = timeit.timeit(wrapper_access, number=self.timeit_runs)
        mean_new = new_time / self.timeit_runs * 1000000

        # Calculate the mean time in microseconds for direct access
        old_time = timeit.timeit(direct_access, number=self.timeit_runs)
        mean_old = old_time / self.timeit_runs * 1000000
        percent = (mean_new / mean_old) * 100

        # Print the performance comparison
        print(f"\n{self.TestClass.__name__} attribute access: {mean_new:.3f} μs ({percent:.3f}% of direct access time)")
        assert percent < self.speed_tolerance

```


#### 3.3.2 Concrete Performance Classes

Concrete Performance Test Suites are subclasses of Base Performance Test Suites and focus on validating tests defined by
the Base Performance Test Suite and creating tests which may pertain only to a specific test target. Concrete
Performance Test Suites follow the guidelines in [Unit Tests](unit_tests.md).

Additional Guidelines:
- Should inherit from a Base Performance Test Suite
- Should be named with a `Performance` suffix

Example:
```python
# Classes #
ExampleOne = WrapperPerformanceTestSuite.ExampleOne
ExampleTwo = WrapperPerformanceTestSuite.ExampleTwo

class DynamicWrapperTestObject(DynamicWrapper):
    """A test class that inherits from DynamicWrapper.

    This class uses DynamicWrapper to wrap ExampleOne and ExampleTwo objects.
    """
    _wrapped = ["_first", "_second"]

    def __init__(self, first: ExampleOne | None = None, second: ExampleTwo | None = None) -> None:
        """Initialize with wrapped objects.

        Args:
            first: The first object to wrap.
            second: The second object to wrap.
        """
        self._first = first
        self._second = second
        self.two = "wrapper"
        self.four = "wrapper"

    def wrap(self) -> str:
        """Return a string identifying this class.

        Returns:
            A string identifying this class.
        """
        return "wrapper"


class TestDynamicWrapperPerformance(WrapperPerformanceTestSuite):
    """A base test suite which assays the performance of wrapper classes.

    This is a base test suite that concrete subclasses should implement abstract methods and assign attributes.

    Attributes:
        ExampleOne: A class which the wrapper class will wrap.
        ExampleTwo: A another class which the wrapper class will wrap.
        _base_time: The time it takes to run a simple function call for a baseline of 100 million iterations.
        call_speed: The baseline speed of a simple function call in microseconds.
        timeit_runs: The number of runs to use for timeit measurements.
        speed_tolerance: The maximum percentage of time a new implementation can take compared to the old one.
        TestClass: The main wrapper class to be assayed.
    """

    # Attributes #
    speed_tolerance: int = 150
    TestClass: Any = DynamicWrapperTestObject

    # Instance Methods #
    # Fixtures
    @pytest.fixture
    def test_object(self) -> Any:
        """Create a test object.

        Returns:
            A wrapper object with ExampleOne and ExampleTwo objects.
        """
        # This concrete implementation satisfies the abstract fixture requirement from the parent class.
        # It provides a specific implementation for creating a DynamicWrapperTestObject instance.
        # The implementation is specific to this test suite because it knows how to create and
        # initialize a DynamicWrapperTestObject with the appropriate wrapped objects.
        first = self.ExampleOne()
        second = self.ExampleTwo()
        return self.DynamicWrapperTestObject(first, second)

    # Tests
    def test_instance_creation(self, *args: Any, **kwargs: Any) -> None:
        """Test that instances of the class can be created.

        Args:
            *args: Positional arguments list to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.
        """
        # This concrete implementation satisfies the abstract method requirement from the parent class.
        # It provides a specific implementation for testing DynamicWrapperTestObject instance creation.
        # The implementation is specific to this test suite because it knows the constructor signature
        # and initialization requirements of the DynamicWrapperTestObject class.
        instance = self.TestClass()
        assert isinstance(instance, self.TestClass)

    def test_setattr_vs_normal_set_speed(self, test_wrapper: DynamicWrapperTestObject) -> None:
        """Test the performance difference between _setattr and normal attribute setting.

        This test compares the speed of setting attributes using _setattr with normal attribute setting.

        Args:
            test_wrapper: A fixture providing a DynamicWrapperTestObject.
        """
        # This is a concrete method that is specific to this test suite and not required by the parent class.
        # It tests a specific feature of the DynamicWrapperTestObject class (_setattr method) that may not
        # be present in all wrapper classes. This shows how concrete test suites can add additional tests
        # that are specific to the class being tested.
        def setattr_method() -> None:
            test_wrapper._setattr("one", "test")

        def normal_set() -> None:
            test_wrapper.one = "test"

        # Calculate the mean time in microseconds for _setattr
        new_time = timeit.timeit(setattr_method, number=self.timeit_runs)
        mean_new = new_time / self.timeit_runs * 1000000

        # Calculate the mean time in microseconds for normal set
        old_time = timeit.timeit(normal_set, number=self.timeit_runs)
        mean_old = old_time / self.timeit_runs * 1000000
        percent = (mean_new / mean_old) * 100

        # Print the performance comparison
        print(f"\n_setattr method: {mean_new:.3f} μs ({percent:.3f}% of normal set time)")
        # No assertion here, just measuring relative performance

```


## 4 Performance Test Semantics and Syntax

Performance Tests should conform to the semantics and syntax described in[Semantics Guidelines](semantics.md)
and [Syntactic Guidelines](syntax.md), but in some cases it may be necessary to deviate from the general
guidelines. The following sections describe semantics and syntax which take precedence over the general styleguide.


### 4.1 Benchmarking

Performance tests should use the `timeit` module for benchmarking. The following guidelines should be followed:

- Use the `timeit` module for measuring execution time
- Use a sufficient number of iterations to get reliable measurements (defined in `timeit_runs`)
- Report times in microseconds for better readability
- Calculate and report the percentage comparison between implementations


### 4.2 Comparison Methodology

Performance tests should compare the performance of custom implementations against standard library equivalents or other reference implementations:

- Define functions that perform equivalent operations using different implementations
- Ensure that the compared operations are truly equivalent
- Use the same input data for all implementations
- Isolate the specific operation being tested

Example:
```python
def normal_copy() -> None:
    copy.copy(normal)

# vs.

test_object.copy()
```

### 4.3 Measurement and Reporting

Performance measurements should be accurate, consistent, and informative:

- Use the `timeit` module with a sufficient number of iterations
- Calculate mean execution time per operation
- Convert times to microseconds for better readability
- Calculate and report the percentage comparison between implementations
- Print detailed performance information for debugging

Example:
```python
# Calculate the mean time in microseconds for the new implementation
new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
mean_new = new_time / self.timeit_runs * 1000000

# Calculate the mean time in microseconds for the old implementation
old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
mean_old = old_time / self.timeit_runs * 1000000
percent = (mean_new / mean_old) * 100

# Print the performance comparison
print(f"\nNew: {mean_new:.3f} μs ({percent:.3f}% of old function time)")
```

## 5 Common Patterns
### 5.1 Comparing with Standard Library

A common pattern is to compare the performance of custom implementations against standard library equivalents:

```python
def test_copy_speed(self, test_object):
    """Test the performance of the copy method of BaseObject."""
    normal = self.NormalObject()

    def normal_copy():
        copy.copy(normal)

    # Compare custom implementation with standard library
    new_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    old_time = timeit.timeit(normal_copy, number=self.timeit_runs)
    # ...
```

### 5.2 Comparing Implementation Variants

Another pattern is to compare different implementation variants:

```python
def test_copy_vs_dunder_copy(self, test_object):
    """Test the performance difference between copy() and __copy__() methods."""
    # Compare two different implementations
    copy_time = timeit.timeit(test_object.copy, number=self.timeit_runs)
    dunder_time = timeit.timeit(test_object.__copy__, number=self.timeit_runs)
    # ...
```

### 5.3 Measuring Overhead

Performance tests can also measure the overhead of additional functionality:

```python
def test_attribute_access_speed(self, test_object):
    """Test the performance of attribute access in BaseObject."""
    normal = self.NormalObject()

    def access_base_attr():
        _ = test_object.immutable
        _ = test_object.mutable

    def access_normal_attr():
        _ = normal.immutable
        _ = normal.mutable

    # Measure overhead of BaseObject attribute access
    base_time = timeit.timeit(access_base_attr, number=self.timeit_runs)
    normal_time = timeit.timeit(access_normal_attr, number=self.timeit_runs)
    # ...
```

By following these guidelines, developers can create effective performance tests that help ensure the efficiency and reliability of the codebase.
