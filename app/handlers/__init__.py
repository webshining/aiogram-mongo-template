from aiogram import Dispatcher

import app.handlers.error

from .admins import router as admin_router
from .users import router as user_router


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_routers(user_router, admin_router)
