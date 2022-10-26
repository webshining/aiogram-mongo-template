from aiogram.types import BotCommandScopeDefault 
from loader import dp, bot, i18n


async def on_startup():
    from app.commands import set_default_commands
    await set_default_commands()
    print("Bot started!")
    
async def on_shutdown():
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=BotCommandScopeDefault(), language_code=lang)
    print("Bot stoped!")


if __name__ == '__main__':
    import app.handlers
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)