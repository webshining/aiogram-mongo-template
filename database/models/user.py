from pydantic import BaseModel

from loader import db


class User(BaseModel):
    id: int
    name: str
    username: str
    lang: str
    status: str


users_collection = db["users"]
