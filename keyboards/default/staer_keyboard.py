from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_1 = KeyboardButton('🍴 Менью')
button_2 = KeyboardButton('👨‍💼 О нас')
button_3 = KeyboardButton('🛒 Корзина')
button_4 = KeyboardButton('📝 Заказы')
button_5 = KeyboardButton('📈 Реферальная система')

start_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
start_keyboard.add(button_1, button_2)
start_keyboard.add(button_4, button_3)
start_keyboard.row(button_5)
# start_keyboard.add(button_3)
# start_keyboard.add(button_4)