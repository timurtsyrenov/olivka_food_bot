from aiogram import types
from loader import dp, bot
from utils import get_menu, get_today_int
from utils.log_app import logger


# Cоздаем message handler, который ловит команду /today
@dp.message_handler(text="/today")
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
        # Обращаемся к базе и проверяем, если на текущий день недели id_photo
        # нету тогда делаем photo_bytes = get_menu(number_today)
        # Отправляем изображение и забираем с него id_photo после записываем в базу
        # Получаем и посылаем пользователю изображение с меню в виде потока байтов
        # Если id_photo есть на тек день, тогда отправляем сразу фотку
        photo_bytes = get_menu(number_today)
        await message.answer_photo(photo=photo_bytes)
