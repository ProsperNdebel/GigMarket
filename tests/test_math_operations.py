"""
Test suite for math_operations module.
"""

import pytest
from utils.math_operations import add


class TestAdd:
    """Test cases for the add function."""
    
    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(100, 200) == 300
    
    def test_add_negative_integers(self):
        """Test adding negative integers."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30
    
    def test_add_positive_and_negative(self):
        """Test adding positive and negative integers."""
        assert add(5, -3) == 2
        assert add(-5, 10) == 5
        assert add(10, -10) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)
        assert add(0.1, 0.2) == pytest.approx(0.3)
    
    def test_add_mixed_int_float(self):
        """Test adding integers and floats."""
        assert add(2, 3.5) == 5.5
        assert add(2.5, 3) == 5.5
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_large_numbers(self):
        """Test adding large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(1.5e10, 2.5e10) == 4.0e10
    
    def test_add_invalid_first_argument(self):
        """Test that TypeError is raised for invalid first argument."""
        with pytest.raises(TypeError, match="First argument must be a number"):
            add("5", 3)
        
        with pytest.raises(TypeError, match="First argument must be a number"):
            add(None, 3)
        
        with pytest.raises(TypeError, match="First argument must be a number"):
            add([1, 2], 3)
    
    def test_add_invalid_second_argument(self):
        """Test that TypeError is raised for invalid second argument."""
        with pytest.raises(TypeError, match="Second argument must be a number"):
            add(5, "3")
        
        with pytest.raises(TypeError, match="Second argument must be a number"):
            add(5, None)
        
        with pytest.raises(TypeError, match="Second argument must be a number"):
            add(5, [1, 2])
    
    def test_add_both_invalid_arguments(self):
        """Test that TypeError is raised when both arguments are invalid."""
        with pytest.raises(TypeError, match="First argument must be a number"):
            add("5", "3")
