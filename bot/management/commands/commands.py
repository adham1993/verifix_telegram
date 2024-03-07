from .log import autorization, setLanguage
from bot.models import UserBot, UserProfile
from .keyboards import home_menu
from apps.content.models import StartMessage


@autorization
def start(update, callback, user, lan):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    if user.language is None:
        setLanguage(update, callback, user, flag=True)
    # elif user.type == 'send_contact':
    #     send_contact(update, callback, user, lan)
    else:
        start_message = StartMessage.objects.filter(user_profile=user_profile_filter).first()
        if user.language == 'uz':
            reply_text = start_message.title_uz + '\n\n'
        elif user.language == 'en':
            if start_message.title_en:
                reply_text = start_message.title_en + '\n\n'
            else:
                reply_text = start_message.title_uz + '\n\n'
        else:
            if start_message.title_ru:
                reply_text = start_message.title_ru + '\n\n'
            else:
                reply_text = start_message.title_uz + '\n\n'
        image = '{}'.format(start_message.image)
        reply_markup = home_menu(lan)
        if start_message.image:
            update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')