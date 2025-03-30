from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'booking_system/index.html')

def my_bookings(request):
    """
    Display all bookings for the logged-in user.
    """
    bookings = request.user.bookings.all()
    return render(request, 'booking_system/my_bookings.html', {'bookings': bookings})

def book_track(request):
    """
    Displays and processes the booking form.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the logged-in user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking_system/book_track.html', {'form': form})

def booking_success(request):
    """
    Simple success page after booking.
    """
    return render(request, 'booking_system/booking_success.html')