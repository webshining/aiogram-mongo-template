from aiogram.types import Message, CallbackQuery, InlineQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
from database import get_or_create_user
from utils import logger


class UserMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        from_user = message.from_user
        
        logger.debug()

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)

    async def on_callback_query(self, call: CallbackQuery, data: dict):
        from_user = call.from_user

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)
        

    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        from_user = inline_query.from_user

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)
