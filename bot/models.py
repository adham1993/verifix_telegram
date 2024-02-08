from django.db import models
from django.contrib.auth.models import User
from apps.company.models import (
    Company,
    Filial,
    Region
)
# Create your models here.


class UserProfile(models.Model):
    profile_name = models.CharField(max_length=128)
    bot_username = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_name or self.user.username


class UserBot(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bot_username = models.CharField(max_length=128)
    language = models.CharField(max_length=10, null=True, blank=True)
    chat_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    passport = models.IntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=100, null=True, blank=True)
    inline_type = models.CharField(max_length=100, null=True, blank=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or self.username or self.chat_id

    class Meta:
        verbose_name = "UserBot"
        verbose_name_plural = "Bot Users"


class BotToken(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    token = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or self.token
