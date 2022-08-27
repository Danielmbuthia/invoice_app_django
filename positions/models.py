from django.db import models

# Create your models here.
from invoices.models import Invoice


class Position(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="Optional")
    amount = models.FloatField(help_text="amount in dollars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice: {self.invoice.invoice_number} position title: {self.title}"





