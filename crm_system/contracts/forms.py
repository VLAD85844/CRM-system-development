from django import forms
from .models import Contract
from django.core.exceptions import ValidationError
from django.utils import timezone

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'name', 'customer', 'product', 'document',
            'signing_date', 'start_date', 'end_date', 'amount'
        ]
        widgets = {
            'signing_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        signing_date = cleaned_data.get("signing_date")

        if start_date and end_date and start_date > end_date:
            raise ValidationError("Дата начала не может быть позже даты окончания")

        if signing_date and signing_date > timezone.now().date():
            raise ValidationError("Дата подписания не может быть в будущем")

        return cleaned_data