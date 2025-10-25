import emoji
from aiogram import types
from data.config import MIDDLEWARE_BAN
from database import get_chat_id, on_notification_in_db
from loader import dp
from utils import regenerate_scheduler
from utils.log_app import logger
from utils.misc import rate_limit


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
        f"Рассылка меню по расписанию включена, сообщения будут приходить в {time[1]}" + emoji.emojize(" ⏳")
    )
    await regenerate_scheduler()
