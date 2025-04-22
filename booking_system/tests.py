from django.test import TestCase
from django.urls import path
from . import views

# Create your tests here.

urlpatterns = [
    path('book/', views.book_track, name='book_track'),
    path('success/', views.booking_success, name='booking_success'),
]
