from . import views
from django.urls import path

urlpatterns = [
    path('', views.edit_chefprofile, name='edit_chefprofile'),
    path('', views.view_chefprofile, name='view_chefprofile'),
]
