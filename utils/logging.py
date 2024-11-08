import logging

from loguru import logger

from data.config import DIR

logger.add(
    f"{DIR}/logs/app.log",
    format="[{time}] [{level}] [{file.name}:{line}]  {message}",
    level="DEBUG",
    compression="zip",
)


def setup_logger(name: str) -> None:
    class CustomFilter(logging.Filter):
        def filter(self, record):
            return "Failed to fetch updates" not in record.getMessage()

    log = logging.getLogger(name)
    log.addFilter(CustomFilter())
    log.setLevel(logging.ERROR)


setup_logger("aiogram")
setup_logger("aiogram.dispatcher")
