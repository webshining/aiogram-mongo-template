from aiogram.filters import Filter
from aiogram.types import Update

from loader import _


class AdminFilter(Filter):
    def __init__(self, super: bool = False):
        self.super = super

    async def __call__(self, update: Update, **data) -> bool:
        user = data['user']
        _is = user.is_admin(self.super)
        if not _is:
            if hasattr(update, "message"):
                await update.answer(_("Not enough rights🚫"))
        return _is
