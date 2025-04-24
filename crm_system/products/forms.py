from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost']
        labels = {
            'cost': 'Стоимость (руб)'
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }