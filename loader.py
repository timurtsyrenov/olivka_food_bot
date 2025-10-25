from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from data import config

# Инициализируем бота
bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

# Хранилище для FSM
storage = MemoryStorage()

# Создаём диспетчер (без bot)
dp = Dispatcher(storage=storage)

__all__ = ["bot", "storage", "dp"]
