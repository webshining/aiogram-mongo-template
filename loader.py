from aiogram import Bot, Dispatcher, types
from pymongo import MongoClient

from data.config import RD_DB, RD_HOST, RD_PASS, RD_PORT, TELEGRAM_BOT_TOKEN, MONGODB_URL


bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
if RD_DB and RD_HOST and RD_PORT:
    from aiogram.contrib.fsm_storage.redis import RedisStorage2
    storage = RedisStorage2(RD_HOST, RD_PORT, RD_DB, RD_PASS)
else:
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

client = MongoClient(MONGODB_URL)
db = client['database']
