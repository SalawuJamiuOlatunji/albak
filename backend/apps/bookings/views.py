from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserBookingHistoryView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user
        ).select_related("product")


class AdminBookingListView(generics.ListAPIView):
    queryset = Booking.objects.select_related(
        "user", "product"
    ).all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]


class BookingStatusUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]


class BookingCancelView(APIView):
    def post(self, request, pk):
        try:
            booking = Booking.objects.get(id=pk, user=request.user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)

        if booking.status == "cancelled":
            return Response({"error": "Already cancelled"}, status=400)
        if booking.status == "confirmed":
            return Response({"error": "Cannot cancel confirmed booking"}, status=400)

        # restore stock
        product = booking.product
        product.stock_quantity += booking.quantity
        product.save()

        booking.status = "cancelled"
        booking.save()

        return Response({"message": "Booking cancelled successfully"})
