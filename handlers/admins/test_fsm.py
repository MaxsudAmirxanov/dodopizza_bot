from os import stat
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Product, Cart, Customer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from aiogram.types import InputFile
from aiogram.types.input_media import InputMediaPhoto

from loader import dp, bot

class TestFSM(StatesGroup):
    # category_name = State()
    # cstegory_code = State()
    # subcategory_name = State()
    # subcatgory_code = State()
    andname = State()
    name = State()
    last_name = State()
    phone = State()

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Назад')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

# @dp.callback_query_handler(lambda c: c.data == 'назад')
# async def mailing(callback_query: types.CallbackQuery, state: FSMContext):
#         print('yfpfffl')
#         cur_state = await dp.current_state()
#         await TestFSM.previous()

inline_btn_1 = InlineKeyboardButton('Назад', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

@dp.callback_query_handler(lambda c: c.data == 'button1', state='*')
async def process_callback_button1(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    
    # cur_state = dp.current_state()
    # st = await cur_state.get_state()
    # if st == 'TestFSM:last_name':
    #     await state.finish()
    #     await TestFSM.name.set()
    # if st == 'TestFSM:phone':
    #     await state.finish()
    #     await TestFSM.last_name.set()

    # print(await cur_state.get_data())
    # print(await cur_state.())

    # await callback_query.message.answer(f'Сработало {cur_state}')
    # await state.finish()
    await state.reset_state()
    await TestFSM.unnext()
    
    # await TestFSM.next()
    await callback_query.message.answer('Назад')
    # await TestFSM.previous()
    await callback_query.message.answer(f'Сработало ')
# @dp.callback_query_handler(text='mailing')
@dp.message_handler(state=TestFSM.andname)
@dp.message_handler(text='test')
async def mailing(message: types.Message):

        await message.answer('Ведите имя', reply_markup=inline_kb1)
        await TestFSM.name.set()

@dp.message_handler(state=TestFSM.name)
async def mailing(message: types.Message, state: FSMContext):
        if message.text == 'Назад':
            
            await TestFSM.unnext()
        
        async with state.proxy() as data:
            data['name'] = message.text
        # inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='назад')
        # inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
        await message.answer('Ведите фамилие', reply_markup=inline_kb1)
        await TestFSM.last_name.set()
        

@dp.message_handler(state=TestFSM.last_name)
async def mailing(message: types.Message, state: FSMContext):
        if message.text == 'Назад':
            await TestFSM.unnext()
            print('123')
        async with state.proxy() as data:
            data['last_name'] = message.text
        # markup = InlineKeyboardMarkup()
        # markup.insert(InlineKeyboardButton('назад', callback_data='назад'))
        await message.answer('Ведите номер', reply_markup=inline_kb1)
        await TestFSM.phone.set()


@dp.message_handler(state=TestFSM.phone)
async def mailing(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['phone'] = message.text
        # markup = InlineKeyboardMarkup()
        # markup.insert(InlineKeyboardButton('назад', callback_data='назад'))
        name = data.get('name')
        last_name = data.get('last_name')
        phone = data['phone']
        await message.answer(
            f'Имя {name}'
            f'Фамилие {last_name}'
            f'Номер {phone}'
            , reply_markup=inline_kb1)
        await state.finish()




# inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

# #bot.py
# @dp.message_handler(commands=['1'])
# async def process_command_1(message: types.Message):
#     await message.reply("Первая инлайн кнопка", reply_markup=inline_kb1)

# @dp.callback_query_handler(lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')