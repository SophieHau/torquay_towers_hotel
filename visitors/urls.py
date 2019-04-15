from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='visitor-home'),
    path('booking/', views.booking, name='visitor-booking'),
    path('reviews/', views.reviews, name='visitor-reviews'),
]