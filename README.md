# GigMarket
Connecting Gig seekers with Gig providers

## Setup

### Prerequisites
- Python 3.12 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ProsperNdebel/GigMarket.git
cd GigMarket
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Features

### Utils Module

The `utils.py` module provides basic utility functions:

- **`add(a, b)`**: Adds two numbers together with type validation

Example usage:
```python
from utils import add

result = add(5, 10)  # Returns 15
```

For detailed documentation, see [docs/utils.md](docs/utils.md)

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run tests with coverage:

```bash
pytest tests/ --cov=. --cov-report=html
```

## Project Structure

```
GigMarket/
├── README.md              # Project overview
├── requirements.txt       # Python dependencies
├── utils.py              # Utility functions
├── docs/                 # Documentation
│   └── utils.md         # Utils module documentation
└── tests/               # Test suite
    ├── __init__.py
    └── test_utils.py    # Tests for utils module
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

[Add your license here]
