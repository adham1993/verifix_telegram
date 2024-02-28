from django.contrib import admin
from .models import (
    Company,
    Region,
    Filial,
    Vacancy,
    Candidate,
    CandidateLanguages,
    ResumeFilter,
)
from bot.models import (
    UserBot
)
from bot.models import UserProfile
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

# Register your models here


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name', 'address')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'company', 'user_profile', 'name_uz')
    list_display_links = ('id', 'name_uz')
    # exclude = ('company', 'user_profile')
    # list_filter = ('parent', )

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('company', 'user_profile')

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


class RegionListFilter(admin.SimpleListFilter):
    title = _('Region')
    parameter_name = 'region'

    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            regions = Region.objects.all()
        else:
            regions = Region.objects.all()
        return [(region.id, region.name_uz) for region in regions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(region__id=self.value())
        return queryset


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'region', 'company', 'name_uz')
    list_display_links = ('id', 'user_profile', 'region', 'company', 'name_uz')
    list_filter = (RegionListFilter, )

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


class FilialListFilter(admin.SimpleListFilter):
    title = _('Filial')
    parameter_name = 'filial'

    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            filials = Filial.objects.all()
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            filials = Filial.objects.filter(user_profile=user_profile)
        return [(filial.id, filial.name_uz) for filial in filials]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(filial__id=self.value())
        return queryset


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company', 'name_uz')
    list_display_links = ('id', 'user_profile', 'company', 'name_uz')
    list_filter = (FilialListFilter, 'main_office')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('company', 'user_profile', 'region', )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'filial' and not request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=request.user)
            kwargs["queryset"] = Filial.objects.filter(user_profile=user_profile)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

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
    exclude = ('vacancy', )


class VacancyListFilter(admin.SimpleListFilter):
    title = _('Vacancy')
    parameter_name = 'vacancy'

    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            vacancies = Vacancy.objects.all()
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            vacancies = Vacancy.objects.filter(user_profile=user_profile)
        return [(vacancy.id, vacancy.name_uz) for vacancy in vacancies]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(vacancy__id=self.value())
        return queryset


class CandidateResource(resources.ModelResource):
    company__name = Field(attribute='company__name', column_name='Company')
    region__name_uz = Field(attribute='region__name_uz', column_name='Region')
    filial__name_uz = Field(attribute='filial__name_uz', column_name='Filial')
    vacancy__name_uz = Field(attribute='vacancy__name_uz', column_name='Vacancy')
    first_name = Field(attribute='first_name', column_name='First Name')
    last_name = Field(attribute='last_name', column_name='Last Name')
    middle_name = Field(attribute='middle_name', column_name='Middle Name')
    gender = Field(attribute='gender', column_name='Gender')
    birthday = Field(attribute='birthday', column_name='Birthday')
    main_phone = Field(attribute='main_phone', column_name='Main Phone')
    extra_phone = Field(attribute='extra_phone', column_name='Extra Phone')
    email = Field(attribute='email', column_name='Email')
    address = Field(attribute='address', column_name='Address')
    legal_address = Field(attribute='legal_address', column_name='Legal Address')
    wage_expectation = Field(attribute='wage_expectation', column_name='Wage Expectation')
    node = Field(attribute='node', column_name='Node')
    language_data = Field(attribute='language_data', column_name='Language Data')
    education_data = Field(attribute='education_data', column_name='Education Data')

    class Meta:
        model = Candidate
        fields = (
            'company__name',
            'region__name_uz',
            'filial__name_uz',
            'vacancy__name_uz',
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'birthday',
            'main_phone',
            'extra_phone',
            'email',
            'address',
            'legal_address',
            'wage_expectation',
            'node',
            'language_data',
            'education_data',
            'add_date'
        )


@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CandidateResource
    list_display = ('id', 'user_profile', 'filial', 'vacancy', 'first_name', 'last_name')
    list_display_links = ('id', 'user_profile', 'filial', 'vacancy', 'first_name', 'last_name')
    list_filter = (FilialListFilter, VacancyListFilter)
    inlines = [CandidateLanguageTabularInlineAdmin, ]

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', )

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

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company')

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


@admin.register(ResumeFilter)
class ResumeFilterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company')
    list_display_links = ('id', 'user_profile', 'company')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('company', 'user_profile', 'bot_user')

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

            user_bot_filters = UserBot.objects.filter(user_profile=user_profile, company=user_profile.company)
            for user_bot_filter in user_bot_filters:
                if user_bot_filter:
                    user_bot_filter.resume_filter = obj
                    user_bot_filter.save()
                    obj.bot_user = user_bot_filter
                    obj.save()
                else:
                    pass
