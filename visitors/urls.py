from django.contrib.auth.models import User
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('accounts/login/', views.login_view, name='login'),
	path('accounts/logout', views.logout_view, name='logout'),
]