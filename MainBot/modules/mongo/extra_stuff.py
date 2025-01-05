import threading
from MainBot.modules.mongo import db

USERS_COLLECTION = db["extra_stuff"]
INSERTION_LOCK = threading.RLock()


async def get_all_higher_users():
    ret = set([])
    admins = await USERS_COLLECTION.find_one({"name": "admins"})
    if admins:
        for el in admins["users"]:
            ret.add(el)
    return ret


async def add_admin(user_id):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"name": "admins"})
        if curr:
            curr["users"][user_id] = True
            await USERS_COLLECTION.update_one({"name": "admins"}, {"$set": curr})
            return True
        else:
            document = {"name": "admins", "users": {user_id: True}}
            await USERS_COLLECTION.insert_one(document)
            return True


async def remove_admin(user_id):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"name": "admins"})
        if curr:
            if user_id in curr["users"]:
                del curr["users"][user_id]
                await USERS_COLLECTION.update_one({"name": "admins"}, {"$set": curr})
                return True
        return False


async def get_all_valid_chats():
    ret = set([])
    valid_chats = await USERS_COLLECTION.find_one({"name": "validChats"})
    if valid_chats:
        for el in valid_chats["chats"]:
            ret.add(el)
    return ret


async def add_valid_chat(chat_id):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"name": "validChats"})
        if curr:
            curr["chats"][chat_id] = True
            await USERS_COLLECTION.update_one({"name": "validChats"}, {"$set": curr})
        else:
            document = {"name": "validChats", "chats": {chat_id: True}}
            await USERS_COLLECTION.insert_one(document)
        return True


async def remove_valid_chat(chat_id):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"name": "validChats"})
        if curr:
            if chat_id in curr["chats"]:
                del curr["chats"][chat_id]
                await USERS_COLLECTION.update_one(
                    {"name": "validChats"}, {"$set": curr}
                )
                return True
        return False
