from aiogram import Dispatcher

from app.routers import admin_router

from .status import StatusFilter


def setup_filters(dp: Dispatcher):
    admin_status = ["admin", "super_admin"]
    admin_router.callback_query.filter(StatusFilter(admin_status))
    admin_router.message.filter(StatusFilter(admin_status))
    admin_router.inline_query.filter(StatusFilter(admin_status))
