from django.db import models


class Product(models.Model):
    CYLINDER_SIZES = [
        ("3kg", "3kg"),
        ("6kg", "6kg"),
        ("12kg", "12kg"),
        ("25kg", "25kg"),
        ("50kg", "50kg"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=CYLINDER_SIZES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    stock_quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.available = self.stock_quantity > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.size}"
