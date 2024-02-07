from django import forms
from .models import ChefProfile


class ChefProfileForm(forms.ModelForm):
    class Meta:
        model = ChefProfile
        fields = ['bio', 'location', 'birth_date', 'profile_pic', 'facebook_url',
                  'twitter_url', 'instagram_url', 'pinterest_url', 'tiktok_url', 'website_url']
