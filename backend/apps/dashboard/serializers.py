from rest_framework import serializers


class DashboardStatsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_products = serializers.IntegerField()
    total_bookings = serializers.IntegerField()
    pending_bookings = serializers.IntegerField()
    completed_bookings = serializers.IntegerField()
    total_revenue = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    available_products = serializers.IntegerField()
    out_of_stock_products = serializers.IntegerField()
