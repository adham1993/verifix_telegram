from django.db import models

# Create your models here.


class UserBot(models.Model):
    language = models.CharField(max_length=10, null=True, blank=True)
    chat_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)
    full_name = models.CharField(max_length=128, null=True, blank=True)
    passport = models.IntegerField(null=True, blank=True, default=None)
    type = models.CharField(max_length=100, null=True, blank=True)
    inline_type = models.CharField(max_length=100, null=True, blank=True)
    new_employee = models.BooleanField(default=False)
    old_employee = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or self.username or self.chat_id

    class Meta:
        verbose_name = "UserBot"
        verbose_name_plural = "Bot Users"


