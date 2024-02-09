from . import views
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.view_chefprofile.as_view(), name='view_chefprofile'),
    path('edit/', views.edit_chefprofile, name='edit_chefprofile'),
]
