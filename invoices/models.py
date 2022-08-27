from django.db import models
from profiles.models import Profile
from receivers.models import Receiver


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


# Create your models here.
class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=200)
    completion_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.invoice_number

    def get_tags(self):
        return self.tags.all()

    def get_positions(self):
        return self.position_set.all()  # relationships

    def get_total_amount(self):
        total = 0
        qs = self.get_positions()
        for pos in qs:
            total += pos.amount
        return total
