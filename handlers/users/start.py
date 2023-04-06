from aiogram import types

import utils
from handlers.users.button_in_get_menu import get_today
from loader import dp
from loader import bot


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    menu_keyboard = types.InlineKeyboardMarkup(row_width=2)
    menu_keyboard.add(
        types.InlineKeyboardButton(text='Сегодня', callback_data='today'),
        types.InlineKeyboardButton(text='Завтра', callback_data='tomorrow'),
    )
    await message.answer(
        text='Привет, меню на:',
        reply_markup=menu_keyboard
    )


@dp.callback_query_handler(lambda call: call.data == 'today')
async def today(call: types.CallbackQuery):
    number_today = get_today()
    if number_today in [6, 7]:  # Проверка на субботу и воскресенье
        await bot.send_message(text="На выходных не кормят", chat_id=call.message.chat.id)
        await bot.send_sticker(
            chat_id=call.from_user.id,
            sticker=r"CAACAgIAAxkBAAEIVUlkIH22b1zwyhnkOPttEAMkc28UeQAC8xAAAnt4yUv8CBg5xaTu4C8E",
        )
    text_message = handler_today(number_today)
    await bot.send_message(text=text_message, chat_id=call.message.chat.id)


def handler_today(number_today: int) -> str:
    menu = utils.get_menu_to_dict(number_today)
    menu_lunch = "\n".join(str(item) for item in menu.get("lunch").get("food"))  # Формируем строку за 450 рублей
    # из всех блюд для отправки пользователю
    menu_dinner = "\n".join(str(item) for item in menu.get("dinner").get("food"))  # Формируем строку за 300 рублей
    # из всех блюд для отправки пользователю
    text_message = (f"Меню на сегодня: \n"
                    f'{menu.get("lunch").get("name")} - {menu.get("lunch").get("price")}\n'
                    f"{menu_lunch}\n\n"
                    f'{menu.get("dinner").get("name")} - {menu.get("dinner").get("price")}\n'
                    f"{menu_dinner}")
    return text_message
