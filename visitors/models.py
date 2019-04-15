from django.db import models
from django.contrib.auth.models import User

class UserHotel(models.Model):
	phone = models.CharField(max_length=10, blank-True, null=true)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username

class Room(models.Model):
	number = models.CharField(max_length=5)
	price = models.CharField(max_length=50, blank-True, null=true)
	description = models.CharField(max_length=100)
	areadesc = models.CharField(max_length=100)

class Book(models.Model):
	customer: models.ForeignKey(User, on_delete=models.CASCADE)
	room: models.ForeignKey(Room, on_delete=models.CASCADE)
	startdate: models.DateField()
	enddate: models.DateField()
	# ocation, images, description, what’s in the surroundingarea,

# class MovieReview(models.Model):

#     RATING_CHOICES = (
#         (1, 1),
#         (2, 2),
#         (3, 3),
#         (4, 4),
#         (5, 5),
#         (6, 6),
#         (7, 7),
#         (8, 8),
#         (9, 9),
#         (10, 10)
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
#     text = models.TextField(blank=True, null=True)
#     rating = models.IntegerField(choices=RATING_CHOICES, default=5)
#     title = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return (self.text)

