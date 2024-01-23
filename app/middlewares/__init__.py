from aiogram import Dispatcher

from .inter import i18n_middleware
from .user import UserMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(UserMiddleware())
    dp.update.middleware(i18n_middleware)
