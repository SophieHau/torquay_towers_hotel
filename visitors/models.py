from django.db import models
from django.contrib.auth.models import User

class UserHotel(models.Model):
	phone = models.CharField(max_length=10, blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Room(models.Model):
	number = models.CharField(max_length=5)
	price = models.CharField(max_length=50)

class Booking(models.Model):
	customer = models.ForeignKey(UserHotel, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	startdate = models.DateField()
	enddate = models.DateField()
