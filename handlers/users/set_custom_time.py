from aiogram import types
from aiogram.dispatcher import filters

from loader import dp
from utils.log_app import logger
from database import set_custom_time_in_db
from datetime import datetime
from utils.notifications import create_job


# Cоздаем message handler, который ловит команду /set_custom_time HH:MM
@dp.message_handler(filters.Text(startswith="/set_custom_time"))
async def set_custom_time(message: types.Message):
    """
    Асинхронная функция, которая предназначена для изменения времени рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Пользователя с chat_id = {message.chat.id} хочет сменить время рассылки")
    try:
        time_str = message.text.split(" ")[1]
        hours, minutes = time_str.split(":")
        formatted_time = hours.zfill(2) + ":" + minutes
        try:
            datetime.strptime(time_str, "%H:%M")
            await set_custom_time_in_db(message.chat.id, formatted_time)
            await message.answer(f"Установлено время рассылки {formatted_time}")
            logger.info(f"Пользователь с chat_id = {message.chat.id} сменил время рассылки на {formatted_time}")
            await create_job()
            logger.info("Перегенерирована рассылка меню по расписанию")
        except ValueError:
            await message.answer("Необходимо ввести команду в формате /set_custom_time HH:MM")

    except IndexError:
        await message.answer("Необходимо ввести команду в формате /set_custom_time HH:MM")

