from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set',
        blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']

    @property
    def total_price(self):
        return self.quantity * self.product.price

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name}"

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    @property
    def total_price(self):
        return self.quantity * self.product.price
