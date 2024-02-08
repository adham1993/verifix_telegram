from django.db import models
# from bot.models import UserProfile
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
    # user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_region')
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128, null=True, blank=True)
    name_en = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_uz or self.name_ru or self.name_en


class Filial(models.Model):
    user_profile = models.ForeignKey('bot.UserProfile', on_delete=models.CASCADE, related_name='user_profile_filial')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128, null=True, blank=True)
    name_en = models.CharField(max_length=128, null=True, blank=True)
    opened_date = models.DateTimeField(auto_now=True)
    closed_date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name_uz or self.name_ru or self.name_en


