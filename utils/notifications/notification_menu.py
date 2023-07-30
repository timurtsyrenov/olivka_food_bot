from aiogram import Bot
from utils import get_menu, get_today_int, logger


async def send_notification_menu(chat_id, bot: Bot):
    """
    Асинхронная функция, которая отправляет меню на сегодня. Используется в рассылке по расписанию
    :param chat_id:
    :param bot: переменная бота
    """
    number_today = get_today_int()
    # Получаем изображение с меню в виде потока байтов
    photo_bytes = get_menu(number_today)
    # Посылаем изображение в чаты указанные в переменной CHAT_ID
    logger.info("Отправка меню по расписанию")
    await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
