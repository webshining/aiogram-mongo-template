from aiogram.types import BotCommandScopeChat

from loader import bot, i18n
from .admins import set_admins_commands
from .default import set_default_commands


async def remove_admins_commands(id: int):
    await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=id))
    for lang in i18n.available_locales:
        await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=id), language_code=lang)
