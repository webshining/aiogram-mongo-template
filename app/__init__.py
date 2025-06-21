from aiogram import Dispatcher

from .commands import set_default_commands
from .handlers import routers
from .middlewares import setup_middlewares


async def setup_routes(dp: Dispatcher):
    dp.include_routers(*routers)


__all__ = ["setup_routes", "setup_middlewares"]
