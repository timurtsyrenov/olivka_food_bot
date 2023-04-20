from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loader import bot
from utils.notifications.notification_menu import send_notification_menu
from data.notification_config import CUSTOM_TIME

# Инициализируем переменную для рассылки меню по расписанию
scheduler_menu = AsyncIOScheduler(timezone="Asia/Novosibirsk")
scheduler_menu.add_job(
    send_notification_menu,
    trigger="cron",
    day_of_week="mon-fri",
    hour=CUSTOM_TIME,
    minute=00,
    kwargs={"bot": bot},
)
