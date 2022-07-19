from aiogram.dispatcher.filters import BoundFilter
from utils.db_api.database import Admin
from aiogram import types

admin_db = Admin()

class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user_id = message.from_user.id
        result = admin_db.chek_admin(user_id)
        if result != []:
            return True
        else:
            return False