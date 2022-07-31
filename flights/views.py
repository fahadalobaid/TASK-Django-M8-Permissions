import datetime

from rest_framework import generics

from flights import serializers
from flights.models import Booking, Flight
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission


class FlightsList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class BookingsList(generics.ListAPIView):
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = datetime.date.today()
        return Booking.objects.filter(user=self.request.user, date__gte=today)


class BookingDetails(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateBooking(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.AdminUpdateBookingSerializer

        return serializers.UpdateBookingSerializer


class CancelBooking(generics.DestroyAPIView,BasePermission):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"
    permission_classes = [IsAuthenticated, IsAdminUser]
    message = "You must be the author of this article."

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.author == request.user

class BookFlight(generics.CreateAPIView):
    serializer_class = serializers.AdminUpdateBookingSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user, flight_id=self.kwargs["flight_id"])


class Register(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
