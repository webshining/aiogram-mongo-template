from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
from database import get_or_create_user
from utils import logger


class UserMiddleware(BaseMiddleware):
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        from_user = message.from_user
        
        logger.debug

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)

    @staticmethod
    async def on_callback_query(call: CallbackQuery, data: dict):
        from_user = call.from_user

        data['user'] = get_or_create_user(from_user.id, from_user.full_name, from_user.username)
