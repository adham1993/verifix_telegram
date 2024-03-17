from django.db import models
from apps.main.models import (
    Language,
    LanguageLevel,
    Education
)
# Create your models here.


class Company(models.Model):
    # user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_company')
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or self.address


class Region(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='user_profile_region')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    image = models.ImageField(upload_to='static/regions/images')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz or self.name_ru or self.name_en


class Filial(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_filial')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    image = models.ImageField(upload_to='static/filials/images')
    opened_date = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name_uz


class Vacancy(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_vacancy')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    filial = models.ManyToManyField(Filial, related_name='vacancy_filial', blank=True)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128, null=True, blank=True)
    name_en = models.CharField(max_length=128, null=True, blank=True)
    description_uz = models.TextField()
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    job_name_uz = models.CharField(max_length=128)
    job_name_ru = models.CharField(max_length=128, null=True, blank=True)
    job_name_en = models.CharField(max_length=128, null=True, blank=True)
    schedule_uz = models.TextField(verbose_name='Work time uzbek')
    schedule_ru = models.TextField(null=True, blank=True, verbose_name='Work time russian')
    schedule_en = models.TextField(null=True, blank=True, verbose_name='Work time english')
    wage_limit_uz = models.TextField(verbose_name='salary work uzbek')
    wage_limit_ru = models.TextField(verbose_name='salary work russian', null=True, blank=True)
    wage_limit_en = models.TextField(verbose_name='salary work english', null=True, blank=True)
    lang_uz = models.CharField(max_length=64, verbose_name='Tillar')
    lang_ru = models.CharField(max_length=64, verbose_name='Languages', null=True, blank=True)
    lang_en = models.CharField(max_length=64, verbose_name='Язикы', null=True, blank=True)
    order = models.IntegerField(default=0)
    main_office = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz or self.name_en or self.name_ru


class Candidate(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_candidate')
    bot_user = models.ForeignKey('bot.UserBot', on_delete=models.CASCADE, related_name='candidate_user')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=128, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='static/candidate/images', null=True, blank=True)
    main_phone = models.CharField(max_length=128, null=True, blank=True)
    extra_phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    legal_address = models.CharField(max_length=256, null=True, blank=True)
    wage_expectation = models.CharField(max_length=128,null=True, blank=True, default=0)
    note = models.CharField(max_length=256, null=True, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    language_data = models.CharField(max_length=256, null=True, blank=True)
    education_data = models.CharField(max_length=256, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name or self.last_name or self.middle_name


class CandidateLanguages(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='user_profile_candidate_language')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidate_languages')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='candidate_language_vacancy')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    language_level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE, null=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.candidate.first_name or self.candidate.last_name or self.candidate.middle_name


class ResumeFilter(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE,
                                     related_name='user_profile_resume_filter')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.BooleanField(default=False)
    last_name = models.BooleanField(default=False)
    middle_name = models.BooleanField(default=False)
    gender = models.BooleanField(default=False)
    birthday = models.BooleanField(default=False)
    image = models.BooleanField(default=False)
    main_phone = models.BooleanField(default=False)
    extra_phone = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    address = models.BooleanField(default=False)
    legal_address = models.BooleanField(default=False)
    wage_expectation = models.BooleanField(default=False)
    note = models.BooleanField(default=False)
    language = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name or None





