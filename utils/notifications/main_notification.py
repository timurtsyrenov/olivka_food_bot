import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import get_chats_in_db
from loader import bot
from utils.log_app import logger

from .notification_menu import send_notification_menu


async def create_scheduler():
    """
    Функция создания планировщика
    :return:
    """
    global scheduler_menu
    scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")


async def shutdown_scheduler():
    """
    Функция выключения планировщика
    :return:
    """
    scheduler_menu.shutdown()


async def create_job():
    """
    Функция генерации рассылок
    :return:
    """
    # Получаем список чатов из базы данных
    chats = await get_chats_in_db()
    # Удаляем старые задачи
    scheduler_menu.remove_all_jobs()
    for chat_in_db in chats:
        scheduler_menu.add_job(
            send_notification_menu,
            trigger="cron",
            day_of_week="mon-fri",
            hour=chat_in_db[1][:2],
            minute=chat_in_db[1][-2:],
            kwargs={"chat_id": chat_in_db[0], "bot": bot},
        )
    logging.info(scheduler_menu.print_jobs())
    logging.info("завершение функции create_job")
    scheduler_menu.start()


async def regenerate_scheduler():
    """
    Функция перегенерации рассылки меню по расписанию
    :return:
    """
    logger.info("Запуск перегенерации рассылки меню по расписанию")
    await shutdown_scheduler()
    await create_scheduler()
    await create_job()
    logger.info("Перегенерирована рассылка меню по расписанию")
