from django.contrib import admin
from .models import (
    Product, CustomUser, Cart, Category, Wishlist, 
    ProductReview, Order, OrderItem, Coupon, 
    NewsletterSubscription, UserAddress
)
from django.contrib.auth.admin import UserAdmin


# ==================== CATEGORY ADMIN ====================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


# ==================== PRODUCT ADMIN ====================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'sale_price', 'stock', 'featured', 'on_sale', 'is_active')
    list_filter = ('category', 'is_active', 'featured', 'on_sale', 'created_at')
    search_fields = ('name', 'desc', 'sku')
    ordering = ('-created_at',)
    list_editable = ('price', 'sale_price', 'stock', 'featured', 'on_sale', 'is_active')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'desc', 'sku', 'category')
        }),
        ('Pricing', {
            'fields': ('price', 'on_sale', 'sale_price')
        }),
        ('Inventory', {
            'fields': ('stock', 'image')
        }),
        ('Status', {
            'fields': ('is_active', 'featured')
        }),
    )


# ==================== CUSTOMUSER ADMIN ====================
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'phone_number')
        }),
    )


# ==================== CART ADMIN ====================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at', 'subtotal')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-added_at',)
    readonly_fields = ('added_at', 'subtotal')


# ==================== WISHLIST ADMIN ====================
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)


# ==================== PRODUCT REVIEW ADMIN ====================
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'title', 'is_approved', 'is_verified_purchase', 'created_at')
    list_filter = ('rating', 'is_approved', 'is_verified_purchase', 'created_at')
    search_fields = ('product__name', 'user__username', 'title', 'comment')
    ordering = ('-created_at',)
    list_editable = ('is_approved',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Review Information', {
            'fields': ('product', 'user', 'rating', 'title', 'comment')
        }),
        ('Status', {
            'fields': ('is_approved', 'is_verified_purchase')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ==================== ORDER ITEM INLINE ====================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('subtotal',)
    fields = ('product', 'quantity', 'price', 'subtotal')


# ==================== ORDER ADMIN ====================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'customer_email', 'status', 'payment_status', 'total', 'created_at')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('order_number', 'user__username', 'guest_email', 'guest_name')
    ordering = ('-created_at',)
    list_editable = ('status', 'payment_status')
    readonly_fields = ('order_number', 'created_at', 'updated_at', 'customer_email', 'customer_name')
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'user', 'guest_email', 'guest_name', 'status', 'payment_status')
        }),
        ('Pricing', {
            'fields': ('subtotal', 'tax', 'shipping_cost', 'discount', 'total', 'coupon')
        }),
        ('Shipping Address', {
            'fields': ('shipping_address', 'shipping_city', 'shipping_state', 'shipping_zip', 'shipping_country')
        }),
        ('Billing Address', {
            'fields': ('billing_address', 'billing_city', 'billing_state', 'billing_zip', 'billing_country'),
            'classes': ('collapse',)
        }),
        ('Payment', {
            'fields': ('payment_method', 'transaction_id')
        }),
        ('Additional', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ==================== ORDER ITEM ADMIN ====================
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal')
    list_filter = ('order__created_at',)
    search_fields = ('order__order_number', 'product__name')
    readonly_fields = ('subtotal',)


# ==================== COUPON ADMIN ====================
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'uses_count', 'max_uses', 'valid_from', 'valid_to', 'is_active')
    list_filter = ('discount_type', 'is_active', 'valid_from', 'valid_to')
    search_fields = ('code', 'description')
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    readonly_fields = ('uses_count', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Coupon Details', {
            'fields': ('code', 'description', 'discount_type', 'discount_value')
        }),
        ('Usage Limits', {
            'fields': ('max_uses', 'uses_count', 'max_uses_per_user', 'min_purchase_amount')
        }),
        ('Validity', {
            'fields': ('valid_from', 'valid_to', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# ==================== NEWSLETTER SUBSCRIPTION ADMIN ====================
@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'is_active', 'subscribed_at', 'unsubscribed_at')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email', 'user__username')
    ordering = ('-subscribed_at',)
    list_editable = ('is_active',)
    readonly_fields = ('subscribed_at', 'unsubscribed_at')
    
    actions = ['activate_subscriptions', 'deactivate_subscriptions']
    
    def activate_subscriptions(self, request, queryset):
        queryset.update(is_active=True, unsubscribed_at=None)
        self.message_user(request, f"{queryset.count()} subscriptions activated.")
    activate_subscriptions.short_description = "Activate selected subscriptions"
    
    def deactivate_subscriptions(self, request, queryset):
        from django.utils import timezone
        queryset.update(is_active=False, unsubscribed_at=timezone.now())
        self.message_user(request, f"{queryset.count()} subscriptions deactivated.")
    deactivate_subscriptions.short_description = "Deactivate selected subscriptions"


# ==================== USER ADDRESS ADMIN ====================
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address_type', 'city', 'state', 'is_default')
    list_filter = ('address_type', 'is_default', 'country')
    search_fields = ('user__username', 'full_name', 'city', 'state')
    ordering = ('-is_default', '-created_at')
    list_editable = ('is_default',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User', {
            'fields': ('user', 'address_type', 'is_default')
        }),
        ('Contact Information', {
            'fields': ('full_name', 'phone')
        }),
        ('Address', {
            'fields': ('address_line1', 'address_line2', 'city', 'state', 'zip_code', 'country')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
