from email import message
from os import stat
from secrets import choice
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_main_admin import IsMainAdmin
from utils.db_api.database import Admin, MainAdmin
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from aiogram.types import InputFile
from aiogram.types.input_media import InputMediaPhoto
import asyncio
from .show_admin import show_admin

main_admin_db = MainAdmin()

from loader import bot
from loader import dp

class DeleteAdmin(StatesGroup):
    admin_id = State()
    choice = State()

@dp.message_handler(IsMainAdmin(), text='/delete_admin')
async def admin_start(message: types.Message):
    # await message.answer('Удаляя админа, вы решаете доступ ко всем админским коммандам, для того чтобы узнвть какие есть комманды ведике комманду /show_admin_commands'
    # )
    # asyncio.sleep(6)

    await message.answer('Введите Телеграм ID этого админа, чтобы узнать  Телеграм ID админа введите комманду /show_admin')
    await DeleteAdmin.admin_id.set()

@dp.message_handler(IsMainAdmin(), state=DeleteAdmin.admin_id)
async def admin(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '/show_admin':
        await show_admin(message=message)
        await admin_start(message=message)
        # await state.finish()
        # await DeleteAdmin.admin_id.set()

    async with state.proxy() as data:
        data['admin_id'] = answer

        

    admin = main_admin_db.get_admin_name(answer)
    
    await message.answer(f'Вы точно хотите удалить админа {admin[0][0]} {admin[0][1]} ?\n(Да/Нет)')
    
    await DeleteAdmin.choice.set()


@dp.message_handler(IsMainAdmin(), state=DeleteAdmin.choice)
async def admin(message: types.Message, state: FSMContext):

    data = await state.get_data()

    answer = message.text
    if answer.lower() == 'да':
        'Удаление Админа'
        await message.answer(f'Удаление админа {data["admin_id"]}')
        main_admin_db.delete_admin(data["admin_id"])
        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена удаление')
        await state.finish()


