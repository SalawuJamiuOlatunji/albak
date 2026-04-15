from rest_framework import generics, permissions
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
