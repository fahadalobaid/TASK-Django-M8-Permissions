from django.contrib import admin

from .models import Booking, Flight

admin.site.register(Flight)
admin.site.register(Booking)
