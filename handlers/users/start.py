from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.staer_keyboard import start_keyboard
from utils.db_api.db_commands_2 import add_customer, read_user_id

def chek():
    p = []
    for i in read_user_id():
        
        p.append(i[0])
       
        # print(1)
        # # print(i[0])
        # if id == i[0]:
        #     return False

    return p
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
 
    if str(message.from_user.id) not in chek():
        print(2)
        print(chek())

        if message.from_user.username:
            add_customer(name=message.from_user.first_name, last_name=message.from_user.last_name, user_name=message.from_user.username, user_id=message.from_user.id)
            
        else:
            add_customer(name=message.from_user.first_name, last_name=message.from_user.last_name, user_name='-', user_id=message.from_user.id)
            
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
