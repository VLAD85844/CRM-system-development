from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'product', 'amount')
    list_filter = ('product',)
    raw_id_fields = ('customer', 'product')