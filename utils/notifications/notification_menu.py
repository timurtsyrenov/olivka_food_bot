from aiogram import Bot
from data.notification_config import CHAT_ID
from utils import get_menu, get_today_int, logger


async def send_notification_menu(bot: Bot):
    """
    Асинхронная функция, которая отправляет меню на сегодня. Используется в рассылке по расписанию
    :param bot: переменная бота
    """
    number_today = get_today_int()
    # Проверка на субботу и воскресенье, в субботу и воскресенье рассылки не будет даже если рассылка будет включена
    # на выходные
    if number_today not in [6, 7]:
        # Получаем изображение с меню в виде потока байтов
        photo_bytes = get_menu(number_today)
        # Посылаем изображение в чаты указанные в переменной CHAT_ID
        logger.info("Отправка меню по расписанию")
        for chat_id in CHAT_ID:
            await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
