from django import forms
from django.forms import TextInput
from .models import UserHotel, Room, Booking
# from django.forms.widgets import SelectDateWidget
from bootstrap_datepicker_plus import DatePickerInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room','startdate','enddate']
        widgets = {'movie': forms.HiddenInput()}
        widgets = {
        'startdate': DatePickerInput(format='%d-%m-%Y'),
        'enddate': DatePickerInput(format='%d-%m-%Y')
        }



# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['name', 'start_date', 'end_date']
#         widgets = {
#             'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
#             'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
#         }