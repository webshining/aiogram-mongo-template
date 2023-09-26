from aiogram import Dispatcher

from app.routers import admin_router
from .admin import AdminMiddleware
from .inter import i18n_middleware
from .user import UserMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(i18n_middleware)
    dp.update.middleware(UserMiddleware())
    admin_router.message.middleware(AdminMiddleware())
