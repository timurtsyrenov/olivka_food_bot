import time
from typing import Any, Awaitable, Callable, Dict

import emoji
from aiogram import BaseMiddleware
from aiogram.types import Message


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float = 1.0):
        super().__init__()
        self.rate_limit = limit
        self.last_time: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        now = time.time()
        last = self.last_time.get(user_id, 0)
        delta = now - last

        # Если пользователь пишет слишком быстро — игнорируем
        if delta < self.rate_limit:
            await event.answer("Не так быстро, друг, дай подумоть " + emoji.emojize("🤔"))
            return
        else:
            self.last_time[user_id] = now
            return await handler(event, data)
