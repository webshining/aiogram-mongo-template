import asyncio

from beanie import init_beanie

from app import setup_routes, setup_middlewares, set_default_commands
from database.base import database
from database.models import User
from loader import dp, bot
from utils import logger


async def on_startup() -> None:
    await set_default_commands()
    logger.info("Bot started!")


async def on_shutdown() -> None:
    logger.info("Bot stopped!")


async def main() -> None:
    await init_beanie(database=database, document_models=[User])
    await setup_middlewares(dp)
    await setup_routes(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
