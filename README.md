# GigMarket
Connecting Gig seekers with Gig providers

## Overview
GigMarket is a platform designed to connect people seeking gig work with those offering gig opportunities.

## Features

### Math Utilities
The project includes basic math utility functions:

#### `add(a, b)`
Adds two numbers together.

**Parameters:**
- `a` (int or float): First number
- `b` (int or float): Second number

**Returns:**
- (int or float): The sum of a and b

**Raises:**
- `TypeError`: If either argument is not a number (int or float)

**Examples:**
```python
from src.math_utils import add

# Add integers
result = add(2, 3)  # Returns 5

# Add floats
result = add(1.5, 2.5)  # Returns 4.0

# Add negative numbers
result = add(-5, 10)  # Returns 5
```

## Installation

### Requirements
- Python 3.8 or higher

### Setup
1. Clone the repository:
```bash
git clone https://github.com/ProsperNdebel/GigMarket.git
cd GigMarket
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

### Running Tests
```bash
pytest tests/
```

### Running Tests with Coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

## Project Structure
```
GigMarket/
├── src/
│   ├── __init__.py
│   └── math_utils.py      # Basic math utility functions
├── tests/
│   ├── __init__.py
│   └── test_math_utils.py # Tests for math utilities
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Contributing
Contributions are welcome! Please ensure all tests pass before submitting a pull request.

## License
TBD
