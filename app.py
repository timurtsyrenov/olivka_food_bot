import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from database import connect_db, disconnect_db
from dotenv import load_dotenv
from handlers import dp
from handlers.admin.notify_admins import on_startup_notify
from middlewares import setup as setup_middlewares
from utils import create_job, create_scheduler, shutdown_scheduler
from utils.log_app import logger
from utils.set_bot_commands import set_default_commands

# Загружаем переменные окружения
load_dotenv()

# Создаем экземпляр бота
bot = Bot(token=getenv("BOT_TOKEN"))
dispatcher = Dispatcher()

# Регистрируем роутеры
dispatcher.include_router(dp)


async def on_startup():
    """Функция, выполняемая при запуске бота"""
    await set_default_commands(bot)
    logger.info("Установлены команды для бота")

    # Подключаем Middleware
    setup_middlewares(dispatcher)
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
    await on_startup_notify()
    logger.info("Отправлено сообщение админу о запуске бота")

    logger.info("Бот запущен")


async def on_shutdown():
    """Функция, выполняемая при остановке бота"""
    await disconnect_db()
    logger.info("Соединение с базой данных завершено")
    await shutdown_scheduler()
    logger.info("Планировщик отключен")


async def main():
    await on_startup()

    try:
        await dispatcher.start_polling(bot)
    finally:
        await on_shutdown()


if __name__ == "__main__":
    asyncio.run(main())
