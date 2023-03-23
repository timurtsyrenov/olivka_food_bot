from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

# Инициализируем переменную bot (token = 'токен взятый у бота BotFather')
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# Создаем диспетчер простых сообщений. Он будет обрабатывать входящие сообщения.

dp = Dispatcher(bot, storage=storage)

__all__ = ['bot', 'storage', 'dp']