from django.db import models
# Create your models here.


class Education(models.Model):
    name_uz = models.CharField(max_length=64)
    name_ru = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uz or self.name_ru


class LanguageLevel(models.Model):
    name_uz = models.CharField(max_length=64)
    name_ru = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)

    def __str__(self):
        return self.name_uz or self.name_ru


class Language(models.Model):
    name_uz = models.CharField(max_length=64)
    name_ru = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64)

    def __str__(self):
        return self.name_uz or self.name_ru


class Question(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    vacancy = models.ForeignKey('company.Vacancy', on_delete=models.CASCADE)
    title_uz = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz or self.title_ru


class Answer(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    vacancy = models.ForeignKey('company.Vacancy', on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title_uz = models.TextField()
    title_ru = models.TextField(null=True, blank=True)
    title_en = models.TextField(null=True, blank=True)
    current_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz or self.title_ru


class Contact(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True)
    instagram = models.URLField(max_length=300, null=True, blank=True)
    facebook = models.URLField(max_length=300, null=True, blank=True)
    telegram = models.URLField(max_length=300, null=True, blank=True)
    linkedin = models.URLField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=300, null=True, blank=True)


class AboutCompany(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    link = models.URLField(max_length=255, null=True, blank=True)
    video = models.FileField(upload_to='static/about_company/videos', null=True, blank=True)
    image = models.ImageField(upload_to='static/about_company/images', null=True, blank=True)

    def __str__(self):
        return self.title_uz or self.title_ru


class SuccessCandidate(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE,
                                     related_name='user_profile_success_candidate')
    bot_user = models.ForeignKey('bot.UserBot', on_delete=models.CASCADE, related_name='success_candidate_user')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey('company.Region', on_delete=models.CASCADE, null=True, blank=True)
    filial = models.ForeignKey('company.Filial', on_delete=models.CASCADE, null=True, blank=True)
    vacancy = models.ForeignKey('company.Vacancy', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=128, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='static/success_candidate/images', null=True, blank=True)
    main_phone = models.CharField(max_length=128, null=True, blank=True)
    extra_phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    legal_address = models.CharField(max_length=256, null=True, blank=True)
    wage_expectation = models.CharField(max_length=128,null=True, blank=True, default=0)
    node = models.CharField(max_length=256, null=True, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    language_data = models.CharField(max_length=256, null=True, blank=True)
    education_data = models.CharField(max_length=256, null=True, blank=True)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name or self.last_name or self.middle_name


class FailedCandidate(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE,
                                     related_name='user_profile_failed_candidate')
    bot_user = models.ForeignKey('bot.UserBot', on_delete=models.CASCADE, related_name='failed_candidate_user')
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey('company.Region', on_delete=models.CASCADE, null=True, blank=True)
    filial = models.ForeignKey('company.Filial', on_delete=models.CASCADE, null=True, blank=True)
    vacancy = models.ForeignKey('company.Vacancy', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=128, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='static/failed_candidate/images', null=True, blank=True)
    main_phone = models.CharField(max_length=128, null=True, blank=True)
    extra_phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    legal_address = models.CharField(max_length=256, null=True, blank=True)
    wage_expectation = models.CharField(max_length=128,null=True, blank=True, default=0)
    node = models.CharField(max_length=256, null=True, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    language_data = models.CharField(max_length=256, null=True, blank=True)
    education_data = models.CharField(max_length=256, null=True, blank=True)
    add_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name or self.last_name or self.middle_name
