import asyncio

from app.commands import set_default_commands
from app.handlers import setup_handlers
from app.middlewares import setup_middlewares
from loader import bot, dp
from utils import logger


async def on_startup() -> None:
    await set_default_commands()
    logger.info("Bot started!")


async def on_shutdown() -> None:
    logger.info("Bot stopped!")


async def main() -> None:
    setup_middlewares(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
