from aiogram import types
from loader import dp, bot
import utils
import datetime


def today():
    return datetime.datetime.today().weekday() + 1  # Переменная, хранящая номер сегодняшнего дня недели


# number_today = 6

@dp.message_handler(text='/today')  # Cоздаем message handler который ловит команду /today
async def button_today(message: types.Message):  # Создаем асинхронную функцию, которая отправляет меню на сегодня
    number_today = today()
    if number_today in [6, 7]:  # Проверка на субботу и воскресенье
        await message.answer('На выходных не кормят')
        await bot.send_sticker(chat_id=message.from_user.id,
                               sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E")
    else:
        menu = utils.get_menu_to_dict(number_today)
        await message.answer(f'Меню на сегодня: \n'
                             f'{menu}')
