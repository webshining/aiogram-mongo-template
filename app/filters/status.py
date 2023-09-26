from aiogram.filters import Filter
from aiogram.types import Message

from app.commands import remove_admins_commands
from loader import _


class StatusFilter(Filter):
    def __init__(self, status: str) -> None:
        if status == 'admin':
            self.statuses = ['admin', 'super_admin']
        else:
            self.statuses = ['super_admin']

    async def __call__(self, message: Message, **data: dict) -> bool:
        user = data['user']
        _is = user.status in self.statuses
        if not _is:
            await remove_admins_commands(user.id)
            await message.answer(_("Not enough rights🚫"))
        return _is
