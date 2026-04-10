# Contributing to ML MCP Project

Thanks for your interest in contributing! This guide will help you get started.

## 🌟 Ways to Contribute

- **Add ML Models**: Implement support for new model types (PyTorch, TensorFlow, Scikit-learn, etc.)
- **Improve Documentation**: Fix typos, add examples, clarify instructions
- **Bug Fixes**: Report and fix issues
- **Feature Requests**: Suggest new tools or capabilities
- **Tests**: Add test coverage for existing functionality

## 🚀 Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/ml-mcp-project.git
cd ml-mcp-project
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

### 3. Make Changes

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ...

# Format code
black src/ tests/ examples/

# Lint
flake8 src/ tests/ examples/

# Run tests
pytest tests/
```

### 4. Submit Pull Request

1. Commit your changes with clear messages
2. Push to your fork
3. Open a PR with a description of changes
4. Wait for review and feedback

## 📝 Code Style

- **Python**: Follow PEP 8
- **Docstrings**: Use Google-style docstrings
- **Type Hints**: Add type annotations where possible
- **Formatting**: Use `black` for consistent formatting

## 🧪 Testing

All contributions should include tests:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

## 📚 Documentation

- Update README.md if adding new features
- Add docstrings to all public functions/classes
- Include usage examples for new tools

## 🔍 Code Review

Before submitting:

- [ ] Code is formatted with `black`
- [ ] No linting errors from `flake8`
- [ ] Tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear

## 💬 Questions?

Open an issue for questions or discussions!

---

Thanks for contributing! 🎉
