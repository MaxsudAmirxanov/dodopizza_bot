from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.staer_keyboard import start_keyboard

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("""
Махсуд, привет! 

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
