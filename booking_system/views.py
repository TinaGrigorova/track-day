from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def index(request):
    """
    Homepage view.
    """
    return render(request, 'booking_system/index.html')

@login_required
def my_bookings(request):
    """
    Display all bookings for the logged-in user.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_system/my_bookings.html', {'bookings': bookings})

@login_required
def book_track(request):
    """
    Displays and processes the booking form.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your track day has been booked successfully!')
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'booking_system/book_track.html', {'form': form})

@login_required
def booking_success(request):
    """
    Success page after booking.
    """
    return render(request, 'booking_system/booking_success.html')

@login_required
def cancel_booking(request, booking_id):
    """
    Allows the user to cancel their booking.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been cancelled.')
        return redirect('my_bookings')
    return render(request, 'booking_system/cancel_booking.html', {'booking': booking})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! You can now manage your booking.')
            return redirect('my_bookings')
    else:
        form = UserRegisterForm()
    return render(request, 'booking_system/register.html', {'form': form})


def signup(request):
    """
    Allows a user to register an account.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('booking_index')
    else:
        form = UserRegisterForm()
    return render(request, 'booking_system/signup.html', {'form': form})