from aiogram import types
import peeweedbevolve
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.peewee import Miner
from loader import dp

def statistic_keyboard(update, next_smile, fast_sell):
    buttons = [
        InlineKeyboardButton(text='🔁', callback_data=update),
        InlineKeyboardButton(text=next_smile, callback_data=next_smile)
    ]


    updatebutton = InlineKeyboardMarkup(row_width=2)
    updatebutton.add(*buttons)
    if fast_sell is True:

        button = [
            InlineKeyboardButton(text='Быстрая продажа', callback_data='fast_sell')
        ]

        updatebutton.add(*button)
    return updatebutton

def mining_message_await(miner):
    text= f'Ваш отчёт по добыче:' \
    f'\nПользователь: @{miner.username}' \
    f'\n---' \
    f'\n💰 Баланс:{miner.balance:.2f}$' \
    f'\n💸 Затраты: {miner.expenses/60}$/мин' \
    f'\n---' \
    f'\n⬛️ Уголь: {miner.coal} шт.\n' \
    f'\n🟧 Олово: {miner.tin} шт.\n' \
    f'\n⬜️ Железо: {miner.iron} шт.\n' \
    f'\n⬜️ Серебро: {miner.silver} шт.\n' \
    f'\n🟨 Золото: {miner.aurum} шт.\n' \
    f'\n🟥 Платина: {miner.platinum} шт.\n' \
    f'\n🟦 Палладий: {miner.palladium} шт.\n' \
    f'\n---' \
    f'\n🗻Шахты: {miner.mines1 + miner.mines2 + miner.mines3 + miner.mines4} шт.' \
    f'\n👷‍♂️Шахтёры: {miner.minerstype1 + miner.minerstype2 + miner.minerstype3 + miner.minerstype4} чел.' \
    f'\n---' \
    f'\nПоделись статистикой с 👬друзьями!'
    return text

@dp.message_handler(text='⛏ Добыча')
async def mining(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    await message.answer(text=mining_message_await(miner), reply_markup=statistic_keyboard('update_statistic', '🧾', miner.fast_sell))

@dp.callback_query_handler(text='update_statistic')
async def update_statistic(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=mining_message_await(miner), reply_markup=statistic_keyboard('update_statistic', '🧾', miner.fast_sell))

@dp.callback_query_handler(text='⛏')
async def info_courses(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=mining_message_await(miner), reply_markup=statistic_keyboard('update_statistic', '🧾', miner.fast_sell))

