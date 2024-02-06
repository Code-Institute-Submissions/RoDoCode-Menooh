from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_chefprofile, name='view_chefprofile'),
    path('edit/', views.edit_chefprofile, name='edit_chefprofile'),
]
