import urllib.parse
from environs import Env
from pathlib import Path

env = Env()
env.read_env()


DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN", None)

MONGO_HOST = env.str("MONGO_HOST", "localhost")
MONGO_PORT = env.int("MONGO_PORT", 27017)
MONGO_USER = env.str("MONGO_USER", None)
MONGO_PASS = env.str("MONGO_PASS", None)
MONGO_NAME = env.str("MONGO_NAME", "bot")

MONGO_URL = env.str("MONGO_URL", f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
if MONGO_USER and MONGO_PASS:
    MONGO_URL = f"mongodb://{urllib.parse.quote(MONGO_USER)}:{urllib.parse.quote(MONGO_PASS)}@{MONGO_HOST}:{MONGO_PORT}/"

RD_DB = env.int("RD_DB", None)
RD_HOST = env.str("RD_HOST", None)
RD_PORT = env.int("RD_PORT", None)
RD_USER = env.str("RD_USER", None)
RD_PASS = env.str("RD_PASS", None)

I18N_DOMAIN = "bot"
I18N_PATH = f"{DIR}/data/locales"
