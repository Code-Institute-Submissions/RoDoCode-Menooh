from django import forms
from .models import ChefProfile
from blog.models import Post, Cookbook


class ChefProfileForm(forms.ModelForm):
    class Meta:
        model = ChefProfile
        fields = ['bio', 'location', 'birth_date', 'profile_pic', 'facebook_url',
                  'twitter_url', 'instagram_url', 'pinterest_url', 'tiktok_url', 'website_url']


class NewDishForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content',
                  'ingredients', 'status', 'excerpt', 'category', 'prep_time_minutes', 'prep_time_hours', 'cook_time_minutes', 'cook_time_hours']


class NewCookbookForm(forms.ModelForm):
    class Meta:
        model = Cookbook
        fields = ['title', 'cover_image', 'description', 'status', 'excerpt']
