from apps.content.models import (
    FilialMessage,
    RegionMessage
)
from bot.models import UserProfile
from .keyboards import (
    regions_button,
    filials_button
)


def regions(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    filial_message = RegionMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = filial_message.title_uz + '\n\n'
    elif user.language == 'en':
        if filial_message.title_en:
            reply_text = filial_message.title_en + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    else:
        if filial_message.title_ru:
            reply_text = filial_message.title_ru + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    image = '{}'.format(filial_message.image)
    reply_markup = regions_button(callback, user, lan)
    if filial_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'region'
    user.save()


def filials(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    filial_message = FilialMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = filial_message.title_uz + '\n\n'
    elif user.language == 'en':
        if filial_message.title_en:
            reply_text = filial_message.title_en + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    else:
        if filial_message.title_ru:
            reply_text = filial_message.title_ru + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    image = '{}'.format(filial_message.image)
    reply_markup = filials_button(callback, user, lan)
    if filial_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'filials'
    user.save()
