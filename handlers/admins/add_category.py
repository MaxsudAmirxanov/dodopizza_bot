from email import message
from os import stat
from unicodedata import category
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
from googletrans import Translator


product_db = Product()


class AddCategory(StatesGroup):
    category_name = State()
    category_code = State()
    choice = State()


# @dp.message_handler(IsAdmin())
# async def catefory_ctart(message: types.Message):
#     translator = Translator()
#     result = translator.translate(message.text)
    
#     # await message.answer(f'Перевод {result}')
#     await message.answer(f'Перевод {result.text}')



'⬇️'
@dp.message_handler(IsAdmin(), commands='add_category')
async def catefory_start(message: types.Message):
    await message.answer('Ведите название для категории 👇')

    await AddCategory.category_name.set()

@dp.message_handler(IsAdmin(), state=AddCategory.category_name)
async def catefory_name(message: types.Message, state: FSMContext):

    answer = message.text
    categories = product_db.get_category_name_distinct()
    

    print(categories)
    category_names = []
    for i in categories:
        category_names.append(i[0].lower())

    if  answer.lower() in category_names:
        await message.answer('Такая категория уже существует')
        await state.finish()
    else:


        async with state.proxy() as data:
            data['category_name'] = answer

        await message.answer(f'Подтверждаете название {answer}\n(Да/Нет)')
        translator = Translator()
        result = translator.translate(message.text, )

        # await message.answer(f'Перевод {result.text}')
        async with state.proxy() as data:
            data['category_code'] = result.text
        await AddCategory.choice.set()   

            

@dp.message_handler(IsAdmin(), state=AddCategory.choice)
async def catefory_choice(message: types.Message, state: FSMContext):

    answer = message.text

    data = await state.get_data()

    answer = message.text
    if answer.lower() == 'да':
        'Добавление категории'
        await message.answer(f'Добавление категории {data["category_name"]}')
        product_db.add_category(data['category_name'], data['category_code'])
        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена добавлению')
        await state.finish() 