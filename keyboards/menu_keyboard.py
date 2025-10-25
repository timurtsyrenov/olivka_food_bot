from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура из двух кнопок реагирует на start и menu
menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сегодня", callback_data="today"),
            InlineKeyboardButton(text="Завтра", callback_data="tomorrow"),
        ]
    ],
    row_width=2,
)
