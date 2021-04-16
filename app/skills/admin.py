from django.contrib import admin
from skills.models import Skill


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    list_per_page = 20

admin.site.register(Skill, SkillsAdmin)