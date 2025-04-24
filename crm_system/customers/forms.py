from django import forms
from .models import Customer
from leads.models import Lead

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['lead', 'assigned_to', 'status']
        widgets = {
            'lead': forms.Select(attrs={'class': 'form-select'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }