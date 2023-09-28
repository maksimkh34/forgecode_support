# Создание и передача обработчиков команд

from telegram.ext import CommandHandler

from bot_defs import *


def exec_handlers(application):
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
