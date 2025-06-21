from .status import status_middleware

middlewares = [status_middleware]

__all__ = ["middlewares"]
