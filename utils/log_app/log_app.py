import sys

from data.config import LOG_LEVEL
from loguru import logger

if not LOG_LEVEL:
    LOG_LEVEL = "DEBUG"

# Конфигурация логов вывод в консоль stdout и в файл server.log
config = {
    "handlers": [
        {"sink": sys.stdout, "level": LOG_LEVEL},
        {
            "sink": "server.log",
            "level": LOG_LEVEL,
            "backtrace": True,
            "diagnose": True,
            "rotation": "1 week",
            "compression": "gz",
            "serialize": True,
        },
    ]
}

logger.configure(**config)
