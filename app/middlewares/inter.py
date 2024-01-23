from aiogram.types import Update
from aiogram.utils.i18n import I18nMiddleware

from loader import i18n


class MyI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: Update, data: dict) -> str:
        user = data['user']
        return user.lang if user else await super().get_locale(event, data)


i18n_middleware = MyI18nMiddleware(i18n)
