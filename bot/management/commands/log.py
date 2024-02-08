from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from bot.models import UserBot, BotToken, UserProfile
from telegram.ext import ConversationHandler
from .keyboards import language_menu, home_menu
import importlib, json

from .utils import get_language


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Error: {e}'
            print(error_message)
            print(f)
            raise e

    return inner


def setLanguage(update, callback, user, flag=False, *args, **kwargs):
    print('setLanguage')
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    data = eval(str(update.message))
    try:
        if user.language:
            language = user.language
            lan = get_language(language)

        else:
            language = 'uz'
            lan = get_language(language)
    except:
        try:
            default_lang_user = data['from']['language_code']
        except:
            default_lang_user = 'uz'
        lan = get_language(default_lang_user)

    if flag:
        reply_text = lan['select_language']
    else:
        reply_text = lan['select_lang']

    user.type = 'set_lang'
    user.save()

    reply_markup = language_menu(lan)
    res = update.message.reply_text(text=reply_text, reply_markup=reply_markup)


def autorization(f):
    def inner(update, callback, *args, **kwargs):
        try:
            if hasattr(update.message, 'chat_id'):
                chat_id = update.message.chat_id
                message_id = update.message.message_id
            else:
                chat_id = update.callback_query.message.chat.id
            bot_username = callback.bot.username
            bot_filter = BotToken.objects.filter(username=bot_username).first()
            user_profile_filter = UserProfile.objects.filter(company=bot_filter.company).first()
            user = UserBot.objects.filter(chat_id=chat_id, bot_username=bot_username).first()
            if not user:
                user = UserBot.objects.create(
                    chat_id=chat_id,
                    company=bot_filter.company,
                    user_profile=user_profile_filter,
                    bot_username=bot_username
                )
                user.save()
            is_break = False
            if user.language is None:
                is_break = True
                setLanguage(update, callback, user, *args, **kwargs)

            lan = get_language(user.language)

            if not is_break:
                return f(update, callback, user, lan, *args, **kwargs)
        except Exception as e:
            error_message = f'Error: {e}'
            print(error_message)
            print(f)
            raise e

    return inner


def clear_home(update, callback, activity):
    try:
        detail = json.loads(activity.detail)
        if "home_message" in detail:
            if hasattr(update.message, 'chat_id'):
                callback.bot.deleteMessage(chat_id=update.message.chat_id, message_id=int(detail['home_message']))
            del detail['home_message']
            activity.detail = json.dumps(detail)
            activity.save()
    except Exception as e:
        error_message = f'Error: {e}'
        print(error_message)
        print('clear_home_function')