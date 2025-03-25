from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Class race track where people can book sessions.

class Track(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    length_km = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name