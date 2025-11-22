# Code Style Guide - TechNest

## Python Code Standards

### General Principles
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Keep functions small and focused (single responsibility)
- Add docstrings to all functions and classes
- Maximum line length: 100 characters

### Naming Conventions
```python
# Classes: PascalCase
class ProductReview:
    pass

# Functions/Methods: snake_case
def get_cart_items():
    pass

# Constants: UPPER_SNAKE_CASE
MAX_CART_ITEMS = 100

# Variables: snake_case
user_email = "user@example.com"
```

### Import Organization
```python
# Standard library imports
import os
from pathlib import Path

# Third-party imports
from django.shortcuts import render
from django.contrib.auth import login

# Local imports
from .models import Product, Cart
from .utils import CartService
```

### Function Documentation
```python
def calculate_discount(order_total, coupon):
    """
    Calculate discount amount for an order.
    
    Args:
        order_total (Decimal): Total order amount
        coupon (Coupon): Coupon object to apply
        
    Returns:
        Decimal: Calculated discount amount
        
    Raises:
        ValueError: If order_total is negative
    """
    if order_total < 0:
        raise ValueError("Order total cannot be negative")
    return coupon.calculate_discount(order_total)
```

## JavaScript Code Standards

### General Principles
- Use ES6+ features
- Prefer `const` over `let`, avoid `var`
- Use arrow functions for callbacks
- Add JSDoc comments for functions

### Naming Conventions
```javascript
// Classes: PascalCase
class ToastManager {}

// Functions: camelCase
function showToast() {}

// Constants: UPPER_SNAKE_CASE
const MAX_TOASTS = 5;

// Variables: camelCase
const userName = "John";
```

### Function Documentation
```javascript
/**
 * Display a toast notification
 * @param {string} message - Message to display
 * @param {string} type - Toast type (success, error, warning, info)
 * @param {number} duration - Display duration in milliseconds
 * @returns {HTMLElement} The created toast element
 */
function showToast(message, type = 'info', duration = 3000) {
    // Implementation
}
```

## CSS Code Standards

### General Principles
- Use CSS custom properties (variables)
- Follow BEM naming convention for classes
- Group related properties together
- Add comments for complex sections

### Naming Conventions
```css
/* BEM: block__element--modifier */
.product-card {}
.product-card__title {}
.product-card__title--featured {}

/* Use kebab-case for class names */
.toast-notification {}
.btn-futuristic {}
```

### Property Organization
```css
.element {
    /* Positioning */
    position: relative;
    top: 0;
    left: 0;
    
    /* Display & Box Model */
    display: flex;
    width: 100%;
    padding: 1rem;
    margin: 0;
    
    /* Typography */
    font-size: 1rem;
    color: white;
    
    /* Visual */
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-md);
    
    /* Animation */
    transition: all 0.3s ease;
}
```

## Django Template Standards

### General Principles
- Use template inheritance
- Keep logic minimal in templates
- Use template tags and filters appropriately
- Add comments for complex sections

### Template Structure
```django
{% extends 'base.html' %}
{% load static %}

{% block title %}Page Title{% endblock %}

{% block content %}
    {# Main content here #}
    <div class="container">
        {% if user.is_authenticated %}
            <p>Welcome, {{ user.username }}!</p>
        {% else %}
            <p>Please log in.</p>
        {% endif %}
    </div>
{% endblock %}

{% block extra_scripts %}
    <script src="{% static 'js/custom.js' %}"></script>
{% endblock %}
```

## Git Commit Messages

### Format
```
type: brief description

Detailed explanation (optional)

- Bullet points for changes (optional)
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat: add toast notification system

Implemented elegant toast notifications to replace alert() calls.
- Created toast CSS and JS files
- Integrated into base template
- Replaced all alert() calls

fix: resolve logout HTTP 405 error

Changed logout link to POST form to comply with Django's LogoutView requirements.

docs: update README with installation instructions
```

## File Organization

### Python Files
- Keep related functionality together
- Separate concerns (models, views, forms, utils)
- Use meaningful file names

### Template Files
- One template per page/view
- Use partials for reusable components
- Keep templates in logical folders

### Static Files
```
static/
├── css/
│   ├── base/           # Base styles
│   ├── components/     # Component styles
│   └── pages/          # Page-specific styles
├── js/
│   ├── core/           # Core functionality
│   ├── components/     # Component scripts
│   └── utils/          # Utility functions
└── images/
    ├── products/       # Product images
    └── ui/             # UI elements
```

## Code Review Checklist

### Before Committing
- [ ] Code follows style guide
- [ ] All functions have docstrings
- [ ] No console.log() or print() statements (except for debugging)
- [ ] No commented-out code
- [ ] Variables have meaningful names
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Tests pass
- [ ] No linting errors

### Security Checks
- [ ] No hardcoded secrets or passwords
- [ ] CSRF tokens present in forms
- [ ] User input is validated
- [ ] SQL injection prevention (use ORM)
- [ ] XSS prevention (template escaping)

## Performance Best Practices

### Django
- Use `select_related()` and `prefetch_related()` for queries
- Add database indexes for frequently queried fields
- Use caching for expensive operations
- Paginate large querysets

### Frontend
- Minimize HTTP requests
- Compress and minify CSS/JS
- Optimize images
- Use lazy loading for images
- Defer non-critical JavaScript

## Testing Standards

### Test Structure
```python
class ProductModelTest(TestCase):
    """Test suite for Product model"""
    
    def setUp(self):
        """Set up test data"""
        self.category = Category.objects.create(
            name='Electronics',
            slug='electronics'
        )
    
    def test_product_creation(self):
        """Test creating a product"""
        product = Product.objects.create(
            name='Test Product',
            desc='Test Description',
            price=99.99,
            category=self.category
        )
        self.assertEqual(product.name, 'Test Product')
        self.assertTrue(product.is_active)
```

### Test Coverage
- Aim for 80%+ code coverage
- Test edge cases
- Test error handling
- Test user permissions

---

**Remember**: Clean code is not just about following rules, it's about writing code that others (including future you) can easily understand and maintain.
