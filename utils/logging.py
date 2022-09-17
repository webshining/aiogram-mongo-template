from loguru import logger
from data.config import DIR

logger.add(f'{DIR}/data/logs/log.out', format='[{level}]-[{time}]-[{message}]', level='DEBUG', rotation='1 day')
