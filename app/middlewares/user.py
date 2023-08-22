from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery, InlineQuery, Message

from database.services import get_or_create_user


class UserMiddleware(BaseMiddleware):    
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        from_user = message.from_user
        
        data['user'] = get_or_create_user(from_user.id, name=from_user.full_name, username=from_user.username, lang=from_user.language_code)

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        from_user = callback_query.from_user

        data['user'] = get_or_create_user(from_user.id, name=from_user.full_name, username=from_user.username, lang=from_user.language_code)
        

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        from_user = inline_query.from_user

        data['user'] = get_or_create_user(from_user.id, name=from_user.full_name, username=from_user.username, lang=from_user.language_code)