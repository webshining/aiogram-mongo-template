from aiogram.types import Message, CallbackQuery, InlineQuery
from aiogram.dispatcher.middlewares import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):    
    @staticmethod
    async def on_process_message(message: Message, data: dict):
        pass

    @staticmethod
    async def on_process_callback_query(callback_query: CallbackQuery, data: dict[str]):
        pass
        

    @staticmethod
    async def on_process_inline_query(inline_query: InlineQuery, data: dict[str]):
        pass