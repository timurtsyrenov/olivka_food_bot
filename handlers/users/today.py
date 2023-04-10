from aiogram import types
from loader import dp, bot
from .start import get_today
from .start import get_menu


@dp.message_handler(text="/today")  # Cоздаем message handler который ловит команду /today
async def today(message: types.Message):
    """
    Асинхронная функция, которая отправляет меню на сегодня
    :parameter message: Сообщение от пользователя
    """
    number_today = get_today()
    if number_today in [6, 7]:  # Проверка на субботу и воскресенье
        await message.answer("На выходных не кормят")
        await bot.send_sticker(
            chat_id=message.from_user.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
    else:
        photo_bytes = get_menu(number_today)
        await message.answer_photo(photo=photo_bytes)
