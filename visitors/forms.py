from django import forms
from django.forms import TextInput
from .models import UserHotel, Room, Booking
from bootstrap_datepicker_plus import DatePickerInput

# class Booking(models.Model):
#     customer = models.ForeignKey(UserHotel, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
#     startdate = models.DateField(blank=True, null=True)
#     enddate = models.DateField(blank=True, null=True)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room','startdate','enddate']
        widgets = {
            'startdate': DatePickerInput(), # default date-format %m/%d/%Y will be used
            'enddate': DatePickerInput(format='%d-%m-%Y'), # specify date-frmat
        }
