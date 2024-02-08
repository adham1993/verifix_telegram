from django.contrib import admin
from .models import UserBot, UserProfile, BotToken
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_name', 'bot_username', 'user', 'company',)  # Qo'shimcha maydonlarni qo'shishingiz mumkin


admin.site.register(UserProfile, UserProfileAdmin)


@admin.register(UserBot)
class UserBotAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile', 'company', 'username', 'chat_id', 'full_name', )
    list_display_links = ('id', 'username', 'chat_id', 'full_name', )
    search_fields = ('username', 'full_name', 'chat_id')

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


@admin.register(BotToken)
class BotTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'username')
