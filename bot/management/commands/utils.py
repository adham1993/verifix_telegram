import importlib
from bot.models import UserBot
import json


def get_language(from_where):
    lan = importlib.import_module("bot.languages." + from_where).words
    return lan


def get_chat_id_by_update(update):
    return update.message.chat_id


def get_user_by_chat_id(update=None, message=None, callback=None):
    if update:
        chat_id = get_chat_id_by_update(update)
    elif message:
        chat_id = message.chat_id
    elif callback:
        chat_id = callback.message.chat_id
    user = UserBot.objects.filter(chat_id=chat_id).first()
    return user
