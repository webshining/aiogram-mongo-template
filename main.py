import asyncio

from aiogram import Dispatcher
from aiogram.types import BotCommandScopeDefault

import app.commands
import app.handlers
import app.middlewares
from app.middlewares.inter import i18n
from loader import bot, storage


async def on_startup() -> None:
    await app.commands.set_default_commands()
    print("Bot started!")
    
async def on_shutdown() -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=BotCommandScopeDefault(), language_code=lang)
    print("Bot stoped!")

async def main() -> None:
    dp = Dispatcher(storage=storage)
    app.middlewares.setup_middlewares(dp)
    app.handlers.setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())