from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "size",
        "price",
        "previous_price",
        "stock_quantity",
        "available",
        "updated_at",
    )
    search_fields = ("name", "size")
    list_filter = ("size", "available", "updated_at")
