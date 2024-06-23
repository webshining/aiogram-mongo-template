import asyncio

from app import (
    remove_commands,
    set_default_commands,
    setup_filters,
    setup_handlers,
    setup_middlewares,
)
from loader import bot, dp
from utils import logger


async def on_startup() -> None:
    await set_default_commands()
    logger.info("Bot started!")


async def on_shutdown() -> None:
    await remove_commands()
    logger.info("Bot stopped!")


async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    setup_middlewares(dp)
    setup_handlers(dp)
    setup_filters(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
