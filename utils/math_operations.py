"""
Mathematical operations utility module.

This module provides basic mathematical operations for the GigMarket application.
"""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Raises:
        TypeError: If either argument is not a number
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
        >>> add(-5, 10)
        5
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, got {type(a).__name__}")
    
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, got {type(b).__name__}")
    
    return a + b
