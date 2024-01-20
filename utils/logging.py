from loguru import logger

from data.config import DIR

logger.add(f'{DIR}/logs/app.log', format='[{time}] [{level}] [{file.name}:{line}]  {message}',
           level='DEBUG', compression='zip')
