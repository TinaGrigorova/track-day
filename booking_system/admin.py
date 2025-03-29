from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Track, Car, Booking

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'length_km')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'is_rental', 'owner')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'track', 'car', 'date', 'time_slot')
    list_filter = ('track', 'date')
