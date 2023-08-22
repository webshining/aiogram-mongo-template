from ..models import User, users_collection


def get_users():
    users = users_collection.find()
    return [User(**u) for u in users]


def get_user(id: int):
    user = users_collection.find_one({'id': id})
    return User(**user) if user else None


def create_user(id: int, **kwargs):
    user = users_collection.insert_one({'id': id, **kwargs})
    return get_user(user.inserted_id)


def update_user(id: int, **kwargs):
    user = users_collection.find_one_and_update({'id': id}, {'$set': kwargs}, return_document=True)
    return User(**user)


def get_or_create_user(id: int, **kwargs):
    user = get_user(id)
    if user:
        del kwargs['lang']
        user = update_user(id, **kwargs)
    else:
        user = create_user(id, **kwargs)
    return user