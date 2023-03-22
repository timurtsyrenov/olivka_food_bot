from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_get_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/today'),
            KeyboardButton(text='/monday'),
            KeyboardButton(text='/tuesday'),
        ],
        [
            KeyboardButton(text='/wednesday'),
            KeyboardButton(text='/thursday'),
            KeyboardButton(text='/friday'),
        ]
    ],
    resize_keyboard=True
)