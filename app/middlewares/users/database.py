from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import CallbackQuery, InlineQuery, Message

from database.base import client


async def database_middleware(event: TelegramEventObserver):
    @event.middleware()
    async def process(handler, event: Message | CallbackQuery | InlineQuery, data):
        async with client.start_session() as session:
            data['session'] = session
            await handler(event, data)
