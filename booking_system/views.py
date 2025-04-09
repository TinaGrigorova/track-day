from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import BookingForm, UserRegisterForm
from .models import Booking

# Homepage
def index(request):
    return render(request, 'booking_system/index.html')

# User Signup
def signup(request):
    """
    Allows a user to register an account.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created successfully! Welcome, {user.username}!")
            return redirect('index') 
    else:
        form = UserRegisterForm()
    return render(request, 'booking_system/signup.html', {'form': form})

# Custom Login
def custom_login_view(request):
    """
    Custom login view with welcome message.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('my_bookings')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'booking_system/login.html')

# Booking a Track
@login_required
def book_track(request):
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

# Viewing My Bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_system/my_bookings.html', {'bookings': bookings})

# Booking Success Page
@login_required
def booking_success(request):
    return render(request, 'booking_system/booking_success.html')

# Cancel Booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been cancelled.')
        return redirect('my_bookings')
    return render(request, 'booking_system/cancel_booking.html', {'booking': booking})

# Track Information & booking 

def track_detail(request, track_slug):
    return render(request, f'booking_system/tracks/{track_slug}.html')


def lydden_hill(request):
    return render(request, 'booking_system/tracks/lydden_hill.html')

def brands_hatch(request):
    return render(request, 'booking_system/tracks/brands_hatch.html')

def silverstone(request):
    return render(request, 'booking_system/tracks/silverstone.html')