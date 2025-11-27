# Contributing to Porter Neural Network Delivery Time Prediction

First off, thank you for considering contributing to this project! 🎉

The following is a set of guidelines for contributing to the Porter NN project. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. Please be respectful and constructive in all interactions.

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, Node version)

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear use case** and motivation
- **Detailed description** of the proposed functionality
- **Possible implementation** approach (if you have ideas)
- **Alternative solutions** you've considered

### 🔧 Code Contributions

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** as needed
5. **Submit a pull request**

---

## Development Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/PORTER_NN.git
cd PORTER_NN

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Run backend
cd backend
uvicorn main:app --reload
```

### Frontend Setup

```bash
# Install dependencies
cd frontend
npm install

# Run development server
npm run dev
```

---

## Coding Standards

### Python (Backend)

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Write **docstrings** for functions and classes
- Keep functions **focused and small**
- Use **meaningful variable names**

Example:
```python
def predict_delivery_time(order_data: dict) -> float:
    """
    Predict delivery time for a given order.
    
    Args:
        order_data: Dictionary containing order features
        
    Returns:
        Predicted delivery time in minutes
    """
    # Implementation
    pass
```

### JavaScript/React (Frontend)

- Use **ESLint** configuration provided
- Follow **React best practices**
- Use **functional components** and hooks
- Keep components **small and reusable**
- Use **meaningful component and variable names**

Example:
```jsx
const PredictionForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({});
  
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };
  
  return (
    // JSX
  );
};
```

### General Guidelines

- **DRY Principle**: Don't Repeat Yourself
- **KISS Principle**: Keep It Simple, Stupid
- **Write tests** for new features
- **Comment complex logic** but prefer self-documenting code
- **Remove debugging code** before committing

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
feat(backend): add caching for model predictions

Implement Redis caching to reduce prediction latency for
frequently requested order patterns.

Closes #123
```

```bash
fix(frontend): correct form validation for negative values

Previously, the form allowed negative values for total_items.
Added validation to ensure all numeric inputs are positive.

Fixes #456
```

---

## Pull Request Process

### Before Submitting

1. ✅ **Test your changes** locally
2. ✅ **Update documentation** if needed
3. ✅ **Follow coding standards**
4. ✅ **Write meaningful commit messages**
5. ✅ **Ensure no merge conflicts** with main branch

### PR Template

When creating a pull request, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested your changes

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
```

### Review Process

1. At least **one maintainer review** required
2. All **CI checks must pass**
3. **Resolve all review comments**
4. Maintainer will **merge** when approved

---

## Development Workflow

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation
- `refactor/description` - Code refactoring

### Example Workflow

```bash
# Create feature branch
git checkout -b feature/add-traffic-integration

# Make changes and commit
git add .
git commit -m "feat(backend): integrate traffic API"

# Push to your fork
git push origin feature/add-traffic-integration

# Create pull request on GitHub
```

---

## Testing Guidelines

### Backend Tests

```bash
# Run tests
pytest backend/tests/

# With coverage
pytest --cov=backend backend/tests/
```

### Frontend Tests

```bash
# Run tests
npm test

# With coverage
npm test -- --coverage
```

---

## Questions?

Feel free to:
- 💬 Open a **discussion** for general questions
- 🐛 Create an **issue** for bugs or feature requests
- 📧 Contact the maintainer: **ratnesh.kumar@example.com**

---

## Recognition

Contributors will be recognized in:
- **README.md** acknowledgments section
- **Release notes** for significant contributions
- **GitHub contributors** page

---

Thank you for contributing! 🚀

**Happy Coding!** 💻
