from email import message
from secrets import choice
from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin
from utils.db_api.database import Product, Cart, Customer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
from typing import Union
from aiogram.types import InputFile
from aiogram.types.input_media import InputMediaPhoto

from loader import dp, bot

customer_db = Customer()
class MessageFSM(StatesGroup):
    message = State()
    choice = State()

class PhotoFSM(StatesGroup):
    photo = State()
    choice = State()

class PhotoMessageFSM(StatesGroup):
    photo = State()
    photo_choice = State()
    message = State()
    message_choice = State()
    


@dp.message_handler(IsAdmin(), text='/mailing')
async def start_mailing(message: types.Message):
    inline_btn_1 = InlineKeyboardButton('Сообщение', callback_data='message')
    inline_btn_2 = InlineKeyboardButton('Фото', callback_data='photo')
    inline_btn_3 = InlineKeyboardButton('Сообщение + фото', callback_data='message_photo')
    inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3)

    await message.answer('Для того, что бы разослать рассылку по всем пользователям, выберите тип рассылки.', reply_markup=inline_kb1)

@dp.callback_query_handler(text='message')
async def send_message(call: types.CallbackQuery):
    await call.message.answer('Отправте текст')
    await MessageFSM.message.set()


@dp.message_handler(state=MessageFSM.message)
async def send_message(call: types.Message, state: FSMContext):
    print(call)
    global message_text
    message_text = []
    message_text.append(call.text)

    async with state.proxy() as data:
        data['message'] = call.text

    

    await call.answer('Потверждаете рассылку ?\n(Да/Нет)')
    await MessageFSM.choice.set()

@dp.message_handler(state=MessageFSM.choice)
async def send_message(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    # text = data["message"]
    if answer.lower() == 'да':
        await message.answer('Начало рассылки')
        users = customer_db.read_customer_id()
        for id in users:
            # print(id)
            await bot.send_message(id[0], message_text[0])
        
        await message.answer(f'Рассылка завершена. Текст рассылки \n {message_text[0]}')
        await state.finish()

    elif answer.lower() == 'нет':
        await message.answer('Отмена рассылки')
        await state.finish()
        # await message.answer(f'{message_text[0]}')

    else:
        await state.finish()
        await message.answer('Не понял вас, да или нет ?')
        await MessageFSM.choice.set()
        
        





@dp.callback_query_handler(text='photo')
async def send_photo(call: types.CallbackQuery):
    await call.message.answer('Отправте одну фотогрвфию')
    await PhotoFSM.photo.set()


@dp.message_handler(state=PhotoFSM.photo, content_types=types.ContentTypes.PHOTO)
async def photo(message: types.Message, state: FSMContext, **kwargs):
    photo = message.photo[0].file_id
    print(photo)
    global message_photo
    message_photo = []
    message_photo.append(photo)

    async with state.proxy() as data:
        data['photo'] = photo

    

    await message.answer('Потверждаете рассылку ?\n(Да/Нет)')
    await PhotoFSM.choice.set()

@dp.message_handler(state=PhotoFSM.choice)
async def send_message(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    # text = data["message"]
    if answer.lower() == 'да':
        await message.answer('Начало рассылки')
        users = customer_db.read_customer_id()
        for id in users:
            # print(id)
            await bot.send_photo(id[0], message_photo[0])
        
        await message.answer(f'Рассылка завершена. Фото рассылки')
        await message.answer_photo(message_photo[0])
        await state.finish()
        
    elif answer.lower() == 'нет':
        await message.answer('Отмена рассылки')
        await state.finish()
        # await message.answer(f'{message_text[0]}')

    else:
        await state.finish()
        await message.answer('Не понял вас, да или нет ?')
        await MessageFSM.choice.set()





@dp.callback_query_handler(text='message_photo')
async def send_photo(call: types.CallbackQuery):
    await call.message.answer('Отправте одну фотогрвфию')
    await PhotoMessageFSM.photo.set()


@dp.message_handler(state=PhotoFSM.photo, content_types=types.ContentTypes.PHOTO)
async def photo(message: types.Message, state: FSMContext, **kwargs):
    photo = message.photo[0].file_id
    print(photo)
    global message_photo
    message_photo = []
    message_photo.append(photo)

    async with state.proxy() as data:
        data['photo'] = photo

    

    await message.answer('Потверждаете фото ?\n(Да/Нет)')
    await PhotoMessageFSM.photo_choice.set()

@dp.message_handler(state=PhotoMessageFSM.photo_choice)
async def send_message(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    # text = data["message"]
    if answer.lower() == 'да':
        await PhotoMessageFSM.message.set()
        
    elif answer.lower() == 'нет':
        await message.answer('Отмена рассылки')
        await state.finish()
        # await message.answer(f'{message_text[0]}')

    else:
        await state.finish()
        await message.answer('Не понял вас, да или нет ?')
        await MessageFSM.choice.set()


@dp.message_handler(state=PhotoMessageFSM.message)
async def photo(message: types.Message, state: FSMContext, **kwargs):
    answer = message.text
    global message_text
    message_text = []
    

    async with state.proxy() as data:
        data['message'] = answer

    

    await message.answer('Потверждаете текст ?\n(Да/Нет)')
    await PhotoMessageFSM.photo_choice.set()

@dp.message_handler(state=PhotoMessageFSM.photo_choice)
async def send_message(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    # text = data["message"]
    if answer.lower() == 'да':
        "Начало рассылки"
        await message.answer('Начало рассылки')
        users = customer_db.read_customer_id()
        for id in users:
            # print(id)
            await bot.send_photo(id[0], message_photo[0])
            await bot.send_message(id[0], message_text)
            await state.finish()
        
    elif answer.lower() == 'нет':
        await message.answer('Отмена рассылки')
        await state.finish()
        # await message.answer(f'{message_text[0]}')

    else:
        await state.finish()
        await message.answer('Не понял вас, да или нет ?')
        await MessageFSM.choice.set()
        