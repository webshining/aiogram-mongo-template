from typing import Any, Tuple

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import User

from data.config import I18N_DOMAIN, I18N_PATH
from database.models import User


class MyI18nMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str | None:
        *_, data = args
        user = data["user"]
        return user.lang

    def set_user_locale(self, locale: str):
        self.ctx_locale.set(locale)

    async def trigger(self, action, args):
        if "update" not in action and "error" not in action and action.startswith("process"):
            locale = await self.get_user_locale(action, args)
            self.set_user_locale(locale)
            return True


i18n = MyI18nMiddleware(I18N_DOMAIN, I18N_PATH)
