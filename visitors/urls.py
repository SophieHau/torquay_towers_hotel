from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('booking/', views.booking, name='visitor-booking'),
    path('bookingok/', views.bookingok, name='visitor-booking-ok'),
    path('reviews/', views.reviews, name='visitor-reviews'),
	path('accounts/login/', views.login_view, name='login'),
	path('accounts/logout', views.logout_view, name='logout'),
	path('inforequest/', views.inforequest, name='inforequest'),
]