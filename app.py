from aiogram import executor
from handlers import dp

# Импортируем функцию, которая отправляет сообщение о запуске бота всем админам
from handlers.admin.notify_admins import on_startup_notify

# Импортируем функцию, которая устанавливает команды для бота
from utils.set_bot_commands import set_default_commands
from utils.log_app import logger

"""
Основной файл
Чтобы запустить бота нуобходимо запустить данный скрипт
"""


# Создаем асинхронную функцию которая будет запускаться по запуску бота
async def on_startup(dp):
    # Отправлем сообщение админу
    await on_startup_notify(dp)

    # Устанавливаем каманды для бота
    await set_default_commands(dp)

    logger.info("Бот запущен")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
