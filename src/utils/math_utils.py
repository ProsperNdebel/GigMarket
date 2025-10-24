"""
Math utility functions for GigMarket application.

This module provides common mathematical operations used throughout
the application, including basic arithmetic, power operations,
percentages, and statistical calculations.
"""

from typing import List, Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
        >>> add(-5, 10)
        5
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract b from a.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        Difference of a and b (a - b)

    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(5, 10)
        -5
        >>> subtract(-5, -3)
        -2
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2.5, 2)
        5.0
        >>> multiply(-5, 3)
        -15
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a and b (a / b)

    Raises:
        ValueError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """
    Raise base to the power of exponent.

    Args:
        base: Base number
        exponent: Exponent to raise base to

    Returns:
        base raised to the power of exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 2)
        25
        >>> power(2, -1)
        0.5
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent


def percentage(part: Union[int, float], total: Union[int, float]) -> float:
    """
    Calculate what percentage 'part' is of 'total'.

    Args:
        part: The part value
        total: The total value

    Returns:
        Percentage as a float (e.g., 50.0 for 50%)

    Raises:
        ValueError: If total is zero

    Examples:
        >>> percentage(50, 100)
        50.0
        >>> percentage(25, 100)
        25.0
        >>> percentage(150, 100)
        150.0
        >>> percentage(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: Total cannot be zero
    """
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (part / total) * 100


def average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average (mean) of a list of numbers.

    Args:
        numbers: List of numbers to average

    Returns:
        Average of all numbers in the list

    Raises:
        ValueError: If the list is empty

    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([10, 20, 30])
        20.0
        >>> average([-5, 0, 5])
        0.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: Cannot calculate average of empty list
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
