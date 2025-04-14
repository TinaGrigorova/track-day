from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

# Class race track where people can book sessions.

class Track(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length_km = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default="No description provided.")
    image = models.ImageField(upload_to='tracks/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    is_rental = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='bookings')
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.track.name} on {self.date}"
    
