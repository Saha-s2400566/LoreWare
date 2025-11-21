from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from Techapp.models import Product
import urllib.request
import os


class Command(BaseCommand):
    help = 'Add placeholder images to products'

    def handle(self, *args, **kwargs):
        # Mapping of product names to image URLs (using placeholder service)
        # Using picsum.photos for placeholder images
        products_images = {
            'iPhone 15 Pro Max': 'https://picsum.photos/400/400?random=1',
            'Samsung Galaxy S24 Ultra': 'https://picsum.photos/400/400?random=2',
            'Google Pixel 8 Pro': 'https://picsum.photos/400/400?random=3',
            'MacBook Pro 16" M3': 'https://picsum.photos/400/400?random=4',
            'Dell XPS 15': 'https://picsum.photos/400/400?random=5',
            'ThinkPad X1 Carbon': 'https://picsum.photos/400/400?random=6',
            'iPad Pro 12.9"': 'https://picsum.photos/400/400?random=7',
            'Samsung Galaxy Tab S9+': 'https://picsum.photos/400/400?random=8',
            'AirPods Pro (2nd Gen)': 'https://picsum.photos/400/400?random=9',
            'Sony WH-1000XM5': 'https://picsum.photos/400/400?random=10',
            'Logitech MX Master 3S': 'https://picsum.photos/400/400?random=11',
            'Apple Watch Series 9': 'https://picsum.photos/400/400?random=12',
            'Samsung Galaxy Watch 6': 'https://picsum.photos/400/400?random=13',
            'Fitbit Charge 6': 'https://picsum.photos/400/400?random=14',
        }

        updated_count = 0
        for product_name, image_url in products_images.items():
            try:
                product = Product.objects.get(name=product_name)
                
                # Skip if product already has an image
                if product.image:
                    self.stdout.write(self.style.WARNING(f'Product already has image: {product_name}'))
                    continue

                # Download image
                self.stdout.write(f'Downloading image for: {product_name}...')
                response = urllib.request.urlopen(image_url)
                image_content = response.read()

                # Create filename
                filename = f"{product_name.replace(' ', '_').replace('\"', '')}.jpg"
                
                # Save image to product
                product.image.save(filename, ContentFile(image_content), save=True)
                updated_count += 1
                
                self.stdout.write(self.style.SUCCESS(f'✓ Added image to: {product_name}'))
                
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product not found: {product_name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error adding image to {product_name}: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully added images to {updated_count} products!'))
