from . import views
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.view_chefprofile, name = 'view_chefprofile'),
    path('edit/', views.edit_chefprofile, name = 'edit_chefprofile'),
    path('new_dish/', views.new_dish, name = 'new_dish'),
    path('new_cookbook/', views.new_cookbook, name = 'new_cookbook'),
]
