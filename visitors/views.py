from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='/accounts/login/')
def index(request, user_id):
    return render(request, 'index.html')

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index', user_id=user.id)

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

