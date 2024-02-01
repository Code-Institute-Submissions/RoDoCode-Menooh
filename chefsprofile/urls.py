from django.urls import path
from .views import edit_profile, view_profile

urlpatterns = [
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', view_profile, name='profile'),
]
