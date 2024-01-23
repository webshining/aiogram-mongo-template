from aiogram import Dispatcher

import app.handlers.error
from app.filters import AdminFilter
from .admins import router as admin_router
from .users import router as user_router


def setup_handlers(dp: Dispatcher) -> None:
    admin_router.callback_query.filter(AdminFilter())
    dp.include_routers(user_router, admin_router)
