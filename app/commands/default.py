from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import bot, i18n, _

def get_default_commands(lang: str = 'en'):
    commands = [
        BotCommand('start', _('start chat', locale=lang))
    ]
    
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(lang), scope=BotCommandScopeDefault())