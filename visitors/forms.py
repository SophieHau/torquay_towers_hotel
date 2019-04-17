from django import forms
from django.forms import TextInput
from .models import UserHotel, Room, Booking
from bootstrap_datepicker_plus import DatePickerInput

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room','startdate','enddate']
        widgets = {
            'startdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'enddate': DatePickerInput(format='%d-%m-%Y'), # specify date-frmat
        }

