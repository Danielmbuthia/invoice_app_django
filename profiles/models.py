from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from profiles.utils import generate_account_number


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=26, blank=True)
    company_name = models.CharField(max_length=220)
    company_info = models.TextField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Profile of user: {self.user.username}'

    def save(self, *args, **kwargs):
        if self.account_number == '':
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

