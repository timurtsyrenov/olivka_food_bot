from aiogram import types


# Объявляем команды у бота
async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", "Получить меню"),
            types.BotCommand("today", "Получить меню на сегодня"),
            types.BotCommand("on_notification", "Включить рассылку меню"),
            types.BotCommand("off_notification", "Выключить рассылку меню"),
        ]
    )
