from aiogram import Bot
from utils import logger
import emoji

async def send_prekol(chat_id, bot: Bot):
    """
    Асинхронная функция, которая отправляет оповещение что Данильчик еще на месте.
    :param chat_id:
    :param bot: переменная бота
    """
    # Посылаем изображение в чаты указанные в переменной CHAT_ID
    logger.info("Прекол отправлен")
    await bot.send_message(text="Данильчик еще не уволился" + emoji.emojize(" 🐸"), chat_id=chat_id)
