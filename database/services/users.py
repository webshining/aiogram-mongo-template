from ..models import User, users_collection


def get_users():
    users = users_collection.find()
    return [User(**u) for u in users]


def get_user(id: int):
    user = users_collection.find_one({'_id': id})
    return User(**user) if user else None


def create_user(id: int, name: str, username: str, language: str):
    user = users_collection.insert_one({'_id': id, 'name': name, 'username': username, 'language': language})
    return get_user(user.inserted_id)


def update_user(id: int, name: str, username: str):
    user = users_collection.find_one_and_update({'_id': id}, {'$set': {'name': name, 'username': username}}, return_document=True)
    return User(**user)


def get_or_create_user(id: int, name: str, username: str, language: str):
    user = get_user(id)
    if user:
        user = update_user(id, name, username)
    else:
        user = create_user(id, name, username, language)
    return user


def edit_user_language(id: int, language: str):
    user = users_collection.find_one_and_update({'_id': id}, {'$set': {'language': language}}, return_document=True)
    return User(**user)
