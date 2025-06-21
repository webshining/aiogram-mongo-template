from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import CallbackQuery, InlineQuery, Message

from database.models import User


async def user_middleware(event: TelegramEventObserver):
    @event.middleware()
    async def process(handler, event: Message | CallbackQuery | InlineQuery, data):
        await process_user(event.from_user, data)
        await handler(event, data)

    async def process_user(from_user, data):
        data["user"] = await User.get_or_create(
            from_user.id, name=from_user.full_name, username=from_user.username, lang=from_user.language_code
        )
