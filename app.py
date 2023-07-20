from aiogram import executor
from handlers import dp

# Импортируем функцию, которая отправляет сообщение о запуске бота всем админам
from handlers.admin.notify_admins import on_startup_notify

# Импортируем функцию, которая устанавливает команды для бота
from utils.set_bot_commands import set_default_commands

# Импортируем переменные, которые отправляют сообщения по расписанию
from utils import create_job
from utils.log_app import logger

# Импортируем функцию для создания/соединения с базой данных
from database import connect_db

"""
Основной файл
Чтобы запустить бота необходимо запустить данный скрипт
"""


# Создаем асинхронную функцию которая будет запускаться по запуску бота
async def on_startup(dp):
    # Отправляем сообщение админу
    await on_startup_notify(dp)
    logger.info("Отправлено сообщение админу о запуске бота")

    # Устанавливаем команды для бота
    await set_default_commands(dp)
    logger.info("Установлены команды для бота")

    # Подключаем базу данных
    await connect_db()
    logger.info("База данных подключена")

    # Запускаем рассылку меню по расписанию
    create_job()
    logger.info("Запущена рассылка меню по расписанию")

    logger.info("Бот запущен")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
