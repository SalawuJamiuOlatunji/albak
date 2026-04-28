from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate

from apps.users.models import User
from apps.products.models import Product
from apps.bookings.models import Booking


class DashboardStatsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_users = User.objects.count()
        total_products = Product.objects.count()
        total_bookings = Booking.objects.count()

        # Daily revenue
        daily_revenue = (
            Booking.objects.filter(status="completed")
            .annotate(date=TruncDate("created_at"))
            .values("date")
            .annotate(total=Sum("total_price"))
            .order_by("date")
        )

        # Top selling products
        top_products = (
            Booking.objects.values("product__name", "product__size")
            .annotate(total_sold=Sum("quantity"))
            .order_by("-total_sold")[:5]
        )

        # Bookings per day
        daily_bookings = (
            Booking.objects.annotate(date=TruncDate("created_at"))
            .values("date")
            .annotate(count=Count("id"))
            .order_by("date")
        )

        # Status distribution
        status_stats = (
            Booking.objects.values("status")
            .annotate(count=Count("id"))
        )

        pending_bookings = Booking.objects.filter(status="pending").count()
        completed_bookings = Booking.objects.filter(status="completed").count()

        total_revenue = (
            Booking.objects.filter(status="completed")
            .aggregate(total=Sum("total_price"))["total"] or Decimal("0.00")
        )

        available_products = Product.objects.filter(available=True).count()
        out_of_stock_products = Product.objects.filter(available=False).count()

        return Response({
            "summary": {
                "total_users": total_users,
                "total_products": total_products,
                "total_bookings": total_bookings,
                "pending_bookings": pending_bookings,
                "completed_bookings": completed_bookings,
                "total_revenue": total_revenue,
                "available_products": available_products,
                "out_of_stock_products": out_of_stock_products,
            },
            "analytics": {
                "daily_revenue": list(daily_revenue),
                "top_products": list(top_products),
                "daily_bookings": list(daily_bookings),
                "status_distribution": list(status_stats),
            }
        })
