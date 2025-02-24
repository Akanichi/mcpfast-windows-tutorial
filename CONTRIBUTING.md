# Contributing to MCP Fast Windows Tutorial

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine
3. **Create a new branch** for your changes
4. **Make your changes** following the coding standards
5. **Test your changes** thoroughly
6. **Commit your changes** with clear, descriptive commit messages
7. **Push your changes** to your fork
8. **Submit a pull request** to the main repository

## Development Environment

We recommend using uv for Python package management:

```bash
# Create and activate a virtual environment
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Install dependencies
uv pip install -r requirements.txt
```

## Coding Standards

- Follow PEP 8 style guidelines
- Include docstrings for all functions, classes, and modules
- Add type hints to function signatures
- Keep functions focused and small
- Write clear, descriptive variable and function names

## Testing

Before submitting a pull request, please test your changes:

1. Test your MCP server with the MCP Inspector
2. Verify that your server works with Claude Desktop
3. Check that your code runs on different platforms (if possible)

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the examples if you've added new features
3. Ensure your code follows the project's coding standards
4. Your pull request will be reviewed by the maintainers

## Adding Examples

If you're adding a new example:

1. Place it in the `examples/` directory
2. Include comprehensive comments
3. Update the README.md to mention the new example
4. Ensure it works with the latest version of MCP and Claude Desktop

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License. 