from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from invoices.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/main.html"

