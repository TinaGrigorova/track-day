from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking_index'),
    path('book/', views.book_track, name='book_track'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login_view, name='login'),
    #path('logout/', views.custom_logout_view, name='logout'),
    path('track/<slug:track_slug>/', views.track_detail, name='track_detail'),
    path('tracks/lydden-hill/', views.lydden_hill, name='lydden_hill'),
    path('tracks/brands-hatch/', views.brands_hatch, name='brands_hatch'),
    path('tracks/silverstone/', views.silverstone, name='silverstone'),
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]
