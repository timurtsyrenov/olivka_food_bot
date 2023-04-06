from aiogram import executor
from handlers import dp
from handlers.admin.notify_admins import (
    on_startup_notify,
)  # Импортируем функцию, которая отправляет сообщение о запуске бота всем админам
from utils.set_bot_commands import set_default_commands  # Импортируем функцию, которая устанавливает команды для бота
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")


# Основной файл
async def on_startup(dp):  # Создаем асинхронную функцию которая будет запускаться по запуску бота
    await on_startup_notify(dp)

    await set_default_commands(dp)

    logging.info("Бот запущен")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
