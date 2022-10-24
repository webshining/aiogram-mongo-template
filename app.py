from zoneinfo import available_timezones
from aiogram import executor, types

from loader import dp, bot, i18n
from utils import logger


async def on_startup(dispatcher):
    from app.commands import set_default_commands
    await set_default_commands()
    logger.info('Bot started!')


async def on_shutdown(dispatcher):
    from database.services import get_users
    await bot.delete_my_commands()
    [await bot.delete_my_commands(language_code=lang) for lang in i18n.available_locales]
    [await bot.delete_my_commands(scope=types.BotCommandScopeChat(user.id)) for user in get_users()]
    logger.error('Bot shutting down!')


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(app.handlers.dp, on_startup=on_startup, on_shutdown=on_shutdown)
