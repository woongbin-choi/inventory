from django.contrib import admin
from .models import Takeout

class TakeoutAdmin(admin.ModelAdmin):
    search_fields = ['material_name']


admin.site.register(Takeout, TakeoutAdmin)
