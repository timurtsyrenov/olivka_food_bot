from aiogram import types
from data.config import MIDDLEWARE_BAN
from loader import bot, dp
from utils import get_menu, get_today_int
from utils.log_app import logger
from utils.misc import rate_limit


# Cоздаем message handler, который ловит команду /today
@rate_limit(limit=MIDDLEWARE_BAN)
@dp.message_handler(commands=["today"])
async def today(message: types.Message):
    """
    Асинхронная функция, которая отправляет меню на сегодня
    :parameter message: Сообщение от пользователя
    """
    logger.info(f"Вызов меню через / : {message}")
    number_today = get_today_int()
    # Проверка на субботу и воскресенье
    if number_today in [6, 7]:
        await message.answer("На выходных не кормят")
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
    else:
        # Получаем и посылаем пользователю изображение с меню в виде потока байтов
        photo_bytes = get_menu(number_today)
        await message.answer_photo(photo=photo_bytes)
