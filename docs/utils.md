# Utils Module Documentation

## Overview
The `utils.py` module provides utility functions for the GigMarket application.

## Functions

### `add(a, b)`

A basic addition function that adds two numbers together.

**Parameters:**
- `a` (int | float): First number to add
- `b` (int | float): Second number to add

**Returns:**
- `int | float`: The sum of a and b

**Raises:**
- `TypeError`: If either argument is not a number (int or float)

**Examples:**

```python
from utils import add

# Adding integers
result = add(2, 3)  # Returns 5

# Adding floats
result = add(1.5, 2.5)  # Returns 4.0

# Adding negative numbers
result = add(-5, 10)  # Returns 5

# Adding with zero
result = add(0, 5)  # Returns 5
```

**Edge Cases Handled:**
- Positive and negative numbers
- Floating point numbers
- Zero values
- Large numbers
- Type validation (raises TypeError for invalid types)

## Testing

Run the test suite with:

```bash
pytest tests/test_utils.py -v
```

The tests cover:
- Adding positive numbers
- Adding negative numbers
- Adding mixed positive/negative
- Adding with zero
- Floating point arithmetic
- Large numbers
- Type validation errors
