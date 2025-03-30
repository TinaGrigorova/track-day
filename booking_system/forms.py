from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    """
    Allows user to select track, car, date, and time slot.
    """
    class Meta:
        model = Booking
        fields = ['track', 'car', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.TextInput(attrs={'placeholder': 'e.g. 09:00 - 10:00'})
        }

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
