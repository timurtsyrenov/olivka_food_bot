import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loader import bot
from utils.notifications.notification_menu import send_notification_menu
from database import get_chats_in_db


async def create_job():
    """
    Функция генерации рассылок
    :return:
    """
    scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")
    chats = get_chats_in_db()
    for chat_in_db in chats:
        scheduler_menu.add_job(
            send_notification_menu,
            trigger="cron",
            day_of_week="mon-fri",
            hour=chat_in_db[1][:2],
            minute=chat_in_db[1][-2:],
            kwargs={"chat_id": chat_in_db[0], "bot": bot},
        )
#    scheduler_menu.print_jobs()
    scheduler_menu.start()
