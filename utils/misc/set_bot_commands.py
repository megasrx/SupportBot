from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni yuklash"),
            types.BotCommand("support", "Qo'llab-quvvatlash xizmatiga yozish"),
            types.BotCommand("support_call", "Qo'llab-quvvatlash xizmati bilan bog'lanish"),
            types.BotCommand("help", "Yordam olish"),
        ]
    )
