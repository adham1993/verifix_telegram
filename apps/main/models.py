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

