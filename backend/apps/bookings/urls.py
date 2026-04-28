from django.urls import path
from .views import (
    BookingCreateView,
    UserBookingHistoryView,
    AdminBookingListView,
    BookingStatusUpdateView,
    BookingCancelView,
    BookingUpdateStatusView
)

urlpatterns = [
    path("create/", BookingCreateView.as_view()),
    path("history/", UserBookingHistoryView.as_view()),
    path("all/", AdminBookingListView.as_view()),
    path("<int:pk>/status/", BookingStatusUpdateView.as_view()),
    path("<int:pk>/cancel/", BookingCancelView.as_view(), name="booking-cancel"),
    path("<int:pk>/update-status/", BookingUpdateStatusView.as_view(), name="booking-update-status"),
]
