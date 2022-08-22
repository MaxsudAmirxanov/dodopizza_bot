from email import message
from os import stat
from secrets import choice
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_main_admin import IsMainAdmin
from utils.db_api.database import Admin, MainAdmin, Customer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from aiogram.types import InputFile
from aiogram.types.input_media import InputMediaPhoto
from utils.function import get_user_info
import asyncio
from .admin import admin_command

main_admin_db = MainAdmin()
customer_db = Customer()

from loader import bot
from loader import dp

class AddAdmin(StatesGroup):
    telegram_id = State()
    choice = State()

@dp.message_handler(IsMainAdmin(), text='/add_admin')
async def admin_start(message: types.Message):
    await message.answer('Добавляя админа, вы даете доступ ко всем админским коммандам, для того чтобы узнать какие есть комманды ведите комманду /admin'
    )
    await asyncio.sleep(4)

    await message.answer('Введите @username пользователя')
    await AddAdmin.telegram_id.set()

@dp.message_handler(IsMainAdmin(), state=AddAdmin.telegram_id)
async def admin(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '/admin':
        await admin_command(message=message)
        await admin_start(message=message)
    global user_info
    user_info = await get_user_info.get_user_info(answer)
    if user_info == False:
        await message.answer('Такого пользователя не существует')
        await state.finish()
    else:
    
        await message.answer(f'Вы точно хотите добавить {user_info.first_name} {user_info.last_name} в администраторы?\n(Да/Нет)'
        )
        await AddAdmin.choice.set()


@dp.message_handler(IsMainAdmin(), state=AddAdmin.choice)
async def admin(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == 'да':
        'Добавление Админа'
        customer_id = customer_db.find_customer_id(user_info.id)
        if customer_id == []:
            await message.answer(f'Пользователь {user_info.first_name} {user_info.last_name} не запускал этого бота, для того чтобы сделать его админом, нужно чтобы пользователь его запустил.')
        print(user_info)
        main_admin_id = main_admin_db.find_main_admin_id(message.from_user.id)
        print(main_admin_id)
        result = main_admin_db.add_admin( user_name=user_info.username, user_telegram_id=user_info.id, customer_id=customer_id[0][0], main_admin_id=main_admin_id[0][0] )
        if result == False:
            await message.answer('Такой админ уже существует')
            await state.finish()
        else:
            await message.answer('Добавление админа')
            await state.finish()
        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена добавление')
        await state.finish()



