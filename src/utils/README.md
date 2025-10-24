# Math Utilities

A collection of mathematical utility functions for the GigMarket application.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division
- **Advanced Operations**: Power/exponentiation operations
- **Statistical Functions**: Average calculations
- **Business Functions**: Percentage calculations

## Usage

```python
from src.utils.math_utils import add, subtract, multiply, divide, power, percentage, average

# Basic arithmetic
result = add(5, 3)  # 8
result = subtract(10, 4)  # 6
result = multiply(3, 4)  # 12
result = divide(10, 2)  # 5.0

# Advanced operations
result = power(2, 3)  # 8 (2^3)
result = percentage(50, 200)  # 25.0 (50 is 25% of 200)
result = average([1, 2, 3, 4, 5])  # 3.0
```

## Error Handling

The functions include proper error handling:

- `divide()`: Raises `ValueError` when dividing by zero
- `percentage()`: Raises `ValueError` when total is zero
- `average()`: Raises `ValueError` when list is empty

## Testing

Run the test suite:

```bash
pytest tests/test_math_utils.py -v
```

Run with coverage:

```bash
pytest tests/test_math_utils.py --cov=src.utils.math_utils --cov-report=term-missing
```

## API Reference

### add(a, b)
Adds two numbers together.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Sum of a and b

### subtract(a, b)
Subtracts b from a.

**Parameters:**
- `a` (int/float): Number to subtract from
- `b` (int/float): Number to subtract

**Returns:** Difference (a - b)

### multiply(a, b)
Multiplies two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** Product of a and b

### divide(a, b)
Divides a by b.

**Parameters:**
- `a` (int/float): Numerator
- `b` (int/float): Denominator

**Returns:** Quotient (a / b)

**Raises:** `ValueError` if b is zero

### power(base, exponent)
Raises base to the power of exponent.

**Parameters:**
- `base` (int/float): Base number
- `exponent` (int/float): Exponent

**Returns:** base^exponent

### percentage(part, total)
Calculates what percentage 'part' is of 'total'.

**Parameters:**
- `part` (int/float): Part value
- `total` (int/float): Total value

**Returns:** Percentage as float (e.g., 50.0 for 50%)

**Raises:** `ValueError` if total is zero

### average(numbers)
Calculates the average (mean) of a list of numbers.

**Parameters:**
- `numbers` (List[int/float]): List of numbers

**Returns:** Average of all numbers

**Raises:** `ValueError` if list is empty
