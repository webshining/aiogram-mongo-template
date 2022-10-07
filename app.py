from aiogram import executor, types

from loader import dp, bot, i18n
from utils import logger


async def on_startup(dispatcher):
    logger.info('Bot started!')
    from app.commands import set_default_commands
    await set_default_commands()


async def on_shutdown(dispatcher):
    from database.services import get_users
    await bot.delete_my_commands()
    [await bot.delete_my_commands(scope=types.BotCommandScopeChat(user.id)) for user in get_users()]
    [await bot.delete_my_commands(language_code=lang) for lang in i18n.available_locales]
    await dp.storage.close()
    await dp.storage.wait_closed()
    logger.error('Bot shutting down!')


if __name__ == '__main__':
    import app.filters, app.handlers, app.middlewares
    app.middlewares.setup_middlewares(dp)
    executor.start_polling(app.handlers.dp, on_startup=on_startup, on_shutdown=on_shutdown)
