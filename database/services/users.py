from ..models import User, users_collection


async def get_users() -> list[User]:
    users = users_collection.find()
    return [User(**u) async for u in users]


async def get_user(id: int) -> User or None:
    user = await users_collection.find_one({'id': id})
    return User(**user) if user else None


async def create_user(id: int, **kwargs) -> User:
    kwargs['status'] = 'user'
    user = await users_collection.insert_one({'id': id, **kwargs})
    return await get_user(user.inserted_id)


async def update_user(id: int, **kwargs) -> User:
    user = await users_collection.find_one_and_update({'id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)


async def get_or_create_user(id: int, **kwargs) -> User:
    user = await get_user(id)
    if user: kwargs['lang'] = user.lang
    user = await update_user(id, **kwargs) if user else await create_user(id, **kwargs)
    return user
