import motor.motor_asyncio
from config import DB_NAME, DB_URI

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            session = None,
        )

def already_db(user_id):
    user = users.find_one({"user_id": str(user_id)})
    return bool(user)

def already_dbg(chat_id):
    group = groups.find_one({"chat_id": str(chat_id)})
    return bool(group)

def add_user(user_id, name):
    if already_db(user_id):
        return
    users.insert_one({"user_id": str(user_id), "name": name, "ban_status": {"is_banned": False}})

def remove_user(user_id):
    if not already_db(user_id):
        return
    users.delete_one({"user_id": str(user_id)})

def add_group(chat_id):
    if already_dbg(chat_id):
        return
    groups.insert_one({"chat_id": str(chat_id)})

def all_users():
    return users.count_documents({})

def all_groups():
    return groups.count_documents({})

def get_all_users():
    return list(users.find({}, {"user_id": 1, "name": 1, "_id": 0}))
    
def add_user(user_id, name):
    if already_db(user_id):
        users.update_one({"user_id": str(user_id)}, {"$set": {"name": name}})
        return
    users.insert_one({"user_id": str(user_id), "name": name, "ban_status": {"is_banned": False}})
    
def already_db(user_id):
    """Checks if the user is already in the MongoDB database"""
    return users.find_one({"user_id": str(user_id)}) is not None
        
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_session(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_session(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('session')

db = Database(DB_URI, DB_NAME)
