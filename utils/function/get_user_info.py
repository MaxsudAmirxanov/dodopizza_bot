from pyrogram import Client
import asyncio
from pyrogram.errors import UsernameNotOccupied, UsernameInvalid
async def get_user_info(id):
    try:
        async with Client("my_account", 9562538, "9b43be1a2058bcbc3108068ac992670a") as app:
            return await app.get_users(id)
            # print(app.get_me()
    except UsernameNotOccupied:
        return False
    except UsernameInvalid:
        return False

# print(asyncio.run(get_user_info(input())))   