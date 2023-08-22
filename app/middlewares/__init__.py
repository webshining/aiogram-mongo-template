from aiogram import Dispatcher

from .inter import i18n
from .user import UserMiddleware


def setup_middleware(dp: Dispatcher):
    dp.setup_middleware(UserMiddleware())
    dp.setup_middleware(i18n)