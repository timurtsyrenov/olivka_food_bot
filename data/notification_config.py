import os

from dotenv import load_dotenv

load_dotenv()

# Переменная хранящая chat id чатов, для рассылки
CHAT_ID = [int(id) for id in os.getenv(key="CHAT_ID").split(",")]

# В дальнейшем нужно стягивать эти переменные из базы данных
CUSTOM_TIME = 11
