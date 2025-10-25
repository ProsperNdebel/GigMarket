"""
Tests for basic math utility functions.
"""
import pytest
from src.math_utils import add


class TestAddFunction:
    """Test suite for the add function."""

    def test_add_two_positive_integers(self):
        """Test adding two positive integers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(1, 1) == 2

    def test_add_two_negative_integers(self):
        """Test adding two negative integers."""
        assert add(-2, -3) == -5
        assert add(-10, -20) == -30
        assert add(-1, -1) == -2

    def test_add_positive_and_negative_integers(self):
        """Test adding positive and negative integers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(10, -10) == 0

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)
        assert add(-1.5, 2.5) == 1.0

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(999999999, 1) == 1000000000

    def test_add_multiple_types(self):
        """Test adding integers and floats."""
        assert add(1, 2.5) == 3.5
        assert add(2.5, 1) == 3.5

    def test_add_type_error(self):
        """Test that adding non-numeric types raises TypeError."""
        with pytest.raises(TypeError):
            add("1", 2)
        with pytest.raises(TypeError):
            add(1, "2")
        with pytest.raises(TypeError):
            add(None, 5)
        with pytest.raises(TypeError):
            add([1], 2)
