"""
URL configuration for menooh project.
"""
from django.contrib import admin
from django.urls import path, include
from contact import views as contact_views

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls"), name='contact'),
    path('chefprofile/', include("chefprofile.urls"),
         name='chefprofile-urls'),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),

]
