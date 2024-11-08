from aiogram import executor

from app.handlers import dp
from app.middlewares import setup_middleware
from app.commands import set_default_commands
from utils import logger


async def on_startup(dispatcher):
    await set_default_commands()
    setup_middleware(dp)
    logger.info("Bot started!")


async def on_shutdown(dispatcher):
    logger.info("Bot stopped!")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
