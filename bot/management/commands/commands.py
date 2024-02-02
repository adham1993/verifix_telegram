from .log import autorization, setLanguage
from bot.models import UserBot
from .keyboards import home_menu
from apps.content.models import StartMessage


@autorization
def start(update, callback, user, lan):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    user = UserBot.objects.get(chat_id=chat_id)

    if user.language is None:
        setLanguage(update, callback, user, flag=True)
    else:
        start_message = StartMessage.objects.filter().first()
        if user.language == 'uz':
            reply_text = start_message.title_uz + '\n\n'
        else:
            reply_text = start_message.title_ru + '\n\n'
        image = '{}'.format(start_message.image)
        reply_markup = home_menu(lan)
        if start_message.image:
            update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                       parse_mode='HTML')
        else:
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
