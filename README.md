# GigMarket
Connecting Gig seekers with Gig providers

## Overview
GigMarket is a platform designed to connect gig seekers with gig providers, facilitating efficient matching and collaboration in the gig economy.

## Features

### Utility Functions
- **Math Operations**: Basic mathematical utilities including addition operations

## Project Structure
```
GigMarket/
├── utils/
│   ├── __init__.py
│   └── math_operations.py    # Mathematical utility functions
├── tests/
│   ├── __init__.py
│   └── test_math_operations.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

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

## Usage

### Math Operations
```python
from utils import add

# Add two numbers
result = add(5, 3)  # Returns 8

# Works with floats
result = add(2.5, 3.5)  # Returns 6.0

# Works with negative numbers
result = add(-5, 10)  # Returns 5
```

## Development

### Running Tests
Run the test suite using pytest:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=utils tests/
```

### Code Quality
- Type hints are used throughout the codebase
- Comprehensive test coverage for all functions
- Clear documentation and examples

## Contributing
1. Create a feature branch from `main`
2. Implement your changes with tests
3. Ensure all tests pass
4. Submit a pull request

## License
TBD
