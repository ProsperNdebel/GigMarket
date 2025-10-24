"""Simple test file for hello functionality."""

import pytest


def hello(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet (default: "World")
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def test_hello_default():
    """Test hello function with default parameter."""
    assert hello() == "Hello, World!"


def test_hello_with_name():
    """Test hello function with custom name."""
    assert hello("Alice") == "Hello, Alice!"


def test_hello_with_empty_string():
    """Test hello function with empty string."""
    assert hello("") == "Hello, !"


def test_hello_with_special_characters():
    """Test hello function with special characters."""
    assert hello("José") == "Hello, José!"


if __name__ == "__main__":
    # Allow running the test file directly
    pytest.main([__file__, "-v"])
