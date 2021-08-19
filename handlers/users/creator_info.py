from aiogram import types

from loader import dp

@dp.message_handler(text='😇 Создатель')
async def creatorinfo(message: types.Message):
    await message.answer('🌌Мой создатель: @chilaveek')

