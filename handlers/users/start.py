import logging

from aiogram.types import CallbackQuery, Message

from keyboards.menu_keyboard import menu_keyboard
from utils import get_menu, get_today
from loader import bot, dp


@dp.message_handler(commands=["start", "menu"])
async def start(message: Message):
    """
    Отправляет сообщение "Меню на:" с двумя inline кнопками.
    :param types.Message message:
    :return:
    """
    await message.answer(text="Меню на:", reply_markup=menu_keyboard)


@dp.callback_query_handler(text="today")
async def call_today(call: CallbackQuery):
    """
    Обработчик реагирует на текст "today" присылаемый от пользователя, возвращает фотографию с обедом на сегодня
    :param CallbackQuery call:
    :return:
    """
    number_today = get_today()
    # Проверка на субботу и воскресенье
    if number_today in [6, 7]:
        await bot.send_message(text="На выходных не кормят", chat_id=call.message.chat.id)
        await bot.send_sticker(
            chat_id=call.from_user.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
    else:
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)


@dp.callback_query_handler(text="tomorrow")
async def call_tomorrow(call: CallbackQuery):
    """
    Обработчик реагирует на текст "tomorrow" присылаемый от пользователя, возвращает фотографию с обедом на завтра
    :param CallbackQuery call:
    :return:
    """
    number_today = get_today() + 1
    # Если день недели больше 7, то выводим меню на понедельник
    if number_today > 7:
        number_today = 1
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)
    # Проверка на субботу и воскресенье
    elif number_today in [6, 7]:
        await bot.send_message(text="На выходных не кормят", chat_id=call.message.chat.id)
        await bot.send_sticker(
            chat_id=call.from_user.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
    else:
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)
