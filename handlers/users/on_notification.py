from aiogram import types
from loader import dp
from utils.log_app import logger
from database import on_notification_in_db, get_chat_id
from utils import regenerate_scheduler
import emoji
from utils.misc import rate_limit
from data.config import MIDDLEWARE_BAN


# Cоздаем message handler, который ловит команду /on_notification
@rate_limit(limit=MIDDLEWARE_BAN)
@dp.message_handler(commands=["on_notification"])
async def on_notification(message: types.Message):
    """
    Асинхронная функция, которая предназначена для включения рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Включение рассылки у пользователя с chat_id = {message.chat.id}")
    await on_notification_in_db(message.chat.id)
    time = await get_chat_id(message.chat.id)
    await message.answer(
        f"Рассылка меню по расписанию включена, сообщения будут приходить в {time[1]}"
        + emoji.emojize(" ⏳")
    )
    await regenerate_scheduler()
