from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сегодня", callback_data="today"),
            InlineKeyboardButton(text="Завтра", callback_data="tomorrow"),
        ]
    ],
    row_width=2,
)
