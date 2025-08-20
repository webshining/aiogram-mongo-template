from enum import StrEnum

from beanie import Document


class Status(StrEnum):
    USER = "user"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"
    BANNED = "banned"


class User(Document):
    id: int
    name: str
    username: str | None = None
    status: str = Status.USER
    lang: str = "en"

    def is_admin(self, super: bool = False) -> bool:
        if super:
            return self.status == Status.SUPER_ADMIN
        return self.status in (Status.ADMIN, Status.SUPER_ADMIN)

    class Settings:
        name = "users"
