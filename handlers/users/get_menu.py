from aiogram import types
from loader import dp
from keyboards.default import kb_get_menu

@dp.message_handler(text='/get_menu')  # Создаем message handler который ловит команду /get_menu
async def command_get_menu(message: types.Message):  # Создаем асинхронную функцию, которая выводит меню с выбором дня
    await message.answer("Выбери день из меню: ", reply_markup=kb_get_menu)




