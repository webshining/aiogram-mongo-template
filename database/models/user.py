from pydantic import Field

from .base import Base


class User(Base):
    id: int = Field(default_factory=int, alias="_id")
    name: str
    username: str | None = Field(default=None)
    lang: str

    @classmethod
    async def get_or_create(cls, id: int, name: str, username: str | None, lang: str):
        user = await cls.get(id)
        user = (
            await cls.update(user.id, name=name, username=username)
            if user
            else await cls.create(_id=id, name=name, username=username, lang=lang)
        )
        return user


User.set_collection("users")
