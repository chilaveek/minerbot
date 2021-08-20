from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.peewee import Miner
from keyboards.default.menu_keyboard import bank_kb
from loader import dp

def bank_keyboard():
    buttons = [
        InlineKeyboardButton(text='💱 Рынок руд', callback_data='market_ore'),
        InlineKeyboardButton(text='💵 Вклады', callback_data='deposit_in_bank'),
    ]
    kb = InlineKeyboardMarkup(row_width=1).add(*buttons)
    return kb

@dp.message_handler(text='🏦 Банк')
async def bank(message: types.Message):
    await message.answer('Вы зашли в <b>🏦 Банк</b>', reply_markup=bank_keyboard())