from aiogram import Bot, Dispatcher, types
from motor.motor_tornado import MotorClient

from data.config import (
    MONGO_URL,
    MONGO_NAME,
    RD_DB,
    RD_HOST,
    RD_PASS,
    RD_PORT,
    RD_USER,
    TELEGRAM_BOT_TOKEN,
)

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)

if RD_PORT and RD_HOST and RD_DB:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2

    storage = RedisStorage2(
        host=RD_HOST, port=RD_PORT, db=RD_DB, password=RD_PASS, username=RD_USER
    )
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

    storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

client = MotorClient(MONGO_URL)
db = client[MONGO_NAME]

from app.middlewares.inter import i18n

_ = i18n.gettext
