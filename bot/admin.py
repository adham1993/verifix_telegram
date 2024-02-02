from django.contrib import admin
from .models import UserBot
# Register your models here.


@admin.register(UserBot)
class UserBotAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'chat_id', 'full_name', )
    list_display_links = ('id', 'username', 'chat_id', 'full_name', )
    search_fields = ('username', 'full_name', 'chat_id')
