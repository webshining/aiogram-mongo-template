from aiogram import executor

import app.filters
import app.handlers
import app.middlewares
from app.commands import set_default_commands
from loader import dp


async def on_startup(dispatcher):
    await set_default_commands()
    app.middlewares.setup_middleware(dp)
    print("Bot started!")
    

async def on_shutdown(dispatcher):
    print("Bot stoped!")


if __name__ == '__main__':
    executor.start_polling(app.handlers.dp, on_startup=on_startup, on_shutdown=on_shutdown)
