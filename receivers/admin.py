from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
from .models import Receiver


# Register your models here.

class ReceiverResource(resources.ModelResource):
    class Meta:
        model = Receiver
        fields = ('name', 'address', 'website')


class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ReceiverResource


admin.site.register(Receiver, ReceiverAdmin)
