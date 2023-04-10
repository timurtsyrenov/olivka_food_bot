from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура из двух кнопок реагирует на /menu
menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сегодня", callback_data="today"),
            InlineKeyboardButton(text="Завтра", callback_data="tomorrow"),
        ]
    ],
    row_width=2,
)
