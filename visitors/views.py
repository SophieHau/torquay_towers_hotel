from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from .forms import BookingForm, InfoRequestForm
=======
>>>>>>> master
from django.utils import timezone
from datetime import *
from .models import Booking, Room, UserHotel
from .forms import BookingForm

@login_required(login_url='accounts/login/')
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

def booking(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        customer = UserHotel.objects.get(user_id=user.id)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            rooms = Room.get_free_rooms(booking.startdate, booking.enddate)
            if len(rooms) > 0:
                booking.room = rooms[0]
                booking.customer = customer
                booking.save()
                return redirect('booking_confirmed')
            else:
                return redirect('index')
    form = BookingForm()
    return render(request, 'booking.html', {
            'form': form,
        })


def booking_confirmed(request):
    return render(request, 'bookingok.html')

def reviews(request):
    return render(request, 'reviews.html')

