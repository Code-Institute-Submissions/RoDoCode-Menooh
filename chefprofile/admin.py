from django.contrib import admin
from .models import ChefProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ChefProfile)
class ProfileAdmin(SummernoteModelAdmin):

    search_fields = ['user', 'bio', 'location', 'birth_date',]
    prepopulated_fields = {'user': ('user',)}
    summernote_fields = ('bio', 'location,', 'birth_date',)


# Register your models here.
admin.site.register(ChefProfile)
