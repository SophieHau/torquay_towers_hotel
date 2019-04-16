from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserHotel, Room, Booking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import BookingForm


def index(request):
    return render(request, 'index.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def booking(request):
	if request.method == 'POST':
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			booking = booking_form.save(commit=False)
			u = request.user
			h = UserHotel.objects.get(user=u)
			booking.customer = h
			booking.save() 
			return redirect('visitor-booking-ok')
	else:
		booking_form = BookingForm()
		return render(request, 'booking.html', {
			'booking_form': booking_form
		})

def bookingok(request):
	return render(request, 'bookingok.html')

def reviews(request):
	return render(request, 'reviews.html')
