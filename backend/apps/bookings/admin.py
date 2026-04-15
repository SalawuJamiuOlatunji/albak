from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product",
        "quantity",
        "total_price",
        "pickup_date",
        "pickup_time",
        "status",
        "created_at",
    )
    search_fields = (
        "user__username",
        "product__name",
        "phone",
    )
    list_filter = (
        "status",
        "pickup_date",
        "created_at",
    )
    ordering = ("-created_at",)
