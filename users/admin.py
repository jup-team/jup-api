from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_filter = ('id', 'username')
    search_fields = ('id', 'username')
