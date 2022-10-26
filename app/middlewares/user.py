from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject, Update
from database.services import get_or_create_user


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message:
            from_user = event.message.from_user
        if event.callback_query:
            from_user = event.callback_query
        if event.inline_query:
            from_user = event.inline_query
        user = await get_or_create_user(from_user.id, name=from_user.full_name, username=from_user.username, lang=from_user.language_code)
        data['user'] = user
        return await handler(event, data)