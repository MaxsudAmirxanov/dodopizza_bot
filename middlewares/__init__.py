from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .is_admin import IsAdmin


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(IsAdmin())
