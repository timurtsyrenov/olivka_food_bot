import datetime

from aiogram import types

import utils
from loader import dp
from loader import bot


@dp.message_handler(commands=["start", "menu"])
async def start(message: types.Message):
    """
    Отправляет сообщение Меню на: с двумя inline кнопками.
    :param types.Message message:
    :return:
    """
    menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
    menu_keyboard.add(
        types.InlineKeyboardButton(text="Сегодня", callback_data="today"),
        types.InlineKeyboardButton(text="Завтра", callback_data="tomorrow"),
    )
    await message.answer(text="Меню на:", reply_markup=menu_keyboard)


@dp.callback_query_handler(lambda call: call.data == "today")
async def handler_today(call: types.CallbackQuery):
    """
    Обработчик нажатия кнопки "Сегодня".
    :param types.CallbackQuery call:
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
        text_message = call_today(number_today)
        await bot.send_message(text=text_message, chat_id=call.message.chat.id)


@dp.callback_query_handler(lambda call: call.data == "tomorrow")
async def handler_tomorrow(call: types.CallbackQuery):
    """
    Обработчик нажатия кнопки "Завтра".
    :param types.CallbackQuery call:
    :return:
    """
    number_today = get_today() + 1
    # Если день недели больше 7, то выводим меню на понедельник
    if number_today > 7:
        number_today = 1
        text_message = call_today(number_today)
        await bot.send_message(text=text_message, chat_id=call.message.chat.id)
    # Проверка на субботу и воскресенье
    elif number_today in [6, 7]:
        await bot.send_message(text="На выходных не кормят", chat_id=call.message.chat.id)
        await bot.send_sticker(
            chat_id=call.from_user.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )


def get_today() -> int:
    """
    Функция возвращает текущую дату
    :return int today: текущая дата в виде числа
    """
    today = datetime.datetime.today().weekday() + 1
    return today


def call_today(number_today: int) -> str:
    """
    Функция возвращает меню блюд на запрошенный день
    :param int number_today: текущая дата в виде числа
    :return str text_message: текущий блюд для отправки пользователю
    """
    menu = utils.get_menu_to_dict(number_today)
    # Формируем строку за 450 рублей из всех блюд для отправки пользователю
    menu_lunch = "\n".join(str(item) for item in menu.get("lunch").get("food"))
    # Формируем строку за 300 рублей из всех блюд для отправки пользователю
    menu_dinner = "\n".join(str(item) for item in menu.get("dinner").get("food"))
    text_message = (
        f"Меню на сегодня: \n"
        f'{menu.get("lunch").get("name")} - {menu.get("lunch").get("price")}\n'
        f"{menu_lunch}\n\n"
        f'{menu.get("dinner").get("name")} - {menu.get("dinner").get("price")}\n'
        f"{menu_dinner}"
    )
    return text_message
