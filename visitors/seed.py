from random import randint
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Towers.settings')

import django
django.setup()

from visitors.models import Hotel, Booking, Room
from faker import Faker
from django.contrib.auth.models import User

if __name__ == '__main__':
	print('Starting to populate...')
	Hotel.objects.all().delete()
	Booking.objects.all().delete()
	Room.objects.all().delete()
