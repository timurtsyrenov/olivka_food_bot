import middlewares
from aiogram import executor
# Импортируем функцию для создания/соединения с базой данных
from database import connect_db, disconnect_db
from handlers import dp
# Импортируем функцию, которая отправляет сообщение о запуске бота всем админам
from handlers.admin.notify_admins import on_startup_notify
# Импортируем переменные, которые отправляют сообщения по расписанию
from utils import create_job, create_scheduler, shutdown_scheduler
from utils.log_app import logger
# Импортируем функцию, которая устанавливает команды для бота
from utils.set_bot_commands import set_default_commands

"""
Основной файл
Чтобы запустить бота необходимо запустить данный скрипт
"""


# Создаем асинхронную функцию которая будет запускаться по запуску бота
async def on_startup(dp):
    # Устанавливаем команды для бота
    await set_default_commands(dp)
    logger.info("Установлены команды для бота")

    # Подключаем Middleware
    middlewares.setup(dp)
    logger.info("Подключен Middleware")

    # Подключаем базу данных
    await connect_db()
    logger.info("База данных подключена")

    # Инициализируем планировщик
    await create_scheduler()
    logger.info("Инициализирован планировщик")

    # Запускаем рассылку меню по расписанию
    await create_job()
    logger.info("Запущена рассылка меню по расписанию")

    # Отправляем сообщение админу
    await on_startup_notify(dp)
    logger.info("Отправлено сообщение админу о запуске бота")

    logger.info("Бот запущен")


# Создаем асинхронную функцию которая будет запускаться по остановке работы бота
async def on_shutdown(dp):
    await disconnect_db()
    logger.info("Соединение с базой данных завершено")
    await shutdown_scheduler()
    logger.info("Планировщик отключен")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
