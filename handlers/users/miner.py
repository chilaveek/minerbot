from aiogram import types
import peeweedbevolve
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.peewee import Miner
from loader import dp

def updatestatbtn():
    buttons = [
        InlineKeyboardButton(text='🔁', callback_data='updatestatistic')
    ]
    updatebutton = InlineKeyboardMarkup(row_width=1)
    updatebutton.add(*buttons)
    return updatebutton

@dp.message_handler(text='⛏Добыча')
async def mining(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    await message.answer(text=f'Ваш отчёт по добыче:'
                         f'\nПользователь: @{miner.username}'
                         f'\n---'
                         f'\n💰Баланс:{miner.balance}$'
                         f'\n💸Затраты: {miner.expenses}$/час'
                         f'\n---'
                         f'\n⬛️Уголь: {miner.coal} шт.\n'
                         f'\n🟧Олово: {miner.tin} шт.\n'
                         f'\n⬜️Железо: {miner.iron} шт.\n'
                         f'\n⬜️Серебро: {miner.silver} шт.\n'                         
                         f'\n🟨Золото: {miner.aurum} шт.\n'
                         f'\n🟥Платина: {miner.platinum} шт.\n'
                         f'\n🟦Палладий: {miner.palladium} шт.\n'
                         f'\n---'
                         f'\n🗻Шахты: {miner.mines1 + miner.mines2 + miner.mines3 + miner.mines4} шт.'
                         f'\n👷‍♂️Шахтёры: {miner.minerstype1 + miner.minerstype2 + miner.minerstype3 + miner.minerstype4} чел.'
                         f'\n---'
                         f'\nПоделись статистикой с 👬друзьями!',
                         reply_markup=updatestatbtn())

@dp.callback_query_handler(text='updatestatistic')
async def updatestatistic(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=f'Ваш отчёт по добыче:'
                         f'\nПользователь: @{miner.username}'
                         f'\n---'
                         f'\n💰Баланс:{miner.balance}$'
                         f'\n💸Затраты: {miner.expenses}$/час'
                         f'\n---'
                         f'\n⬛️Уголь: {miner.coal} шт.\n'
                         f'\n🟧Олово: {miner.tin} шт.\n'
                         f'\n⬜️Железо: {miner.iron} шт.\n'
                         f'\n⬜️Серебро: {miner.silver} шт.\n'                         
                         f'\n🟨Золото: {miner.aurum} шт.\n'
                         f'\n🟥Платина: {miner.platinum} шт.\n'
                         f'\n🟦Палладий: {miner.palladium} шт.\n'
                         f'\n---'
                         f'\n🗻Шахты: {miner.mines1 + miner.mines2 + miner.mines3 + miner.mines4} шт.'
                         f'\n👷‍♂️Шахтёры: {miner.minerstype1 + miner.minerstype2 + miner.minerstype3 + miner.minerstype4} чел.'
                         f'\n---'
                         f'\nПоделись статистикой с 👬друзьями!',
                         reply_markup=updatestatbtn())
