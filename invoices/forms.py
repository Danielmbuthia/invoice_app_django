from django import forms
from django.core.exceptions import ValidationError

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Invoice
        fields = (
            'receiver',
            'invoice_number',
            'completion_date',
            'issue_date',
            'payment_date',
        )

    # def clean_invoice_number(self):
    #     number = self.cleaned_data.get('invoice_number')
    #     if len(number) < 10:
    #         raise ValidationError('Invoice Number too short')
