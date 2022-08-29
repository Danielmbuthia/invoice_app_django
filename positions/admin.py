from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
from positions.models import Position


class PositionResources(resources.ModelResource):
    invoice = Field()

    class Meta:
        model = Position
        fields = ('title', 'description', 'amount', 'invoice')

    def dehydrate_invoice(self, obj):
        return obj.invoice.invoice_number


class PositionAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PositionResources


admin.site.register(Position, PositionAdmin)
