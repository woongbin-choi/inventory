from django.contrib import admin

from .models import Management


class ManagementAdmin(admin.ModelAdmin):
    search_fields = ['product_name']


admin.site.register(Management, ManagementAdmin)