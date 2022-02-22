from django.contrib import admin

from .models import Question


class QuestionSearch(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionSearch)
