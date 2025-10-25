"""
Tests for utility functions.
"""
import pytest
from utils import add


class TestAddFunction:
    """Test cases for the add function."""

    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_two_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -15) == -25

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        assert add(10, -5) == 5
        assert add(-10, 5) == -5

    def test_add_with_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1000000, 2000000) == 3000000

    def test_add_with_invalid_types(self):
        """Test that add raises TypeError for invalid types."""
        with pytest.raises(TypeError):
            add("string", 5)
        with pytest.raises(TypeError):
            add(5, None)
        with pytest.raises(TypeError):
            add([], 5)
