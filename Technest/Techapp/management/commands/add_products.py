from django.core.management.base import BaseCommand
from Techapp.models import Product, Category
from decimal import Decimal


class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **kwargs):
        # Create categories if they don't exist
        categories_data = [
            {'name': 'Smartphones', 'slug': 'smartphones'},
            {'name': 'Laptops', 'slug': 'laptops'},
            {'name': 'Tablets', 'slug': 'tablets'},
            {'name': 'Accessories', 'slug': 'accessories'},
            {'name': 'Wearables', 'slug': 'wearables'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']}
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Sample products
        products_data = [
            {
                'name': 'iPhone 15 Pro Max',
                'desc': 'The latest flagship smartphone from Apple with A17 Pro chip, titanium design, and advanced camera system.',
                'price': Decimal('1199.99'),
                'stock': 25,
                'category': 'smartphones',
            },
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'desc': 'Premium Android smartphone with S Pen, 200MP camera, and AI-powered features.',
                'price': Decimal('1299.99'),
                'stock': 18,
                'category': 'smartphones',
            },
            {
                'name': 'Google Pixel 8 Pro',
                'desc': 'Google\'s flagship with advanced AI photography, pure Android experience, and Tensor G3 chip.',
                'price': Decimal('999.99'),
                'stock': 30,
                'category': 'smartphones',
            },
            {
                'name': 'MacBook Pro 16" M3',
                'desc': 'Powerful laptop with M3 Pro chip, stunning Liquid Retina XDR display, and all-day battery life.',
                'price': Decimal('2499.99'),
                'stock': 12,
                'category': 'laptops',
            },
            {
                'name': 'Dell XPS 15',
                'desc': 'Premium Windows laptop with InfinityEdge display, Intel Core i9, and NVIDIA RTX graphics.',
                'price': Decimal('1899.99'),
                'stock': 15,
                'category': 'laptops',
            },
            {
                'name': 'ThinkPad X1 Carbon',
                'desc': 'Business ultrabook with legendary keyboard, military-grade durability, and lightweight design.',
                'price': Decimal('1599.99'),
                'stock': 20,
                'category': 'laptops',
            },
            {
                'name': 'iPad Pro 12.9"',
                'desc': 'The ultimate iPad experience with M2 chip, Liquid Retina XDR display, and Apple Pencil support.',
                'price': Decimal('1099.99'),
                'stock': 22,
                'category': 'tablets',
            },
            {
                'name': 'Samsung Galaxy Tab S9+',
                'desc': 'Premium Android tablet with AMOLED display, S Pen included, and DeX desktop mode.',
                'price': Decimal('899.99'),
                'stock': 16,
                'category': 'tablets',
            },
            {
                'name': 'AirPods Pro (2nd Gen)',
                'desc': 'Premium wireless earbuds with active noise cancellation, spatial audio, and adaptive transparency.',
                'price': Decimal('249.99'),
                'stock': 50,
                'category': 'accessories',
            },
            {
                'name': 'Sony WH-1000XM5',
                'desc': 'Industry-leading noise canceling headphones with exceptional sound quality and 30-hour battery.',
                'price': Decimal('399.99'),
                'stock': 35,
                'category': 'accessories',
            },
            {
                'name': 'Logitech MX Master 3S',
                'desc': 'Advanced wireless mouse with ergonomic design, customizable buttons, and multi-device support.',
                'price': Decimal('99.99'),
                'stock': 45,
                'category': 'accessories',
            },
            {
                'name': 'Apple Watch Series 9',
                'desc': 'Advanced smartwatch with always-on Retina display, health tracking, and seamless iPhone integration.',
                'price': Decimal('399.99'),
                'stock': 28,
                'category': 'wearables',
            },
            {
                'name': 'Samsung Galaxy Watch 6',
                'desc': 'Feature-rich smartwatch with advanced health monitoring, long battery life, and Wear OS.',
                'price': Decimal('299.99'),
                'stock': 24,
                'category': 'wearables',
            },
            {
                'name': 'Fitbit Charge 6',
                'desc': 'Fitness tracker with built-in GPS, heart rate monitoring, and 7-day battery life.',
                'price': Decimal('159.99'),
                'stock': 40,
                'category': 'wearables',
            },
        ]

        created_count = 0
        for product_data in products_data:
            category_slug = product_data.pop('category')
            product_data['category'] = categories[category_slug]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully added {created_count} new products!'))
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {Product.objects.count()}'))
