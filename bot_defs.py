# Функции, которые будут помещены в обработчики (одна команда бота = одна функция)

from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Bot is working ({datetime.now().hour}:{datetime.now().minute})")
