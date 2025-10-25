from data.config import ADMIN_ID
from loader import bot


async def on_startup_notify():
    await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")
