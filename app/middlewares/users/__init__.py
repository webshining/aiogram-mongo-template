from .database import database_middleware
from .inter import i18n_middleware
from .user import user_middleware

middlewares = [database_middleware, user_middleware, i18n_middleware]

__all__ = ["middlewares"]
