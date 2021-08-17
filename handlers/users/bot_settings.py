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

def settings_script(miner_setting, minerid, call):
    miner = Miner.get(minerid=minerid)
    if miner_setting is False:
        miner_setting = True
    elif miner_setting is True:
        miner_setting = False
    miner.save()
    call.message.reply_markup = notifications(minerid)

@dp.message_handler(text='⚙️Настройки')
async def settings(message: types.Message):
    await message.answer(text='⚙️Открываем настройки...', reply_markup=settings_kb())

@dp.callback_query_handler(text='🔊')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(text='Нажмите на кнопку, чтобы настроить уведомления: ', reply_markup=notifications(miner.minerid))

@dp.callback_query_handler(text='balance_end_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.message.from_user.id)
    settings_script(miner.notify_balance, miner.minerid, call)

@dp.callback_query_handler(text='change_courses_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.message.from_user.id)
    settings_script(miner.notify_courses, miner.minerid, call)

@dp.callback_query_handler(text='reset_bot_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.message.from_user.id)
    settings_script(miner.notify_reset, miner.minerid, call)



