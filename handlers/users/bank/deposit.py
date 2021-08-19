from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from random import randint

from data.peewee import Miner
from handlers.users.bank.bank import bank_keyboard
from loader import dp

def deposit_btn():
    button = [
        InlineKeyboardButton(text='➕', callback_data='deposit_plus'),
        InlineKeyboardButton(text='➖', callback_data='deposit_minus'),
        InlineKeyboardButton(text='Назад', callback_data='in_bank')
    ]
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(*button)
    return kb

class Deposit(StatesGroup):
    plus = State()
    minus = State()


@dp.callback_query_handler(text='deposit_in_bank')
async def deposit(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=f'Ваш общий вклад составляет <b>{miner.deposit}$</b>'
                              f'\nДоход с него составляет <b>{(miner.deposit*0.025).__round__(2)}$</b>'
                              f'\n---\n'
                              f'Вклад идёт в банк по ставке 2.5% в час, эти деньги приходят на ваш счёт. '
                              f'Например, за 1000$ вклада вы будете получать 25$ на счёт ежечасно. Думайте стратегически - '
                              f'не стоит тратить весь баланс на вклад', reply_markup=deposit_btn())

@dp.callback_query_handler(text='deposit_plus', state=None)
async def deposit_change(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=f'Окей, следующим сообщением введи сумму пополнения от 1 до {int(miner.balance)} (Ваш баланс на данный момент)'
                                      f'\nНапример: {randint(1, int(miner.balance))}')
    await Deposit.plus.set()

@dp.message_handler(state=Deposit.plus)
async def deposit_plus(message: types.Message, state=FSMContext):
    miner = Miner.get(minerid=message.from_user.id)
    deposit_num = message.text
    if deposit_num.isdigit() is True:
        deposit_num = int(message.text)
        if deposit_num > 0:
            if deposit_num <= miner.balance:
                miner.deposit += deposit_num
                miner.balance -= deposit_num
                miner.save()
                await message.answer(parse_mode='html', text='Транкзакция прошла успешно!', reply_markup=bank_keyboard())
            else:
                await message.answer(parse_mode='html', text='Сумма пополнения <b>НЕ</b> может быть больше вашего баланса', reply_markup=deposit_btn())
        else:
            await message.answer(parse_mode='html', text='Сумма пополнения <b>НЕ</b> может быть меньше нуля', reply_markup=deposit_btn())
    else:
        await message.answer('Вы прислали символы или число, содержащее символы. Повторите попытку.',reply_markup=deposit_btn())



    await state.finish()

@dp.callback_query_handler(text='deposit_minus', state=None)
async def deposit_change(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text=f'Окей, следующим сообщением введи сумму снятия с депозита от 1 до {int(miner.deposit)} (Cумма вашего депозита)'
                                      f'\nНапример: {randint(1, int(miner.deposit))}')
    await Deposit.minus.set()

@dp.message_handler(state=Deposit.minus)
async def deposit_plus(message: types.Message, state=FSMContext):
    miner = Miner.get(minerid=message.from_user.id)
    deposit_num = message.text
    if deposit_num.isdigit() is True:
        deposit_num = int(message.text)
        if deposit_num > 0:
            if deposit_num <= miner.deposit:
                miner.balance += deposit_num
                miner.deposit -= deposit_num
                miner.save()
                await message.answer(parse_mode='html', text='Транкзакция прошла успешно!', reply_markup=bank_keyboard())
            else:
                await message.answer(parse_mode='html', text='Сумма снятия <b>НЕ</b> может быть больше вашего депозита', reply_markup=deposit_btn())
        else:
            await message.answer(parse_mode='html', text='Сумма снятия <b>НЕ</b> может быть меньше нуля', reply_markup=deposit_btn())
    else:
        await message.answer('Вы прислали символы или число, содержащее символы. Повторите попытку.',reply_markup=deposit_btn())



    await state.finish()



@dp.callback_query_handler(text='in_bank')
async def in_bank(call: CallbackQuery):
    await call.message.edit_text(text='Вы зашли в <b>🏦 Банк</b>', reply_markup=bank_keyboard())