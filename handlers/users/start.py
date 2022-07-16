from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import bot

from loader import dp
from keyboards.default.staer_keyboard import start_keyboard
from utils.db_api.db_commands_2 import add_customer, read_user_id
from utils.db_api.database import Customer, Referrer, Referral

customer = Customer()
referrer_db = Referrer()
referral_db = Referral()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    args = message.get_args()
    print('диплинк')
    print(args)
    if args != '':
        print('12345')
        if int(args) == message.from_user.id:
            await message.answer("Извинитие, но вы не можете стать своим же рефералом")
        referrer_id = referrer_db.get_referrer_id(args)
        r = referral_db.add_referral(referrer_id[0][0], message.from_user.id)
        print(r)
        if message.from_user.username:
            if r != None:
                await bot.send_message(int(args), f'Вашей реферальной системой воспользовался @{message.from_user.username}')
        else:
            if r != None:
                bot.send_message(int(args), f'Вашей реферальной системой воспользовался {message.from_user.full_name}')
        
    if message.from_user.username:
        customer.add_customer(name=message.from_user.first_name, last_name=message.from_user.last_name, user_name=message.from_user.username, user_id=message.from_user.id)
        
    else:
        customer.add_customer(name=message.from_user.first_name, last_name=message.from_user.last_name, user_name='-', user_id=message.from_user.id)
        
    await message.answer(f"""
{message.from_user.first_name}, привет! 

Добро пожаловать в наш сервис доставки из ресторанов «Dodo Pizza»! 🍕🍟🥤 

Куда мы доставляем?

Как оформить заказ?

☑️ перейди на вкладку «Меню»
☑️ выбери те блюда, которые хочешь заказать
☑️ укажи их количество и адрес доставки

🔺заказы принимаем с 11:00 до 23:00 ежедневно
🔸минимальная сумма заказа — 1000₽
🔺время доставки — от 30 до 90 минут
🔸подробнее о стоимости и зоне доставки — во вкладке «Доставка»

Итак, скорее жми «Меню»
    
    
    """, reply_markup=start_keyboard
        )
