from aiogram import Router

from .users import routers as user_routers

dp = Router()

for r in user_routers:
    dp.include_router(r)
