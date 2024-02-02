from .log import log_errors, autorization, setLanguage
from datetime import datetime, timedelta
from bot.models import UserBot
from .commands import start


@autorization
def handler(update, callback, user, lan):
    # print('user.type=', user.type)
    chat_id = update.message.chat_id
    text = update.message.text
    print('text=', text)
    print(update.message.message_id)
    if text == lan['home_menu']:
        start(update, callback)
    elif text == lan['edit_language']:
        setLanguage(update, callback, user, flag=True)


@log_errors
def set_language(update, callback):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = update.message.text
    text = text.split(' ')[1]
    user = UserBot.objects.get(chat_id=chat_id)
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
