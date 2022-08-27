from django.contrib import admin
from .models import Profile
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin


# Register your models here.


class ProfileResources(resources.ModelResource):
    user = Field()

    class Meta:
        model = Profile
        fields = ('user', 'account_number', 'company_name', 'company_info')

    def dehydrate_user(self, obj):
        return obj.user.username


class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProfileResources


admin.site.register(Profile, ProfileAdmin)
