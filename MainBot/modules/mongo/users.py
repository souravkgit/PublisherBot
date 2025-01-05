import threading
from MainBot.modules.mongo import db

USERS_COLLECTION = db["users"]
INSERTION_LOCK = threading.RLock()


async def set_user(
    user_id, first=None, last=None, username=None, notification=True, chats={}
):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"user_id": user_id})
        if not curr:
            document = {
                "user_id": user_id,
                "first_name": first,
                "last_name": last,
                "user_name": username,
                "notification": notification,
                "chats": chats,
            }
            USERS_COLLECTION.insert_one(document)
            return True


async def add_user_chat(user_id, chat_id):
    with INSERTION_LOCK:
        curr = await USERS_COLLECTION.find_one({"user_id": user_id})
        if curr:
            curr["chats"][chat_id] = True
            await USERS_COLLECTION.update_one({"_id": curr["_id"]}, {"$set": curr})
            return True
        return False


async def get_user_chats(user_id):
    curr = await USERS_COLLECTION.find_one({"user_id": user_id})
    if curr:
        return curr["chats"]
    return {}


async def get_user(user_id):
    curr = await USERS_COLLECTION.find_one({"user_id": user_id})
    if not curr:
        return None
    else:
        return curr


async def get_username(user_id):
    curr = await USERS_COLLECTION.find_one({"user_id": user_id})
    if not curr:
        return None
    else:
        return curr["user_name"]


async def get_firstname(user_id):
    curr = await USERS_COLLECTION.find_one({"user_id": user_id})
    if not curr:
        return None
    else:
        return curr["first_name"]


async def get_lastname(user_id):
    curr = await USERS_COLLECTION.find_one({"user_id": user_id})
    if not curr:
        return None
    else:
        return curr["last_name"]


async def get_userid(user_name):
    curr = await USERS_COLLECTION.find_one({"user_name": user_name})
    if not curr:
        return None
    else:
        return curr["user_id"]


async def get_all_users():
    ALL_USERS_LIST = {}
    async for user in USERS_COLLECTION.find({}):
        ALL_USERS_LIST[user["user_id"]] = user
    return ALL_USERS_LIST


async def get_all_users_count():
    count = 0
    async for user in USERS_COLLECTION.find():
        count += 1
    return count


async def broadcasttag(context, msg_id, chat_id):
    all_users = await get_all_users()
    users_done = 0
    users_fail = 0
    for el in all_users:
        try:
            await context.bot.forward_message(
                int(el),
                chat_id,
                msg_id,
            )
            users_done += 1
        except Exception as e:
            users_fail += 1
            pass
    return f"Broadcast Done!\n\nUsers Done : {users_done}\nUsers Failed : {users_fail}"


async def broadcast(context, msg_, chat_id):
    all_users = await get_all_users()
    users_done = 0
    users_fail = 0
    for el in all_users:
        try:
            await msg_.copy(int(el))
            users_done += 1
        except Exception as e:
            print(e)
            users_fail += 1
            pass
    return f"Broadcast Done!\n\nUsers Done : {users_done}\nUsers Failed : {users_fail}"
