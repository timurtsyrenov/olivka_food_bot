from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_get_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/today"),
            KeyboardButton(text="/tomorrow"),
        ],
    ],
    resize_keyboard=True,
)
