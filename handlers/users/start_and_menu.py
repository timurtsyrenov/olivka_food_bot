from aiogram.types import CallbackQuery, Message

from keyboards import menu_keyboard
from utils import get_menu, get_today_int
from loader import bot, dp
from utils.log_app import logger
from database import create_chat_id
import emoji
from utils.misc import rate_limit
from data.config import MIDDLEWARE_BAN


# Cоздаем message handler, который ловит команды start и menu
@rate_limit(limit=MIDDLEWARE_BAN)
@dp.message_handler(commands=["start"])
async def start(message: Message):
    """
    Запускает бота, и создает запись в таблице оповещений
    :param types.Message message:
    :return:
    """
    logger.info(f"Запуск бота у пользователя с id = {message.chat.id}")
    await create_chat_id(message.chat.id)
    await message.answer(
        "Бот запущен"
        + emoji.emojize(" 🤖")
        + f"\nЧто бы включить рассылку меню используйте /on_notification"
        + emoji.emojize(" 💌")
    )


@rate_limit(limit=MIDDLEWARE_BAN)
@dp.message_handler(commands=["menu"])
async def menu(message: Message):
    """
    Отправляет сообщение "Меню на:" с двумя inline кнопками.
    :param types.Message message:
    :return:
    """
    logger.info(f"Команда: {message.text}")
    logger.debug(f"Вызов меню: {message}")
    await message.answer(text="Меню на:", reply_markup=menu_keyboard)


# Cоздаем message handler, который ловит команду today
@dp.callback_query_handler(text="today")
async def call_today(call: CallbackQuery):
    """
    Обработчик реагирует на текст "today" присылаемый от пользователя, возвращает фотографию с обедом на сегодня
    :param CallbackQuery call:
    :return:
    """
    logger.info(f"Команда callback: {call.data}")
    logger.info(f"Вызов меню: {call}")
    number_today = get_today_int()
    # Проверка на субботу и воскресенье
    if number_today in [6, 7]:
        await bot.send_message(
            text="На выходных не кормят", chat_id=call.message.chat.id
        )
        await bot.send_sticker(
            chat_id=call.message.chat.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
        # Подтверждение приема call
        await call.answer()
    else:
        # Получаем и посылаем пользователю изображение с меню в виде потока байтов
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)
        # Подтверждение приема call
        await call.answer()


# Cоздаем message handler, который ловит команду tomorrow
@dp.callback_query_handler(text="tomorrow")
async def call_tomorrow(call: CallbackQuery):
    """
    Обработчик реагирует на текст "tomorrow" присылаемый от пользователя, возвращает фотографию с обедом на завтра
    :param CallbackQuery call:
    :return:
    """
    logger.info(f"Команда callback: {call.data}")
    logger.info(f"Вызов меню: {call}")
    number_today = get_today_int() + 1
    # Если день недели больше 7, то выводим меню на понедельник
    if number_today > 7:
        number_today = 1
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)
        # Подтверждение приема call
        await call.answer()
    # Проверка на субботу и воскресенье
    elif number_today in [6, 7]:
        await bot.send_message(
            text="На выходных не кормят", chat_id=call.message.chat.id
        )
        await bot.send_sticker(
            chat_id=call.message.chat.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
        # Подтверждение приема call
        await call.answer()
    else:
        # Получаем и посылаем пользователю изображение с меню в виде потока байтов
        photo_bytes = get_menu(number_today)
        await bot.send_photo(photo=photo_bytes, chat_id=call.message.chat.id)
        # Подтверждение приема call
        await call.answer()
