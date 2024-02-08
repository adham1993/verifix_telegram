from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from apps.company.models import (
    Region,
    Filial
)
from bot.models import UserProfile


def language_menu(lan):
    keyboard = [
            [KeyboardButton("🇺🇿 UZ"), KeyboardButton("🇷🇺 RU"), KeyboardButton("🇬🇧 EN")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def home_menu(lan):
    keyboard = [
        [KeyboardButton(lan['filial']), KeyboardButton(lan['vacancy'])],
        [KeyboardButton(lan['contact']), KeyboardButton(lan['about_company'])],
        [KeyboardButton(lan['edit_language'])]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def regions_button(callback, user, lan):
    # bot_username = callback.bot.username
    # user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    regions = Region.objects.all()
    keyboard = []
    c = 0
    b = []
    region_len = len(regions)
    if user.language == 'uz':
        for region in regions:
            a = KeyboardButton(str(region.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for region in regions:
            a = KeyboardButton(str(region.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for region in regions:
            a = KeyboardButton(str(region.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def filials_button(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    region = user.region
    filials = Filial.objects.filter(user_profile=user_profile_filter, region=region)
    keyboard = []
    c = 0
    b = []
    region_len = len(filials)
    if user.language == 'uz':
        for filial in filials:
            a = KeyboardButton(str(filial.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for filial in filials:
            a = KeyboardButton(str(filial.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for filial in filials:
            a = KeyboardButton(str(filial.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup
