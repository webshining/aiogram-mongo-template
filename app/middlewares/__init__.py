from aiogram import Dispatcher

from app.handlers import admin_router

from .admins import middlewares as admins_middlewares
from .users import middlewares as users_middlewares


async def setup_middlewares(dp: Dispatcher):
    for middleware in users_middlewares:
        await middleware(dp.message)
        await middleware(dp.callback_query)
        await middleware(dp.inline_query)
    for middleware in admins_middlewares:
        await middleware(admin_router.message)
        await middleware(admin_router.callback_query)
        await middleware(admin_router.inline_query)


__all__ = ["setup_middlewares"]
