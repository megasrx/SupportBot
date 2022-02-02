from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp


@dp.message_handler(Command("support"))
async def ask_support(message: types.Message):
    text = "Qo'llab-quvvatlash xizmatiga xabar yuborishni xohlaysizmi? Unda quyidagi tugmani bosing!"
    