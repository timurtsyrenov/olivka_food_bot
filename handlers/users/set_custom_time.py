from datetime import datetime

import emoji
from aiogram import Router, types
from aiogram.filters import Command
from data.config import MIDDLEWARE_BAN
from database import set_custom_time_in_db
from utils import regenerate_scheduler
from utils.log_app import logger
from utils.misc import rate_limit

router = Router()


# Cоздаем message handler, который ловит команду /set_custom_time HH:MM
@rate_limit(limit=MIDDLEWARE_BAN)
@router.message(Command("/set_custom_time"))
async def set_custom_time(message: types.Message):
    """
    Асинхронная функция, которая предназначена для изменения времени рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Пользователя с chat_id = {message.chat.id} меняет время рассылки")
    try:
        time_str = message.text.split(" ")[1]
        hours, minutes = time_str.split(":")
        formatted_time = hours.zfill(2) + ":" + minutes
        try:
            datetime.strptime(time_str, "%H:%M")
            await set_custom_time_in_db(message.chat.id, formatted_time)
            await message.answer(f"Установлено время рассылки {formatted_time}" + emoji.emojize(" ⏳"))
            logger.info(f"Пользователь с chat_id = {message.chat.id} сменил время рассылки на {formatted_time}")
            await regenerate_scheduler()
        except ValueError:
            await message.answer("Необходимо ввести команду в формате /set_custom_time HH:MM" + emoji.emojize(" 🙅‍♂️"))

    except (IndexError, ValueError):
        await message.answer("Необходимо ввести команду в формате /set_custom_time HH:MM" + emoji.emojize(" 🙅‍♂️"))
