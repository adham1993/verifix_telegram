from django.contrib import admin
from .models import StartMessage
# Register your models here.


@admin.register(StartMessage)
class StartMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'title_ru')
