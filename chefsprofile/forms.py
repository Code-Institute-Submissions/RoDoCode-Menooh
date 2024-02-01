from django import forms
from .models import ChefsProfile


class ChefProfileForm(forms.ModelForm):
    class Meta:
        model = ChefsProfile
        fields = ['bio', 'location', 'birth_date', 'profile_pic']
