from aiogram.types import Message, CallbackQuery, InlineQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
from database import get_or_create_user
from utils import logger


class UserMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        from_user = message.from_user
        
        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username, from_user.language_code)

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        user = callback_query.from_user

        data['user'] = get_or_create_user(user.id, user.full_name, user.username, user.language_code)
        

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        from_user = inline_query.from_user

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username, from_user.language_code)
