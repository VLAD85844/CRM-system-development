from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('last_name', 'first_name', 'phone')