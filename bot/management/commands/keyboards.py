from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


def language_menu(lan):
    keyboard = [
        [KeyboardButton("🇺🇿 UZ"), KeyboardButton("🇷🇺 RU")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def home_menu(lan):
    keyboard = [
        [KeyboardButton(lan['filial']), KeyboardButton(lan['vacancy'])],
        [KeyboardButton(lan['contact']), KeyboardButton(lan['about_company'])],
        [KeyboardButton(lan['edit_language'])]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup
