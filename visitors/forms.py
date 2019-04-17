from django import forms
from django.forms import TextInput
from .models import UserHotel, Room, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room','startdate','enddate']
    