from django.urls import path
from .views import (
    BookingCreateView,
    UserBookingHistoryView,
    AdminBookingListView,
    BookingStatusUpdateView,
    BookingCancelView
)

urlpatterns = [
    path("create/", BookingCreateView.as_view()),
    path("history/", UserBookingHistoryView.as_view()),
    path("all/", AdminBookingListView.as_view()),
    path("<int:pk>/status/", BookingStatusUpdateView.as_view()),
    path("<int:pk>/cancel/", BookingCancelView.as_view(), name="booking-cancel"),
]
