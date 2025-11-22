# TechNest E-Commerce Platform

A modern, futuristic e-commerce platform built with Django, featuring a sleek dark theme and smooth user experience.

## 🚀 Features

- **Modern UI/UX**: Futuristic dark theme with glassmorphism effects
- **Product Management**: Full CRUD operations for products and categories
- **Shopping Cart**: Session-based and database-backed cart system
- **Wishlist System**: Save favorite products for later
- **Product Reviews**: User ratings and reviews with verification
- **Advanced Search**: Filter by category, price range, and search query
- **Toast Notifications**: Smooth, non-blocking notifications
- **Responsive Design**: Mobile-first approach
- **User Authentication**: Custom user model with profile management
- **Order Management**: Complete order processing system

## 📋 Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saha-s2400566/TechNest.git
   cd TechNest
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files** (for production)
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Frontend: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
TechNest/
├── docs/                          # Documentation files
│   ├── README.md
│   ├── TOAST_COMPLETE.md
│   └── TOAST_IMPLEMENTATION.md
├── Techapp/                       # Main application
│   ├── migrations/               # Database migrations
│   ├── models.py                 # Data models
│   ├── views.py                  # View controllers
│   ├── forms.py                  # Form definitions
│   ├── urls.py                   # URL routing
│   ├── utils.py                  # Utility functions
│   └── tests.py                  # Unit tests
├── Technest/                      # Project settings
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Root URL config
│   └── wsgi.py                   # WSGI config
├── templates/                     # HTML templates
│   ├── base.html                 # Base template
│   ├── index.html                # Homepage
│   ├── products.html             # Product listing
│   ├── product_detail.html       # Product details
│   ├── cart.html                 # Shopping cart
│   ├── wishlist.html             # Wishlist
│   ├── checkout.html             # Checkout page
│   ├── sign_in.html              # Login page
│   ├── sign_up.html              # Registration
│   ├── about.html                # About page
│   ├── contact.html              # Contact page
│   └── policy.html               # Privacy policy
├── static/                        # Static files
│   ├── css/                      # Stylesheets
│   │   ├── futuristic-theme.css
│   │   ├── toast-notifications.css
│   │   ├── quick-wins.css
│   │   └── style.css
│   ├── js/                       # JavaScript files
│   │   ├── toast-notifications.js
│   │   └── quick-wins.js
│   └── images/                   # Image assets
├── media/                         # User-uploaded files
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore rules
└── db.sqlite3                    # SQLite database
```

## 🎨 Key Technologies

- **Backend**: Django 5.1.3
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Variables
- **UI Framework**: Bootstrap 5 (minimal usage)
- **Icons**: Font Awesome

## 🔧 Configuration

### Development Settings

Edit `Technest/settings.py`:

```python
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
```

### Production Settings

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# Add whitenoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]
```

## 📊 Database Models

- **CustomUser**: Extended user model with additional fields
- **Category**: Product categories
- **Product**: Product information and inventory
- **Cart**: Shopping cart items
- **Wishlist**: User wishlists
- **ProductReview**: Product ratings and reviews
- **Order**: Order information
- **OrderItem**: Individual order items
- **Coupon**: Discount coupons
- **NewsletterSubscription**: Email subscriptions
- **UserAddress**: Saved user addresses

## 🧪 Testing

Run tests:
```bash
python manage.py test
```

Run specific test:
```bash
python manage.py test Techapp.tests.ProductSortTest
```

## 🚀 Deployment

1. Set environment variables
2. Update `ALLOWED_HOSTS` in settings
3. Set `DEBUG = False`
4. Configure database (PostgreSQL recommended)
5. Run `collectstatic`
6. Use gunicorn or similar WSGI server
7. Set up nginx for static files
8. Enable HTTPS

## 📝 API Endpoints

- `/` - Homepage
- `/products/` - Product listing with filters
- `/product/<id>/` - Product detail page
- `/cart/` - Shopping cart
- `/wishlist/` - User wishlist
- `/checkout/` - Checkout process
- `/add_to_cart/` - Add product to cart (AJAX)
- `/wishlist/add/<id>/` - Toggle wishlist (AJAX)

## 🎯 Features Roadmap

- [ ] Payment gateway integration
- [ ] Email notifications
- [ ] Advanced analytics
- [ ] Product recommendations
- [ ] Multi-language support
- [ ] Social media integration

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is for educational purposes.

## 👥 Authors

- Student ID: WP2404752
- GitHub: [@Saha-s2400566](https://github.com/Saha-s2400566)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- Font Awesome
- Google Fonts

## 📞 Support

For support, email your.email@example.com or open an issue on GitHub.

---

**Built with ❤️ using Django**
