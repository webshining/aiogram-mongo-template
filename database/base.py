from pymongo import AsyncMongoClient

from data.config import MONGO_URL, MONGO_NAME

client = AsyncMongoClient(MONGO_URL)
database = client[MONGO_NAME]
