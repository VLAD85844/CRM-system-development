from django import forms
from .models import Lead
from products.models import Product

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'status',
            'product'
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
        }