from aiogram import types


# Здесь объявляем команды


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("get_menu", "Получить меню"),
        ]
    )
