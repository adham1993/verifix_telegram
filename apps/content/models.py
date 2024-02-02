from django.db import models

# Create your models here.


class StartMessage(models.Model):
    title_uz = models.TextField(null=True, blank=True, default=None)
    title_ru = models.TextField(null=True, blank=True, default=None)
    title_en = models.TextField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='static/start_message/images', null=True, blank=True)

    class Meta:
        verbose_name = 'Bosh sahifa matni'
        verbose_name_plural = 'Home text'

    def __str__(self):
        return self.title_uz or self.title_ru
