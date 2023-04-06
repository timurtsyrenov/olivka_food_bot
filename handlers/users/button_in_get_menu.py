from aiogram import types
from aiogram.types import InputFile

from loader import dp, bot
import utils
import datetime


def get_today() -> int:
    """
    Функция возвращает текущую дату
    :return today: текущая дата в виде числа
    """
    today = datetime.datetime.today().weekday() + 1
    return today


@dp.message_handler(text="/today")  # Cоздаем message handler который ловит команду /today
async def button_today(message: types.Message):
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
        menu = utils.get_menu_to_dict(number_today)
        menu_lunch = "\n".join(str(item) for item in menu.get("lunch").get("food"))  # Формируем строку за 450 рублей
        # из всех блюд для отправки пользователю
        menu_dinner = "\n".join(str(item) for item in menu.get("dinner").get("food"))  # Формируем строку за 300 рублей
        # из всех блюд для отправки пользователю
        menu_to_convert = f'Меню на сегодня: \n' \
                          f'{menu.get("lunch").get("name")} - {menu.get("lunch").get("price")}\n' \
                          f'{menu_lunch}\n\n' \
                          f'{menu.get("dinner").get("name")} - {menu.get("dinner").get("price")}\n' \
                          f'{menu_dinner}'
        utils.convert_text_to_image(menu_to_convert)
        photo_bytes = InputFile(path_or_bytesio='utils/converter/menu_image.png')
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photo_bytes)
