from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('booking/<int:user_id>/', views.booking, name='booking'),
    path('bookingok/', views.booking_confirmed, name='booking_confirmed'),
    path('reviews/', views.reviews, name='reviews'),
	path('accounts/login/', views.login_view, name='login'),
	path('accounts/logout', views.logout_view, name='logout'),
]