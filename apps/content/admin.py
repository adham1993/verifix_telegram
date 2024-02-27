from django.contrib import admin
from bot.models import UserProfile
from .models import (
    StartMessage,
    FilialMessage,
    RegionMessage,
    VacancyMessage,
    MainOfficeVacancyMessage,
    ContactMessage,
    WriteQuestionMessage
)
# Register your models here.


@admin.register(StartMessage)
class StartMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     print(form)
    #     if request.user.is_superuser:
    #         print('aaa')
    #         form.base_fields['user_profile'].widget.can_view_related = False
    #         form.base_fields['user_profile'].widget.can_add_related = False
    #         form.base_fields['user_profile'].widget.can_change_related = False
    #         form.base_fields['user_profile'].widget.can_delete_related = False
    #     else:
    #         print('fffff')
    #         print(form.base_fields)
    #         form.base_fields['user_profile'].widget.can_view_related = False
    #         form.base_fields['user_profile'].widget.can_add_related = False
    #         form.base_fields['user_profile'].widget.can_change_related = False
    #         form.base_fields['user_profile'].widget.can_delete_related = False
    #     return form


@admin.register(FilialMessage)
class FilialMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)


@admin.register(RegionMessage)
class RegionMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)


@admin.register(VacancyMessage)
class VacancyMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)


@admin.register(MainOfficeVacancyMessage)
class MainOfficeVacancyMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)


@admin.register(WriteQuestionMessage)
class WriteQuestionMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz', 'title_ru')
    exclude = ('user_profile',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            if user_profile:
                return queryset.filter(user_profile=user_profile)
            else:
                pass

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            obj.user_profile = user_profile
            super().save_model(request, obj, form, change)
