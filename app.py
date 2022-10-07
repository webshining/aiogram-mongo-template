from aiogram import executor, types

from loader import dp, bot, i18n
from utils import logger


async def on_startup(dispatcher):
    logger.info('Bot started!')
    from app.commands import set_default_commands
    await set_default_commands()


async def on_shutdown(dispatcher):
    logger.error('Bot shutting down!')
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=types.BotCommandScopeDefault(), language_code=lang)


if __name__ == '__main__':
    import app.filters, app.middlewares, app.handlers
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
