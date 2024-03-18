from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, InlineQueryHandler
from telegram.utils.request import Request
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .commands import start
from .messages import handler, set_language, image
from .filters import FilterLanguage
from .callback_queries import callback_query
from .main import main_phone
from bot.models import BotToken


WEBHOOK_URL_BASE = "https://telegram.greenwhite.uz/webhook/"


@csrf_exempt
def webhook(request, token):
    bot_token = BotToken.objects.get(token=token)
    bot = Bot(token=bot_token.token)
    updater = Updater(bot=bot, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(FilterLanguage(), set_language))
    # updater.dispatcher.add_handler(MessageHandler(Filters.document, send_document))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_query))
    updater.dispatcher.add_handler(MessageHandler(Filters.photo, image))
    updater.dispatcher.add_handler(MessageHandler(Filters.contact, main_phone))
    data = json.loads(request.body.decode("utf-8"))
    update = Update.de_json(data, bot)
    updater.dispatcher.process_update(update)

    return HttpResponse("ok")


def set_webhook(request, token):
    bot_token = BotToken.objects.get(token=token)
    bot = Bot(token=bot_token.token)
    updater = Updater(bot=bot, use_context=True)

    port = 8000 + bot_token.id

    webhook_url = f"{WEBHOOK_URL_BASE}{bot_token.token}/"
    updater.bot.set_webhook(
        listen="127.0.0.1",
        port=port,
        url_path=bot_token.token,
        key="/etc/letsencrypt/live/telegram.greenwhite.uz/privkey.pem",
        cert="/etc/letsencrypt/live/telegram.greenwhite.uz/fullchain.pem",
        webhook_url=webhook_url
    )

    return HttpResponse(webhook_url)


def delete_webhook(request, token):
    bot_token = BotToken.objects.get(token=token)
    bot = Bot(token=bot_token.token)
    updater = Updater(bot=bot, use_context=True)

    updater.bot.delete_webhook()
    return HttpResponse("ok")


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        bots = BotToken.objects.all()
        updater_list = []

        for bot_info in bots:
            bot_token = bot_info.token
            updater = self.create_updater(bot_token)
            updater_list.append(updater)

        for updater in updater_list:
            updater.start_polling()

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
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, main_phone))
        updater.dispatcher.add_handler(MessageHandler(Filters.photo, image))

        return updater
