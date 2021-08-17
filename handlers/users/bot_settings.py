from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.peewee import Miner
from loader import dp

def settings_kb():
    buttons = [
        InlineKeyboardButton(text='🔊Уведомления', callback_data='🔊'),
        InlineKeyboardButton(text='🤖Другое', callback_data='🤖')
    ]
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard

def notifications(minerid):
    miner = Miner.get(minerid=minerid)

    notify_balance = 'О бунтах и забастовках'
    notify_courses = 'О смене курса'
    notify_reset = 'О перезапуске бота'

    if miner.notify_balance is True:
        notify_balance += '✅'
    elif miner.notify_balance is False:
        notify_balance += '❌'
    if miner.notify_courses is True:
        notify_courses += '✅'
    elif miner.notify_courses is False:
        notify_courses += '❌'
    if miner.notify_reset is True:
        notify_reset += '✅'
    elif miner.notify_reset is False:
        notify_reset += '❌'

    buttons = [
        InlineKeyboardButton(text=notify_balance, callback_data='balance_end_notify'),
        InlineKeyboardButton(text=notify_courses, callback_data='change_courses_notify'),
        InlineKeyboardButton(text=notify_reset, callback_data='reset_bot_notify'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard

def notifications_fixed(minerid):
    miner = Miner.get(minerid=minerid)

    notify_balance = 'О бунтах и забастовках'
    notify_courses = 'О смене курса'
    notify_reset = 'О перезапуске бота'

    if miner.notify_balance is True:
        notify_balance += '✅'
    elif miner.notify_balance is False:
        notify_balance += '❌'
    if miner.notify_courses is True:
        notify_courses += '✅'
    elif miner.notify_courses is False:
        notify_courses += '❌'
    if miner.notify_reset is True:
        notify_reset += '✅'
    elif miner.notify_reset is False:
        notify_reset += '❌'

    buttons = [
        InlineKeyboardButton(text=notify_balance, callback_data='balance_end_notify'),
        InlineKeyboardButton(text=notify_courses, callback_data='change_courses_notify'),
        InlineKeyboardButton(text=notify_reset, callback_data='reset_bot_notify'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(text='⚙️Настройки')
async def settings(message: types.Message):
    await message.answer(text='⚙️Открываем настройки...', reply_markup=settings_kb())

@dp.callback_query_handler(text='🔊')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text='Нажмите на кнопку, чтобы настроить уведомления: ', reply_markup=notifications(miner.minerid))

@dp.callback_query_handler(text='balance_end_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.notify_balance is False:
        miner.notify_balance = True
        miner.save()
    elif miner.notify_balance is True:
        miner.notify_balance = False
        miner.save()
    return call.message.edit_text(text='Изменения баланса приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications_fixed(miner.minerid))


@dp.callback_query_handler(text='change_courses_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.notify_courses is False:
        miner.notify_courses = True
        miner.save()
    elif miner.notify_courses is True:
        miner.notify_courses = False
        miner.save()
    return call.message.edit_text(text='Изменения курса приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications_fixed(miner.minerid))


@dp.callback_query_handler(text='reset_bot_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.notify_reset is False:
        miner.notify_reset = True
        miner.save()
    elif miner.notify_reset is True:
        miner.notify_reset = False
        miner.save()
    return call.message.edit_text(text='Изменения перезапуска приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications_fixed(miner.minerid))



