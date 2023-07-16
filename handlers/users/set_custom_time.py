from aiogram import types
from aiogram.dispatcher import filters

from loader import dp, bot
from utils.log_app import logger
from database import set_time_notification_in_db


# Cоздаем message handler, который ловит команду /set_custom_time
@dp.message_handler(filters.Text(startswith="/set_custom_time"))
async def set_custom_time(message: types.Message):
    """
    Асинхронная функция, которая предназначена для изменения времени рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Пользователя с chat_id = {message.chat.id} хочет сменить время рассылки")
    args = message.text.split(" ")
    print(args[1])
    
    # await set_time_notification_in_db(message.chat.id)
    # await message.answer(f"Рассылка меню по расписанию включена, сообщения будут приходить в 10:00")
