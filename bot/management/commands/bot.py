from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, InlineQueryHandler
from telegram.utils.request import Request
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .commands import start
from .messages import handler, set_language
from .filters import FilterLanguage
from .callback_queries import callback_query
from bot.models import BotToken


@csrf_exempt
def webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(FilterLanguage(), set_language))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document, send_document))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))
    data = json.loads(request.body.decode("utf-8"))
    update = Update.de_json(data, bot)
    updater.dispatcher.process_update(update)

    return HttpResponse("ok")


def set_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    updater.bot.set_webhook("https://bot.miniature.uz" + "/webhook/" + settings.TOKEN)
    return HttpResponse("https://bot.miniature.uz" + "/webhook/" + settings.TOKEN)


def delete_webhook(request):
    bot = Bot(
        token=settings.TOKEN,
    )

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.bot.delete_webhook()
    return HttpResponse("ok")


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        bots = BotToken.objects.all()
        updater_list = []  # Bu ro'yxatda har bir bot uchun Updater obyektlarini saqlaymiz

        for bot_info in bots:
            bot_token = bot_info.token
            updater = self.create_updater(bot_token)
            updater_list.append(updater)

        # Barcha botlarni bir vaqtda ishga tushiramiz
        for updater in updater_list:
            updater.start_polling()

        # Barcha botlar tugaganida ishni yakunlaymiz
        for updater in updater_list:
            updater.idle()

    def create_updater(self, token):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            token=token,
        )
        updater = Updater(
            bot=bot,
            use_context=True,
        )
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(FilterLanguage(), set_language))
        # updater.dispatcher.add_handler(MessageHandler(Filters.document, send_document))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))
        updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))

        return updater
#
# class Command(BaseCommand):
#     help = 'Telegram bot'
#
#     def handle(self, *args, **options):
#         bots = BotToken.objects.all()
#         for bot in bots:
#             request = Request(
#                 connect_timeout=0.5,
#                 read_timeout=1.0,
#             )
#             bot = Bot(
#                 # request=request,
#                 token=bot.token,
#                 # base_url=settings.PROXY_URL,
#             )
#             updater = Updater(
#                 bot=bot,
#                 use_context=True,
#             )
#             updater.dispatcher.add_handler(CommandHandler('start', start))
#             updater.dispatcher.add_handler(MessageHandler(FilterLanguage(), set_language))
#             # updater.dispatcher.add_handler(MessageHandler(Filters.document, send_document))
#             updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))
#             updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))
#
#             # updater.dispatcher.add_handler(MessageHandler(Filters.contact, text_contact))
#             # updater.dispatcher.add_handler(MessageHandler(Filters.photo, image))
#
#             updater.start_polling()
#             updater.idle()
