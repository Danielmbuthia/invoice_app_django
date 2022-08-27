from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.
from .models import Invoice, Tag


class TagResources(resources.ModelResource):
    class Meta:
        model = Tag
        fields = 'name'


class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResources


admin.site.register(Invoice)
admin.site.register(Tag, TagAdmin)
