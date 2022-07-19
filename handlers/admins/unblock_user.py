from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.chek_admin import IsAdmin, Admin
from utils.db_api.database import Customer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.storage import FSMContext

customer_db = Customer()
admin_db = Admin()

from loader import bot

from loader import dp

class User_Unblock(StatesGroup):
    Q1 = State()

@dp.message_handler(IsAdmin(), commands='unblock_user')
async def admin(message: types.Message):
    await message.answer('Для Разблокировки пользователя введите его телеграм ID:👇 \n\n(чтобы узнать какие пользователи есть в Базе Данных используйте комманду /show_users)')

    await User_Unblock.Q1.set()

@dp.message_handler(state=User_Unblock.Q1)
async def admin(message: types.Message, state: FSMContext):
    answer_q1 = message.text
    # print(customer_db.find_customer_id(answer_q1))
    i = admin_db.unblocked_customer(answer_q1)
    print(i)
    if i == True:
        await message.answer(f'Пользовательбыл с ID {answer_q1} был разблокирован. Теперь он может пользоваться ботом'
        '(Чтоба разблокироват пользователя введите комманду /unblock_user)')
    else:
        await message.answer('Пользователя с таким ID не существует')
    await state.finish() 