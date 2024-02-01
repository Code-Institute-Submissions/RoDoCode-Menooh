from django.urls import path
from .views import edit_profile, view_profile

urlpatterns = [
    path('edit_chefprofile/', edit_chefprofile, name='edit_chefprofile'),
    path('view_chefprofile/', view_chefprofile, name='view_chefprofile'),
]
