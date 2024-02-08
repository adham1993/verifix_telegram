from .log import log_errors, autorization, setLanguage
from datetime import datetime, timedelta
from bot.models import UserBot
from .commands import start
from .main import (
    regions,
    filials
)
from apps.company.models import (
    Region,
    Filial
)


@autorization
def handler(update, callback, user, lan):
    # print('user.type=', user.type)
    chat_id = update.message.chat_id
    text = update.message.text
    bot_username = callback.bot.username
    if text == lan['home_menu']:
        start(update, callback)
    elif text == lan['edit_language']:
        setLanguage(update, callback, user, flag=True)
    elif text == lan['filial']:
        regions(update, callback, user, lan)
    elif user.type == 'region':
        if text == lan['back']:
            start(update, callback)
        else:
            if user.language == 'uz':
                region = Region.objects.filter(name_uz=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)
            elif user.language == 'ru':
                region = Region.objects.filter(name_ru=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)
            else:
                region = Region.objects.filter(name_en=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)




@log_errors
def set_language(update, callback):
    print('set_language')
    bot_username = callback.bot.username
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = update.message.text
    text = text.split(' ')[1]
    user = UserBot.objects.get(chat_id=chat_id, bot_username=bot_username)
    languages = (('uz', 'UZ'), ('ru', 'RU'), ('en', 'EN'))
    lan = 'uz'
    for key, value in enumerate(languages):
        (lowercase, uppercase) = value
        if uppercase == text:
            lan = lowercase
    if user:
        user.language = lan
        user.save()
        user.type = 'set_lang'
        user.save()
        start(update, callback)
