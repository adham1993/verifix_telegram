from django.db import models
from bot.models import UserProfile
# Create your models here.


class StartMessage(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    image = models.ImageField(upload_to='static/start_message/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Bosh sahifa matni'
        verbose_name_plural = 'Home text'

    def __str__(self):
        return self.title_uz or self.title_ru


class RegionMessage(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    image = models.ImageField(upload_to='static/region_message/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Region text'
        verbose_name_plural = 'Region text'

    def __str__(self):
        return self.title_uz or self.title_ru


class FilialMessage(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    image = models.ImageField(upload_to='static/filial_message/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Filial text'
        verbose_name_plural = 'Filial text'

    def __str__(self):
        return self.title_uz or self.title_ru

