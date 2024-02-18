from django.contrib import admin
from .models import (
    Education,
    LanguageLevel,
    Language
)
# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru')
    list_display_links = ('id', 'name_uz', 'name_ru')


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru')
    list_display_links = ('id', 'name_uz', 'name_ru')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru')
    list_display_links = ('id', 'name_uz', 'name_ru')