from django.contrib import admin

from flights.models import Booking, Flight

to_register = [
    Booking,
    Flight,
]

admin.site.register(to_register)
