import sys

from loguru import logger
from data.config import LOG_LEVEL

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
