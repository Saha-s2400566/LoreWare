# TechNest - Modern E-Commerce Platform

<div align="center">

![TechNest Logo](static/images/logo.png)

**A futuristic, feature-rich e-commerce platform built with Django**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

**TechNest** is a modern, futuristic e-commerce platform designed for selling technology products. Built with Django and featuring a stunning glassmorphic UI with neon accents, TechNest provides a premium shopping experience with cutting-edge features.

### Key Highlights

- 🎨 **Futuristic Design** - Glassmorphism, neon accents, and smooth animations
- 🔐 **Secure Authentication** - Custom user system with password strength validation
- 🛒 **Shopping Cart** - Real-time cart management with AJAX
- 📱 **Responsive** - Mobile-first design that works on all devices
- ⚡ **Performance** - Optimized with loading skeletons and lazy loading
- 🎯 **UX Focused** - Toast notifications, breadcrumbs, and intuitive navigation

---

## ✨ Features

### Current Features (Phase 1 Complete)

#### 🔔 Toast Notifications
- Elegant, non-intrusive notifications
- 4 types: Success, Error, Warning, Info
- Auto-dismiss with smooth animations
- Glassmorphic design matching site theme

#### 💪 Password Strength Meter
- Real-time password validation
- Visual strength indicator (Weak/Medium/Strong)
- Requirement checklist with live updates
- Color-coded feedback

#### 🧭 Breadcrumb Navigation
- Auto-generated from URL structure
- Clickable navigation links
- Consistent across all pages

#### 📧 Newsletter Signup
- Email subscription form
- AJAX validation
- Toast notifications on success/error
- Positioned before footer on all pages

#### ⏳ Loading Skeletons
- Animated placeholders during data loading
- Shimmer effect for better UX
- Reduces perceived load time

#### 🛍️ Core E-Commerce Features
- Product catalog with categories
- Shopping cart functionality
- User authentication (Sign up/Sign in)
- Product search and filtering
- Responsive product cards
- Stock management

#### 🎨 UI/UX Features
- Futuristic glassmorphic design
- Neon cyan accent colors
- Smooth animations and transitions
- Dark theme optimized
- Cookie consent banner
- Mobile-responsive navigation

### Upcoming Features (Planned)

#### Phase 2: Database & Infrastructure
- Wishlist system
- Product reviews & ratings
- Enhanced order management
- Coupon system
- Multiple user addresses

#### Phase 3: Advanced Features
- Social authentication (Google, Facebook, GitHub)
- Two-factor authentication (2FA)
- Email verification
- User profile dashboard
- Order tracking

#### Phase 4: Payment & Checkout
- Stripe payment integration
- Guest checkout
- Multiple payment methods
- Tax & shipping calculations
- Order confirmation emails

#### Phase 5: Admin & Analytics
- Admin dashboard with charts
- Sales analytics
- Inventory management
- Customer insights
- Report generation

#### Phase 6: Performance & SEO
- Progressive Web App (PWA)
- Redis caching
- API endpoints (REST)
- SEO optimization
- Image compression

---

## 📸 Screenshots

### Homepage
![Homepage](static/images/screenshots/homepage.png)

### Product Catalog
![Products Page](static/images/screenshots/products.png)

### Shopping Cart
![Cart Page](static/images/screenshots/cart.png)

### Sign Up with Password Strength Meter
![Sign Up](static/images/screenshots/signup.png)

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Django 4.0+** - Web framework
- **SQLite** - Database (development)
- **Pillow** - Image processing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (Glassmorphism, animations)
- **JavaScript (ES6+)** - Interactivity
- **jQuery** - DOM manipulation
- **Bootstrap 4** - Grid system (customized)
- **Font Awesome** - Icons

