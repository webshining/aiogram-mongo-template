from pydantic import BaseModel, Field

from loader import db


class User(BaseModel):
    id: int = Field(default_factory=int, alias='_id')
    name: str
    username: str
    language: str


users_collection = db['users']
