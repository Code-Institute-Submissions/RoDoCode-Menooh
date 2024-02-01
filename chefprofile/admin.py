from django.contrib import admin
from .models import ChefProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ChefProfile)
class ChefProfileAdmin(SummernoteModelAdmin):

    search_fields = ['user', 'bio', 'location', 'birth_date',]
    summernote_fields = ('bio',)
