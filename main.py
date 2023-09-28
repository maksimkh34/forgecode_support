# Основа бота (https://t.me/FCSS_bot)

from api_key import API_KEY
from handling import exec_handlers
from logger import Logger, LogType
from export import boot_options

from telegram.ext import ApplicationBuilder


if __name__ == '__main__':
    choice = input("Enter boot flags: ")
    boot_options(choice)

    logger = Logger()
    logger.log("Main started! ", LogType.OK)

    application = ApplicationBuilder().token(API_KEY).build()
    exec_handlers(application)
    logger.log("Pooling...  ",)
    application.run_polling()
    logger.log("Program finished. ", LogType.OK)
