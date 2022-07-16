from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.staer_keyboard import start_keyboard
from utils.db_api.db_commands_2 import add_customer, read_user_id
from utils.db_api.database import Customer, Referrer

referrer_db = Referrer()
customer_db = Customer()


@dp.message_handler(text='📈 Реферальная система')
async def referral_link(message: types.Message):

    user_id = customer_db.find_customer_id(message.from_user.id)
    referrer_db.add_referrer(message.from_user.id, user_id[0][0])

   
    bot_user = await dp.bot.get_me()

    referal_link = f'https://t.me/{bot_user.username}?start={message.from_id}'
    await message.answer(
        f'В нашей реферальной системе мы предлогаем вам пригласить вашего друга в нашу пиццерию.\n'
        f"Ваш друг и вы получите купон со скидкой в 10% на любой заказ.\n\n"
        f"👇Ваша рефереральная ссылка 👇 \n{referal_link}"
        )