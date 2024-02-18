from django.contrib import admin
from .models import Contact, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)
