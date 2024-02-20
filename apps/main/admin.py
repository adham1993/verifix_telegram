from django.contrib import admin
from .models import (
    Education,
    LanguageLevel,
    Language,
    Question,
    Answer,
    AboutCompany,
    Contact
)
from bot.models import (
    UserProfile
)
from apps.company.models import (
    Vacancy
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


# class AnswerInlineAdmin(admin.TabularInline):
#     model = Answer
#
#     list_display = ('id', 'vacancy', 'question', 'title_uz')
#     list_display_links = ('id', 'vacancy', 'question', 'title_uz')
#
#     def get_exclude(self, request, obj=None):
#         if request.user.is_superuser:
#             return super().get_exclude(request, obj)
#         else:
#             return ('user_profile', 'vacancy', )
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'question' and not request.user.is_superuser:
#             user_profile = UserProfile.objects.get(user=request.user)
#             kwargs["queryset"] = Question.objects.filter(user_profile=user_profile)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if request.user.is_superuser:
#             return queryset
#         else:
#             user_profile = UserProfile.objects.get(user=request.user)
#             if user_profile:
#                 return queryset.filter(user_profile=user_profile)
#             else:
#                 pass
#
#     def save_model(self, request, obj, form, change):
#         if request.user.is_superuser:
#             super().save_model(request, obj, form, change)
#             print('ssssssssssss')
#         else:
#             user_profile = UserProfile.objects.get(user=request.user)
#             obj.user_profile = user_profile
#             obj.save()
#             print('aaaaaaaaaa')
#             super().save_model(request, obj, form, change)
#

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # inlines = [AnswerInlineAdmin, ]
    list_display = ('id', 'vacancy', 'title_uz')
    list_display_links = ('id', 'vacancy', 'title_uz')
    list_filter = ('vacancy', )

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
    list_filter = ('vacancy', 'question')

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
