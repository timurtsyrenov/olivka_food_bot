# Функция, которая отправляет сообщения админам, в случае запуска бота
import logging

from aiogram import Dispatcher

from data.config import admin_id


async def on_startup_notify(dp: Dispatcher):
    try:
        text = "Бот запущен"
        await dp.bot.send_message(chat_id=admin_id, text=text)
    except Exception as err:
        logging.exception(err)
