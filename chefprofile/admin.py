from django.contrib import admin
from .models import ChefProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ChefProfile)
class ChefProfileAdmin(SummernoteModelAdmin):

    search_fields = ['user', 'bio', 'location', 'birth_date',]
    list_filter = ('created_on')
    prepopulated_fields = {'user': ('user',)}
    summernote_fields = ('bio',)


# Register your models here.
admin.site.register(ChefProfile)
