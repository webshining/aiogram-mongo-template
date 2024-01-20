from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')

MONGO_URL = env.str('MONGO_URL', None)

RD_DB = env.int('RD_DB', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)

RD_URI = env.str('RD_URI', default=None)
if RD_DB and RD_HOST and RD_PORT:
    DB_URI = f'redis://{RD_HOST}:{RD_PORT}/{RD_DB}'

I18N_PATH = f'{DIR}/data/locales'
I18N_DOMAIN = env.str('I18N_DOMAIN', 'bot')
