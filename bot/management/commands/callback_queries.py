from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, InputMediaPhoto
from .log import autorization
import datetime


@autorization
def callback_query(update, callback, user, lan):
    query = update.callback_query
    print('query', query)
    print('query data', query.data)
    print(user.inline_type)
