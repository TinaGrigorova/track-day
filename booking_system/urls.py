from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking_index'),  # booking/
    path('book/', views.book_track, name='book_track'),  # booking/book/
    path('success/', views.booking_success, name='booking_success'),
]