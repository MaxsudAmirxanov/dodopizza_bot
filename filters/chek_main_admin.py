from aiogram.dispatcher.filters import BoundFilter
from utils.db_api.database import MainAdmin
from aiogram import types

main_admin_db = MainAdmin()

class IsMainAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user_id = message.from_user.id
        result = main_admin_db.chek_main_admin(user_id)
        if result != []:
            return True
        else:
            return False