from pydantic import BaseModel
from loader import db

class User(BaseModel):
    id: int
    name: str
    username: str

users_collection = db["users"]