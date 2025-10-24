"""
Unit tests for math_utils module.

Tests cover basic mathematical operations including:
- Addition
- Subtraction
- Multiplication
- Division
- Power operations
- Percentage calculations
"""

import pytest
from src.utils.math_utils import (
    add,
    subtract,
    multiply,
    divide,
    power,
    percentage,
    average,
)


class TestBasicOperations:
    """Test basic arithmetic operations."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(0, 5) == 5

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-5, -3) == -8
        assert add(-5, 10) == 5
        assert add(5, -5) == 0

    def test_add_floats(self):
        """Test addition with floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(10, 5) == 5
        assert subtract(5, 10) == -5
        assert subtract(0, 5) == -5

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-5, 3) == -8
        assert subtract(5, -5) == 10

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50
        assert multiply(0, 5) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-5, -3) == 15
        assert multiply(-5, 3) == -15
        assert multiply(5, -5) == -25

    def test_multiply_floats(self):
        """Test multiplication with floating point numbers."""
        assert multiply(2.5, 2) == 5.0
        assert multiply(0.5, 0.5) == 0.25

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero(self):
        """Test division by zero raises appropriate error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test zero divided by a number."""
        assert divide(0, 5) == 0.0


class TestAdvancedOperations:
    """Test advanced mathematical operations."""

    def test_power_positive_exponent(self):
        """Test power with positive exponents."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponents."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01

    def test_power_fractional_exponent(self):
        """Test power with fractional exponents."""
        assert power(4, 0.5) == 2.0
        assert power(27, 1/3) == pytest.approx(3.0)

    def test_percentage_basic(self):
        """Test basic percentage calculations."""
        assert percentage(50, 100) == 50.0
        assert percentage(25, 100) == 25.0
        assert percentage(100, 200) == 50.0

    def test_percentage_zero_total(self):
        """Test percentage with zero total raises error."""
        with pytest.raises(ValueError, match="Total cannot be zero"):
            percentage(10, 0)

    def test_percentage_greater_than_hundred(self):
        """Test percentage can be greater than 100."""
        assert percentage(150, 100) == 150.0

    def test_average_positive_numbers(self):
        """Test average of positive numbers."""
        assert average([1, 2, 3, 4, 5]) == 3.0
        assert average([10, 20, 30]) == 20.0
        assert average([5]) == 5.0

    def test_average_mixed_numbers(self):
        """Test average with mixed positive and negative numbers."""
        assert average([-5, 0, 5]) == 0.0
        assert average([-10, 10, 5, -5]) == 0.0

    def test_average_empty_list(self):
        """Test average with empty list raises error."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            average([])

    def test_average_floats(self):
        """Test average with floating point numbers."""
        assert average([1.5, 2.5, 3.5]) == pytest.approx(2.5)
        assert average([0.1, 0.2, 0.3]) == pytest.approx(0.2)
