
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message

from loader import _


class StatusFilter(Filter):
    def __init__(self, super: bool = False):
        self.super = super

    async def __call__(self, update: any, **data) -> bool:
        user = data['user']
        _is = user.is_admin(self.super)
        if not _is:
            if isinstance(update, Message) or isinstance(update, CallbackQuery):
                await update.answer(_("Not enough rights🚫"))
        return _is
