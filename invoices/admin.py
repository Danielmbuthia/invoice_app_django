from django.contrib import admin

# Register your models here.
from .models import Invoice, Tag

admin.site.register(Invoice)
admin.site.register(Tag)
