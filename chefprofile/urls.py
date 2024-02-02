from . import views
from django.urls import path

urlpatterns = [
    path('edit_chefprofile/', edit_chefprofile, name='edit_chefprofile'),
    path('view_chefprofile/', view_chefprofile, name='view_chefprofile'),
]
