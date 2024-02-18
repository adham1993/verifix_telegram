from django.contrib import admin
from .models import (
    Company,
    Region,
    Filial,
    Vacancy,
    Candidate,
    CandidateLanguages
)
from bot.models import UserProfile
# Register your models here


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name', 'address')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'name_uz')
    list_display_links = ('id', 'name_uz')
    # exclude = ('company', 'user_profile')
    list_filter = ('parent', )

    # def get_exclude(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return super().get_exclude(request, obj)
    #     else:
    #         return ('user_profile', )

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return queryset
    #     else:
    #         user_profile = UserProfile.objects.get(user=request.user)
    #         if user_profile:
    #             return queryset.filter(user_profile=user_profile)
    #         else:
    #             pass

    # def save_model(self, request, obj, form, change):
    #     if request.user.is_superuser:
    #         super().save_model(request, obj, form, change)
    #     else:
    #         user_profile = UserProfile.objects.get(user=request.user)
    #         obj.user_profile = user_profile
    #         # obj.company = user_profile.company
    #         super().save_model(request, obj, form, change)


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'region', 'company', 'name_uz')
    list_display_links = ('id', 'user_profile', 'region', 'company', 'name_uz')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('company', 'user_profile')

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'region' and not request.user.is_superuser:
    #         user_profile = UserProfile.objects.get(user=request.user)
    #         kwargs["queryset"] = Region.objects.filter(user_profile=user_profile)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
            obj.company = user_profile.company
            super().save_model(request, obj, form, change)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company', 'region', 'filial', 'name_uz')
    list_display_links = ('id', 'user_profile', 'company', 'region', 'company', 'name_uz')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('company', 'user_profile', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'filial' and not request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=request.user)
            kwargs["queryset"] = Filial.objects.filter(user_profile=user_profile)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
            obj.company = user_profile.company
            super().save_model(request, obj, form, change)


class CandidateLanguageTabularInlineAdmin(admin.TabularInline):
    model = CandidateLanguages
    list_display = ('id', 'candidate', 'language')
    list_display_links = ('id', 'candidate', 'language')


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'filial', 'vacancy', 'first_name', 'last_name')
    list_display_links = ('id', 'user_profile', 'filial', 'vacancy', 'first_name', 'last_name')
    inlines = [CandidateLanguageTabularInlineAdmin, ]

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'region' and not request.user.is_superuser:
    #         user_profile = UserProfile.objects.get(user=request.user)
    #         kwargs["queryset"] = Region.objects.filter(user_profile=user_profile)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

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


@admin.register(CandidateLanguages)
class CandidateLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'language')
    list_display_links = ('id', 'candidate', 'language')
