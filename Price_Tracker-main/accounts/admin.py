
from django.contrib import admin
from .models import Product, Price, PriceAlert, SeasonalPattern

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'marketplace', 'price', 'timestamp')
    list_filter = ('marketplace', 'timestamp')
    search_fields = ('product__name',)

@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'target_price', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')

@admin.register(SeasonalPattern)
class SeasonalPatternAdmin(admin.ModelAdmin):
    list_display = ('product_category', 'best_month', 'worst_month', 'price_drop_percentage')
