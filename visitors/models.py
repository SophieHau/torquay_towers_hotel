from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

class UserHotel(models.Model):
	phone = models.CharField(max_length=10, blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Room(models.Model):
	number = models.CharField(max_length=5)
	price = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.number

	@staticmethod
	def get_free_rooms(start_date, end_date):
		'''get all rooms without bookings whose:
				start date is before C,
				and end date is after C
				OR whose start date is on or after C
				and start date is before D. '''
		free_rooms = Room.objects.exclude(
			Q(booking__start_date__lt=start_date,
				booking__end_date__gt=start_date) |
			Q(booking__start_date__gte=start_date,
				booking__start_date__lt=end_date))
		return free_rooms

class Booking(models.Model):
	customer = models.ForeignKey(UserHotel, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
	startdate = models.DateField(blank=True, null=True)
	enddate = models.DateField(blank=True, null=True)
	def __str__(self):
		return str(self.room)
