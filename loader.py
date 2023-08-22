from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from pymongo import MongoClient

from data.config import (MONGODB_URL, RD_DB, RD_HOST, RD_PASS, RD_PORT,
                         TELEGRAM_BOT_TOKEN)

bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
if RD_DB and RD_HOST and RD_PORT:
    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
else:
    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

client = MongoClient(MONGODB_URL)
db = client['bot']

from app.middlewares.inter import i18n

_ = i18n.gettext
