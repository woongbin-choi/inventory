from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['product_name']


admin.site.register(Question, QuestionAdmin)
