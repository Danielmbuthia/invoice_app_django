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

    @property  # treat tags as a field
    def tags(self):
        return self.tags.all()

    @property
    def positions(self):
        return self.position_set.all()  # relationships

    @property
    def total_amount(self):
        total = 0
        qs = self.positions
        for pos in qs:
            total += pos.amount
        return total
