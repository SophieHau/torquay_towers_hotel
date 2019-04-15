from django.contrib import admin
from .models import UserHotel, Room, Booking

# to do: register models for Admin app to use

# Register your models here.

admin.site.register(UserHotel)
admin.site.register(Room)
admin.site.register(Booking)
