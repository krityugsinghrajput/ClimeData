from django.contrib import admin

from django.contrib import admin
from .models import LocationRequest

@admin.register(LocationRequest)
class LocationRequestAdmin(admin.ModelAdmin):
    list_display = ('location', 'country', 'submitted_at')
    search_fields = ('location', 'country', 'user_email')
