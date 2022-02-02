from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.inline.support import support_keyboards, support_callback
from loader import dp, bot


@dp.message_handler(Command("support"))
async def ask_support(message: types.Message):
    text = "Qo'llab-quvvatlash xizmatiga xabar yuborishni xohlaysizmi? Unda quyidagi tugmani bosing!"
    keyboard = await support_keyboards(messages="one")
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data:dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))

    await call.message.answer("Qo'llab-quvvatlash xizmatiga yubormoqchi bo'lgan xabaringizni kiriting")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)


@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id, "Sizga xabar yubrildi. Javb berish uchun quyidagi tugmani bosing")
    keyboard = await support_keyboards(messages="one", user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)

    await message.answer("Siz ushbu xabarni yubordingiz")

    await state.reset_state()

