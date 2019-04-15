from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Home Working</h1>')


def booking(request):
	return HttpResponse('<h1>Booking Working</h1>')


def reviews(request):
	return HttpResponse('<h1>Reviews Working</h1>')
