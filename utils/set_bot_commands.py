from aiogram import Bot, types


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Запустить бота"),
            types.BotCommand(command="today", description="Меню на сегодня"),
            types.BotCommand(command="on_notification", description="Включить рассылку меню"),
            types.BotCommand(command="off_notification", description="Выключить рассылку меню"),
        ]
    )
