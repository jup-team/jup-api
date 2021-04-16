from django.contrib import admin
from questions.models import Question


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'statement', 'skill', 'level')
    list_display_links = ('id', 'statement')
    search_fields = ['skill', 'level', 'statement']
    list_per_page = 10

admin.site.register(Question, QuestionsAdmin)