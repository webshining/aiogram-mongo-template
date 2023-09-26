from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.commands import set_admins_commands


class AdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        user = data['user']
        if user.status in ('admin', 'super_admin'):
            await set_admins_commands(user.id)
        return await handler(event, data)
