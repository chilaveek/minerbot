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
        InlineKeyboardButton(text='Назад', callback_data='in_settings'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard

def other_settings(minerid):
    miner = Miner.get(minerid=minerid)
    fast_sell_text = 'Быстрая продажа'

    if miner.fast_sell is True:
        fast_sell_text += '✅'
    elif miner.fast_sell is False:
        fast_sell_text += '❌'

    buttons = [
        InlineKeyboardButton(text=fast_sell_text, callback_data='fast_sell_activate'),
        InlineKeyboardButton(text='Назад', callback_data='in_settings'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(text='⚙️ Настройки')
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
    await call.message.edit_text(text='Изменения баланса приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications(miner.minerid))


@dp.callback_query_handler(text='change_courses_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.notify_courses is False:
        miner.notify_courses = True
        miner.save()
    elif miner.notify_courses is True:
        miner.notify_courses = False
        miner.save()
    await call.message.edit_text(text='Изменения курса приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications(miner.minerid))


@dp.callback_query_handler(text='reset_bot_notify')
async def notify(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.notify_reset is False:
        miner.notify_reset = True
        miner.save()
    elif miner.notify_reset is True:
        miner.notify_reset = False
        miner.save()
    await call.message.edit_text(text='Изменения перезапуска приняты. Нажмите на кнопку, чтобы настроить уведомления',
                           reply_markup=notifications(miner.minerid))

@dp.callback_query_handler(text='🤖')
async def notify(call: CallbackQuery):
    await call.message.edit_text(text='Нажмите на кнопку, чтобы применить настройку: ',
                                 reply_markup=other_settings(call.from_user.id))


@dp.callback_query_handler(text='fast_sell_activate')
async def activate(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.fast_sell is False:
        miner.fast_sell = True
        miner.save()
    elif miner.fast_sell is True:
        miner.fast_sell = False
        miner.save()
    await call.message.edit_text(text='Кнопка <b>Быстрая продажа</b> добавлена в раздел <b>⛏Добыча</b>. '
                                      'Нажмите на кнопку, чтобы применить настройку:',
                                 reply_markup=other_settings(call.from_user.id))

@dp.callback_query_handler(text='in_settings')
async def back(call: CallbackQuery):
    await call.message.edit_text(text='⚙️ Вернулись...', reply_markup=settings_kb())