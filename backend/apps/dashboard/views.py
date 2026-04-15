from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum

from apps.users.models import User
from apps.products.models import Product
from apps.bookings.models import Booking
from .serializers import DashboardStatsSerializer


class DashboardStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.count()
        total_products = Product.objects.count()
        total_bookings = Booking.objects.count()

        pending_bookings = Booking.objects.filter(
            status="pending"
        ).count()

        completed_bookings = Booking.objects.filter(
            status="completed"
        ).count()

        total_revenue = Booking.objects.filter(
            status="completed"
        ).aggregate(
            total=Sum("total_price")
        )["total"] or Decimal("0.00")

        available_products = Product.objects.filter(
            available=True
        ).count()

        out_of_stock_products = Product.objects.filter(
            available=False
        ).count()

        data = {
            "total_users": total_users,
            "total_products": total_products,
            "total_bookings": total_bookings,
            "pending_bookings": pending_bookings,
            "completed_bookings": completed_bookings,
            "total_revenue": total_revenue,
            "available_products": available_products,
            "out_of_stock_products": out_of_stock_products,
        }

        serializer = DashboardStatsSerializer(data)
        return Response(serializer.data)
