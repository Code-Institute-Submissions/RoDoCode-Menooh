from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class ChefProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="chefprofile")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = CloudinaryField('image', default='placeholder')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ChefProfile.objects.create(user=instance)
