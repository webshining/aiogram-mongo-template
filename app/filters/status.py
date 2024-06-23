from aiogram.filters import Filter

from loader import _


class StatusFilter(Filter):
    def __init__(self, status: list[str] = []):
        self.status = status

    async def __call__(self, update: any, **data) -> bool:
        user = data["user"]
        _is = user.status in self.status
        return _is
