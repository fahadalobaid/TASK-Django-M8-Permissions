from datetime import datetime

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from .models import Booking, Flight
from .serializers import (
    AdminUpdateBookingSerializer,
    BookingDetailsSerializer,
    BookingSerializer,
    FlightSerializer,
    RegisterSerializer,
    UpdateBookingSerializer,
)


class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingsList(ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user, date__gte=datetime.today()
        )


class BookingDetails(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class UpdateBooking(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdminUpdateBookingSerializer
        else:
            return UpdateBookingSerializer


class CancelBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookFlight(CreateAPIView):
    serializer_class = AdminUpdateBookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs["flight_id"])


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
