from django import forms
from .models import ChefProfile


class ChefProfileForm(forms.ModelForm):
    class Meta:
        model = ChefProfile
        fields = ['bio', 'location', 'birth_date', 'profile_pic']
