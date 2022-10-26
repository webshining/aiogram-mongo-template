from app.commands.default import set_default_commands
from loader import dp, bot


async def on_startup():
    from app.commands import set_default_commands
    await set_default_commands()
    print("Bot started!")


if __name__ == '__main__':
    import app.handlers
    dp.startup.register(set_default_commands())
    dp.run_polling(bot)