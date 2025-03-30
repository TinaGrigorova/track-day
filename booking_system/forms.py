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