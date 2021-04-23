from django.contrib import admin
from .models import Position
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 10


admin.site.register(Position, PositionAdmin)
