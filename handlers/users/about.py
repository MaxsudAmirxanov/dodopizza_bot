from cgitb import text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default.staer_keyboard import start_keyboard
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.message_handler(text='👨‍💼 О нас')
async def bot_start(message: types.Message):
    inline_kb_full = InlineKeyboardMarkup(row_width=2)
    inline_kb_full.add(InlineKeyboardButton('Подробнее', url='https://dodopizza.ru/moscow/about'))
    await message.answer("""
    <b>Мы</b>

Обычно люди приходят в Додо Пиццу, чтобы просто поесть. Наши промоутеры раздают листовки про кусочек пиццы за двадцать рублей или ещё что-то выгодное. Мы делаем это как первый шаг, чтобы познакомиться.

Но для нас Додо — не только пицца. Это и пицца тоже, но в первую очередь это большое дело, которое вдохновляет нас, заставляет каждое утро просыпаться и с интересом продолжать работу.

""", reply_markup=inline_kb_full)