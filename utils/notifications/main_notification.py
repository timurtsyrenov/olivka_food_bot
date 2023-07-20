import logging
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loader import bot
from utils.notifications.notification_menu import send_notification_menu
from database import get_chats_in_db

# Инициализируем переменную для рассылки меню по расписанию
# scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")
# scheduler_menu.add_job(
#     send_notification_menu,
#     trigger="cron",
#     day_of_week="mon-fri",
#     hour=CUSTOM_TIME,
#     minute=00,
#     kwargs={"bot": bot},
# )


async def create_job():
    """
    Функция генерации рассылок
    :return:
    """
    scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")
    # loop = asyncio.get_event_loop()
    # chats = loop.run_until_complete(get_chats_in_db())
    # loop.close()
    chats = get_chats_in_db()
    print(chats)
    for chat_in_db in chats:
        print(chat_in_db)
        scheduler_menu.add_job(
            send_notification_menu,
            trigger="cron",
            day_of_week="mon-fri",
            hour=chat_in_db[1][:2],
            minute=chat_in_db[1][-2:],
            kwargs={"chat_id": chat_in_db[0], "bot": bot},
        )
    logging.debug(scheduler_menu.get_jobs())
