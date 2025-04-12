from django import forms
from .models import Booking, Track
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Car  

from django import forms
from .models import Booking, Track, Car
from django.utils import timezone

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': timezone.now().date().isoformat()
        }),
        label='Select a date'
    )
    time_slot = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. 09:00 - 10:00',
            'class': 'form-control'
        }),
        label='Time slot'
    )

    class Meta:
        model = Booking
        fields = ['track', 'car', 'date', 'time_slot']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['track'].queryset = Track.objects.all()
        self.fields['car'].queryset = Car.objects.filter(is_rental=True)
        self.fields['track'].widget.attrs.update({'class': 'form-select'})
        self.fields['car'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['time_slot'].widget.attrs.update({'class': 'form-control'})

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