### Design
- **Glassmorphic UI** - Modern, translucent design
- **Neon Accents** - Cyan (#00F0FF) and Electric Blue (#007BFF)
- **Custom Animations** - Smooth transitions and effects
- **Responsive Design** - Mobile-first approach

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Virtual Environment** (recommended)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/technest.git
cd technest
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install django pillow
```

**Required Packages:**
- `Django>=4.0` - Web framework
- `Pillow>=9.0` - Image processing for product images

#### 4. Configure Database

Run migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create Superuser

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set:
- Username
- Email address
- Password

#### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

#### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

---

## ⚙️ Configuration

### Environment Variables

For production, create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost/dbname

# Email Settings (for future features)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Media Files
MEDIA_URL=/media/
MEDIA_ROOT=media/
```

### Database Configuration

**Development (SQLite - Default):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**Production (PostgreSQL - Recommended):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'technest_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📖 Usage

### Accessing the Application

1. **Homepage:** http://127.0.0.1:8000/
2. **Products:** http://127.0.0.1:8000/products/
3. **Cart:** http://127.0.0.1:8000/cart/
4. **Sign Up:** http://127.0.0.1:8000/sign-up/
5. **Sign In:** http://127.0.0.1:8000/sign-in/
6. **Admin Panel:** http://127.0.0.1:8000/admin/

### Adding Products

1. Log in to the admin panel: http://127.0.0.1:8000/admin/
2. Navigate to **Products** → **Add Product**
3. Fill in the product details:
   - Name
   - Description
   - Price
   - Category
   - Stock quantity
   - Upload product image
4. Click **Save**

### Managing Users

**Admin Panel:**
- Navigate to **Users** in the admin panel
- View, edit, or delete user accounts
- Assign staff/superuser permissions

**User Registration:**
- Users can sign up at: http://127.0.0.1:8000/sign-up/
- Password strength meter ensures secure passwords
- Email and phone number optional

### Shopping Cart

**Adding Items:**
- Click "Add to Cart" on any product
- Toast notification confirms addition
- Cart counter updates in real-time

**Managing Cart:**
- View cart at: http://127.0.0.1:8000/cart/
- Update quantities
- Remove items
- View total with tax calculation

---

## 📁 Project Structure

```
Technest/
│
├── Techapp/                    # Main Django app
│   ├── migrations/             # Database migrations
│   ├── __init__.py
│   ├── admin.py               # Admin panel configuration
│   ├── apps.py
│   ├── forms.py               # Custom forms (signup, login)
│   ├── models.py              # Database models (User, Product, Cart)
│   ├── services.py            # Business logic (CartService)
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App URL routing
│   └── views.py               # View functions
│
├── Technest/                   # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py
│
├── static/                     # Static files
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   ├── futuristic-theme.css    # Main theme styles
│   │   ├── quick-wins.css          # Toast, skeletons, etc.
│   │   ├── responsive.css
│   │   └── style.css
│   ├── js/
│   │   ├── jquery.min.js
│   │   ├── popper.min.js
│   │   └── quick-wins.js           # Toast manager, password strength
│   └── images/
│       ├── loading.gif
│       └── ...
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template (navbar, footer)
│   ├── index.html             # Homepage
│   ├── products.html          # Product catalog
│   ├── cart.html              # Shopping cart
│   ├── sign_up.html           # Registration
│   ├── sign_in.html           # Login
│   ├── about.html             # About page
│   ├── contact.html           # Contact page
│   └── policy.html            # Privacy policy
│
├── media/                      # User-uploaded files
│   └── products/              # Product images
│
├── db.sqlite3                 # SQLite database (development)
├── manage.py                  # Django management script
└── README.md                  # This file
```

---

## 🎯 Key Files Explained

### Models (`Techapp/models.py`)

**CustomUser:**
- Extends Django's AbstractUser
- Additional fields: date_of_birth, phone_number
- Custom groups and permissions

**Product:**
- name, description, price
- image, category, stock
- created_at, updated_at, is_active
- Automatic timestamp management

**Cart:**
- Links user to products
- Quantity tracking
- Foreign key relationships

### Views (`Techapp/views.py`)

- `index` - Homepage with featured products
- `products` - Product catalog with cart quantities
- `cart_view` - Shopping cart with total calculation
- `add_to_cart` - AJAX endpoint for adding items
- `sign_up` - User registration with validation
- `sign_in` - User authentication

### Services (`Techapp/services.py`)

**CartService:**
- `add_to_cart()` - Add/update cart items
- `get_cart_items()` - Retrieve user's cart
- `remove_from_cart()` - Delete cart items
- `clear_cart()` - Empty entire cart
- `get_cart_total()` - Calculate total price

---

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run specific tests:

```bash
python manage.py test Techapp.tests.TestProductModel
```

---

## 🔒 Security Features

- **CSRF Protection** - All forms include CSRF tokens
- **Password Hashing** - Django's built-in PBKDF2 algorithm
- **Password Strength Validation** - Real-time client-side checking
- **SQL Injection Protection** - Django ORM prevents SQL injection
- **XSS Protection** - Template auto-escaping enabled
- **Secure Cookies** - SameSite=Lax for cookie security

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up static file serving (WhiteNoise or CDN)
- [ ] Configure email backend
- [ ] Set strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Set up backup strategy
- [ ] Configure logging
- [ ] Run security checks: `python manage.py check --deploy`

### Recommended Hosting

- **Heroku** - Easy deployment with Git
- **DigitalOcean** - VPS with full control
- **AWS** - Scalable cloud hosting
- **PythonAnywhere** - Simple Django hosting

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- Font Awesome Icons
- Glassmorphism Design Inspiration

---

## 📞 Support

For support, email support@technest.com or open an issue in the GitHub repository.

---

## 🗺️ Roadmap

See the [Implementation Plan](docs/implementation_plan.md) for detailed feature roadmap.

**Coming Soon:**
- ✨ Wishlist functionality
- ⭐ Product reviews and ratings
- 💳 Stripe payment integration
- 📧 Email verification
- 🔐 Two-factor authentication
- 📊 Admin analytics dashboard
- 🌐 Multi-language support
- 📱 Progressive Web App (PWA)

---

<div align="center">

**Made with ❤️ using Django**

[Report Bug](https://github.com/yourusername/technest/issues) · [Request Feature](https://github.com/yourusername/technest/issues)

</div>
