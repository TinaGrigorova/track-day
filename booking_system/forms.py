from django import forms
from .models import Booking, Track, Car, RIDE_OPTIONS
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone


TIME_CHOICES = [
    ('10:00 AM', '10:00 AM'),
    ('11:00 AM', '11:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('1:00 PM', '1:00 PM'),
    ('2:00 PM', '2:00 PM'),
    ('3:00 PM', '3:00 PM'),
    ('4:00 PM', '4:00 PM'),
    ('5:00 PM', '5:00 PM'),
    ('6:00 PM', '6:00 PM'),
]


class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': timezone.now().date().isoformat(),
            'class': 'form-control'
        }),
        label='Select a date'
    )

    time_slot = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Select Time Slot'
    )

    ride_option = forms.ChoiceField(
        choices=RIDE_OPTIONS,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Ride Option'
    )

    class Meta:
        model = Booking
        fields = ['track', 'car', 'date', 'time_slot', 'ride_option']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['track'].queryset = Track.objects.all()
        self.fields['car'].queryset = Car.objects.filter(is_rental=True)
        self.fields['track'].widget.attrs.update({'class': 'form-select'})
        self.fields['car'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['time_slot'].widget.attrs.update({'class': 'form-select'})

    def clean(self):
        cleaned_data = super().clean()
        track = cleaned_data.get('track')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        if track and date and time_slot:
            current_booking = self.instance if self.instance.pk else None
            existing = Booking.objects.filter(
                track=track,
                date=date,
                time_slot=time_slot
            ).exclude(id=current_booking.id if current_booking else None)

            if existing.exists():
                raise forms.ValidationError(
                    f"{track.name} is already booked for {date} at {time_slot}"
                )

        return cleaned_data


class UserRegisterForm(UserCreationForm):
    """User registration form with email field."""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
