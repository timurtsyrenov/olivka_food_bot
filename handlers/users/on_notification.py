from aiogram import types
from loader import dp
from utils.log_app import logger
from database import on_notification_in_db

# Cоздаем message handler, который ловит команду /on_notification
@dp.message_handler(text="/on_notification")
async def on_notification(message: types.Message):
    """
    Асинхронная функция, которая предназначена для включения рассылки меню по расписанию
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Включение рассылки у пользователя с chat_id = {message.chat.id}")
    await on_notification_in_db(message.chat.id)
    await message.answer(f"Рассылка меню по расписанию включена, сообщения будут приходить в 10:00")
