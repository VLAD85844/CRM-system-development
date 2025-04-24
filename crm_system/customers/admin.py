from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('lead', 'status', 'created_at')
    list_filter = ('status',)
    raw_id_fields = ('lead',)