from aiogram import Dispatcher

from .admins import *
from .users import *


def setup_handlers(dp :Dispatcher) -> None:
    dp.include_routers(lang_router, start_router)
