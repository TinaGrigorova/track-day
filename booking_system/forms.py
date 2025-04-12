from django import forms
from .models import Booking, Track
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Car  

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['track', 'car', 'date', 'time_slot']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(is_rental=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['track'].queryset = Track.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        track = cleaned_data.get('track')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        if track and date and time_slot:
            existing = Booking.objects.filter(track=track, date=date, time_slot=time_slot)
            if existing.exists():
                raise forms.ValidationError(
                    f"{track.name} is already booked for {date} at {time_slot}."
                )
        return cleaned_data


class UserRegisterForm(UserCreationForm):
    """
    User registration form with email field.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
