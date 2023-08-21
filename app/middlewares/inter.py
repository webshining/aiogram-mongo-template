from typing import Any, Dict

from aiogram.types import Update
from aiogram.utils.i18n import I18nMiddleware

from database.services import get_user
from loader import i18n


class MyI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: Update, data: Dict[str, Any]) -> str:
        if event.message:
            from_user = event.message.from_user
        if event.callback_query:
            from_user = event.callback_query.from_user
        if event.inline_query:
            from_user = event.inline_query.from_user
        user = await get_user(from_user.id)
        return user.lang if user else await super().get_locale(event, data)

i18n_middleware = MyI18nMiddleware(i18n)