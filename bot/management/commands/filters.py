from telegram.ext import BaseFilter
from telegram import Update

from abc import abstractmethod


class FilterLanguage(BaseFilter):

    def __call__(self, update: Update):
        return self.filter(update.effective_message)

    # @abstractmethod
    def filter(self, message):

        return message.text in ['🇺🇿 UZ', '🇷🇺 RU']
