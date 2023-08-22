from typing import Any, Tuple

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import User

from data.config import I18N_DOMAIN, I18N_PATH
from database.services import get_user


class MyI18nMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str | None:
        user = User.get_current()
        user = get_user(user.id)
        return user.lang


i18n = MyI18nMiddleware(I18N_DOMAIN, I18N_PATH)
