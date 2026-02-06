# Contributing to ITP 326 Visual Reference Library

Thank you for your interest in contributing! This project aims to make visual reference management easier for educational Custom GPTs.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. Check if the issue already exists in [Issues](https://github.com/kdlin/itp-326-agent/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, Git version)

### Suggesting Enhancements

We welcome suggestions for:

- New auto-categorization rules
- Additional image formats
- Improved AI description prompts
- Better markdown templates
- Integration with other Custom GPT platforms

### Pull Requests

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   ```bash
   python upload_visuals_final.py
   ```
   - Verify images upload correctly
   - Check markdown generation
   - Test GitHub push

5. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of what you changed"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Include screenshots if applicable

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/itp-326-agent.git
   cd itp-326-agent
   ```

2. Install dependencies:
   ```bash
   pip install gitpython pyyaml pillow
   ```

3. Configure your test environment:
   - Create a test folder for screenshots
   - Update script paths to point to test locations
   - Use a test GitHub repository

## Coding Guidelines

### Python Style

- Follow PEP 8 style guide
- Use descriptive variable names
- Add docstrings for functions
- Keep functions focused and single-purpose

### Example:

```python
def detect_folder(filename):
    """
    Auto-detect which folder based on filename keywords
    
    Args:
        filename (str): The image filename to categorize
        
    Returns:
        str: Either 'examples' or 'reference'
    """
    lower = filename.lower()
    # Implementation...
```

### Commit Messages

Use clear, imperative commit messages:

- ✅ "Add support for .webp image format"
- ✅ "Fix folder detection for files with double underscores"
- ✅ "Update README with troubleshooting section"
- ❌ "Fixed stuff"
- ❌ "Update"

## Areas for Contribution

### High Priority

- [ ] Add support for additional image formats (.webp, .svg)
- [ ] Improve error handling and logging
- [ ] Add unit tests for core functions
- [ ] Create example configuration templates

### Medium Priority

- [ ] Add CLI arguments for script configuration
- [ ] Support multiple output markdown formats
- [ ] Add batch processing for large image sets
- [ ] Improve AI description prompt templates

### Low Priority

- [ ] Add progress bars for long operations
- [ ] Create GUI version of the script
- [ ] Add support for video references
- [ ] Integration with other AI platforms

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion in [Discussions](https://github.com/kdlin/itp-326-agent/discussions)
- Contact [@kdlin](https://github.com/kdlin)

## Code of Conduct

Be respectful, constructive, and collaborative. This is an educational project meant to help students and educators.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping improve this project! 🎉
