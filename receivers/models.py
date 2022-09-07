from django.db import models


# Create your models here.
class Receiver(models.Model):
    """
    Company that receives the invoice
    """
    name = models.CharField(max_length=200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = models.ImageField(default='images/no_photo.png')

    def __str__(self):
        return self.name
