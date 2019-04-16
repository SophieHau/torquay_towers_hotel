from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

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

def booking(request):
	return render(request, 'booking.html')

def reviews(request):
	return render(request, 'reviews.html')

# def show_vacancies(request):
#     if request.method == 'POST':
#         start_date = request.POST['start_date']
#         end_date = request.POST['end_date']
#         rooms = Room.objects.all()
#         for room in rooms:

#     Can I book a stay?
# given: X people,
#        C start date,
#        D end date.
# let A = today
# if C is before A - return No
# we need to find all rooms which are NOT free between C and D:
# for each day between C and D (inclusive?)
# get all bookings which:
#     start date is before C, 
#         and end date is after C
#     OR start date is on or after C
#         and start date is before D
