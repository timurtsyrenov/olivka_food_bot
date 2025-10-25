import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.log_app import logger
from .notification_menu import send_notification_menu

scheduler_menu = None  # глобальная переменная для scheduler

async def create_scheduler():
    """
    Создание планировщика
    """
    global scheduler_menu
    if scheduler_menu is None:
        scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")


async def shutdown_scheduler():
    """
    Выключение планировщика
    """
    global scheduler_menu
    if scheduler_menu and scheduler_menu.running:
        scheduler_menu.shutdown()
        scheduler_menu = None


async def create_job():
    """
    Генерация рассылок
    """
    global scheduler_menu
    if scheduler_menu is None:
        await create_scheduler()

    # локальный импорт, чтобы разорвать циклический импорт
    from database.sqlite import get_chats_in_db
    from loader import bot

    chats = await get_chats_in_db()
    scheduler_menu.remove_all_jobs()

    for chat_in_db in chats:
        scheduler_menu.add_job(
            send_notification_menu,
            trigger="cron",
            day_of_week="mon-fri",
            hour=int(chat_in_db[1][:2]),
            minute=int(chat_in_db[1][-2:]),
            kwargs={"chat_id": chat_in_db[0], "bot": bot},
        )

    logging.info("Pending jobs:\n%s", scheduler_menu.print_jobs())

    if not scheduler_menu.running:
        scheduler_menu.start()


async def regenerate_scheduler():
    """
    Перегенерация рассылки меню по расписанию
    """
    await shutdown_scheduler()
    await create_scheduler()
    await create_job()
    logger.info("Перегенерирована рассылка меню по расписанию")