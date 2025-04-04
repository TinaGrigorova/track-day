from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking_index'),  # booking/
    path('book/', views.book_track, name='book_track'),  # booking/book/
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('signup/', views.signup, name='signup'),

]