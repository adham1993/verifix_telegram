from django.contrib import admin
from .models import (
    Education,
    LanguageLevel,
    Language,
    Question,
    Answer,
    AboutCompany,
    Contact,
    SuccessCandidate,
    FailedCandidate,
    WrittenQuestion,
    WrittenAnswer
)
from bot.models import (
    UserProfile
)
from apps.company.models import (
    Vacancy,
    Filial,
    Region
)
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
# Register your models here.


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


class QuestionListFilter(admin.SimpleListFilter):
    title = _('Question')
    parameter_name = 'question'

    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            questions = Question.objects.all()
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            questions = Question.objects.filter(user_profile=user_profile)
        return [(question.id, question.title_uz) for question in questions]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(vacancy__id=self.value())
        return queryset


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'company', 'user_profile')
    list_display_links = ('id', 'name_uz', 'name_ru')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'company', 'user_profile')
    list_display_links = ('id', 'name_uz', 'name_ru')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_uz', 'name_ru', 'company', 'user_profile')
    list_display_links = ('id', 'name_uz', 'name_ru')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # inlines = [AnswerInlineAdmin, ]
    list_display = ('id', 'title_uz')
    list_display_links = ('id', 'title_uz')
    list_filter = (VacancyListFilter, )

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'vacancy' and not request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=request.user)
            kwargs["queryset"] = Vacancy.objects.filter(user_profile=user_profile)
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
            super().save_model(request, obj, form, change)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'vacancy', 'question', 'title_uz')
    list_display_links = ('id', 'vacancy', 'question', 'title_uz')
    list_filter = (VacancyListFilter, QuestionListFilter)

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'vacancy')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'question' and not request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=request.user)
            kwargs["queryset"] = Question.objects.filter(user_profile=user_profile)
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
            if obj.question:
                if obj.question.vacancy:
                    obj.vacancy = obj.question.vacancy
            super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company')
    list_display_links = ('id', 'user_profile', 'company'   )

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company', 'title_uz')
    list_display_links = ('id', 'user_profile', 'company', 'title_uz')

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


class SuccessCandidateResource(resources.ModelResource):
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
        model = SuccessCandidate
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


@admin.register(SuccessCandidate)
class SuccessCandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SuccessCandidateResource
    list_display = ('id', 'user_profile', 'company', 'first_name')
    list_display_links = ('id', 'user_profile', 'company', 'first_name')
    list_filter = (FilialListFilter, RegionListFilter, VacancyListFilter)

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


class FailedCandidateResource(resources.ModelResource):
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
        model = FailedCandidate
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


@admin.register(FailedCandidate)
class FailedCandidateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FailedCandidateResource
    list_display = ('id', 'user_profile', 'company', 'first_name')
    list_display_links = ('id', 'user_profile', 'company', 'first_name')
    list_filter = (FilialListFilter, RegionListFilter, VacancyListFilter)

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', 'company', )

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


@admin.register(WrittenQuestion)
class WrittenQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz')
    list_display_links = ('id', 'user_profile', 'title_uz')
    # list_filter = (VacancyListFilter, )

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', )

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'vacancy' and not request.user.is_superuser:
    #         user_profile = UserProfile.objects.get(user=request.user)
    #         kwargs["queryset"] = Vacancy.objects.filter(user_profile=user_profile)
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)

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


@admin.register(WrittenAnswer)
class WrittenAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'title_uz')
    list_display_links = ('id', 'user_profile', 'title_uz')
    # list_filter = (VacancyListFilter, )

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)
        else:
            return ('user_profile', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'write_question' and not request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=request.user)
            kwargs["queryset"] = WrittenQuestion.objects.filter(user_profile=user_profile)
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
            super().save_model(request, obj, form, change)

