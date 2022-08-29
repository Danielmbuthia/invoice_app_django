from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.
from import_export.fields import Field

from .models import Invoice, Tag


class TagResources(resources.ModelResource):
    class Meta:
        model = Tag
        fields = 'name'


class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResources


class InvoiceResources(resources.ModelResource):
    receiver = Field()
    profile = Field()
    closed = Field()
    positions = Field()
    total_amount = Field()

    class Meta:
        model = Invoice
        fields = ('receiver', 'profile', 'invoice_number', 'completion_date', 'issue_date', 'payment_date', 'closed',
                  'positions', 'total_amount')

    def dehydrate_receiver(self, obj):
        return obj.receiver.name

    def dehydrate_profile(self, obj):
        return obj.profile.user.username

    def dehydrate_closed(self, obj):
        if obj.closed == 0:
            return False
        return True

    def dehydrate_positions(self, obj):
        positions_list = [position.title for position in obj.positions]
        return ",".join(positions_list)

    def dehydrate_total_amount(self,obj):
        return obj.total_amount


class InvoiceAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = InvoiceResources


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Tag, TagAdmin)
