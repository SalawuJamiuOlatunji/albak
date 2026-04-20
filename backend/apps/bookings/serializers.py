from rest_framework import serializers
from .models import Booking
from django.utils import timezone


class BookingSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "product",
            "quantity",
            "pickup_date",
            "pickup_time",
            "phone",
            "address",
            "status",
            "total_price",
        ]
        read_only_fields = ["status", "total_price"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than 0")
        if value > 5:
            raise serializers.ValidationError("Maximum booking quantity is 5")
        return value

    def validate(self, data):
        if data["pickup_date"] < timezone.now().date():
            raise serializers.ValidationError(
                "Pickup date cannot be in the past")
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        product = validated_data.get("product")
        quantity = validated_data.get("quantity")

        # check stock
        if quantity > product.stock_quantity:
            raise serializers.ValidationError("Not enough stock")

        total_price = product.price * quantity

        # reduce stock
        product.stock_quantity -= quantity
        product.save()

        booking = Booking.objects.create(
            user=user,
            product=product,
            quantity=quantity,
            pickup_date=validated_data.get("pickup_date"),
            pickup_time=validated_data.get("pickup_time"),
            phone=validated_data.get("phone"),
            address=validated_data.get("address"),
            total_price=total_price,
            **validated_data
        )

        return booking
