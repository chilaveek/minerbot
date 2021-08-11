from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.peewee import Miner
from keyboards.default.menu_keyboard import menu
from loader import dp

def change_type_assort():
    buttons = [
        InlineKeyboardButton(text='👷‍♂️Шахтёры', callback_data='miners'),
        InlineKeyboardButton(text='🗻Шахты', callback_data='mines')
    ]
    assortment = InlineKeyboardMarkup(row_width=2)
    assortment.add(*buttons)
    return assortment

def get1_assort():
    buttons = [
        InlineKeyboardButton(text='👷‍♂️1⭐️', callback_data='👷‍♂️1⭐️'),
        InlineKeyboardButton(text='👷‍♂️2⭐️', callback_data='👷‍♂️2⭐️'),
        InlineKeyboardButton(text='👷‍♂️3⭐️', callback_data='👷‍♂️3⭐️'),
        InlineKeyboardButton(text='👷‍♂️4⭐️', callback_data='👷‍♂️4⭐️'),
    ]
    assortment = InlineKeyboardMarkup(row_width=4)
    assortment.add(*buttons)
    return assortment

def get2_assort():
    buttons = [
        InlineKeyboardButton(text='🗻1⭐️', callback_data='🗻1⭐️'),
        InlineKeyboardButton(text='🗻2⭐️', callback_data='🗻2⭐️'),
        InlineKeyboardButton(text='🗻3⭐️', callback_data='🗻3⭐️'),
        InlineKeyboardButton(text='🗻4⭐️', callback_data='🗻4⭐️'),
    ]
    assortment = InlineKeyboardMarkup(row_width=4)
    assortment.add(*buttons)
    return assortment

def get_keyboard(cb_data, cb_back, cb_forward):
    buttons = [
        types.InlineKeyboardButton(text='⬅️', callback_data=cb_back),
        types.InlineKeyboardButton(text="💳Купить", callback_data=cb_data),
        types.InlineKeyboardButton(text="🙅‍♂️Отмена", callback_data='cancel'),
        types.InlineKeyboardButton(text='➡️', callback_data=cb_forward),
    ]
    keyboard = InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard
@dp.message_handler(text='🛒Магазин')
async def shop(message: types.Message):
    await message.answer('Вы зашли в <b>🛒Магазин</b>. Не уходите с пустыми руками', reply_markup=change_type_assort())

@dp.callback_query_handler(text='miners')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(text='Биржа труда шахтёров приветствует вас!', reply_markup=get1_assort())

@dp.callback_query_handler(text='👷‍♂️1⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр-Новичок</b>\n\n'
                                      '💬Только-только выучившийся на шахтёра студент без опыта\n--\n'
                                      '<b>🤑Цена:</b> 1000$\n--\n'
                                      '<b>💫ЗП:</b> 50$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 угля/cек, 2 олова/сек, 1 железо/сек',
                                 reply_markup=get_keyboard('miner1star', '👷‍♂️4⭐️', '👷‍♂️2⭐️'))

@dp.callback_query_handler(text='👷‍♂️2⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Бывалый</b>\n\n'
                                      '💬Более-менее опытный шахтёр\n--\n'
                                      '<b>🤑Цена:</b> 10000$\n--\n'
                                      '<b>💫ЗП:</b> 100$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 олова/сек, 2 железо/сек, 1 серебро/сек' ,
                                 reply_markup=get_keyboard('miner2star', '👷‍♂️1⭐️', '👷‍♂️3⭐️'))

@dp.callback_query_handler(text='👷‍♂️3⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Опытный</b>\n\n'
                                      '💬Шахтёр с приемлимым опытом\n--\n'
                                      '<b>🤑Цена:</b> 50 000$\n--\n'
                                      '<b>💫ЗП:</b> 1500$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 железа/сек, 2 серебра/сек, 1 золото/сек',
                                 reply_markup=get_keyboard('miner3star', '👷‍♂️2⭐️', '👷‍♂️4⭐️'))

@dp.callback_query_handler(text='👷‍♂️4⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Супер-Шахтёр</b>\n\n'
                                      '💬Шахтёр с необычнайным опытом и силами\n--\n'
                                      '<b>🤑Цена:</b> 1 150 000$\n--\n'
                                      '<b>💫ЗП:</b> 80 000$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 золота/сек 2 платины/сек, 1 палладий/сек',
                                 reply_markup=get_keyboard('miner4star', '👷‍♂️3⭐️', '👷‍♂️1⭐️'))

@dp.callback_query_handler(text='miner1star')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1000:
        if miner.mines1 * 7 > miner.minerstype1:
            miner.balance -= 1000
            miner.minerstype1 += 1
            miner.expenses += 50
            miner.save()
            await call.message.edit_text(text='+1 Шахтёр Новичок в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner2star')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 10000:
        if miner.mines2 * 7 > miner.minerstype2:
            miner.balance -= 10000
            miner.minerstype2 += 1
            miner.expenses += 120
            miner.save()
            await call.message.edit_text(text='+1 Бывалый Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner3star')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 50000:
        if miner.mines3 * 7 > miner.minerstype3:
            miner.balance -= 50000
            miner.minerstype3 += 1
            miner.expenses += 250
            miner.save()
            await call.message.edit_text(text='+1 Опытный Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner4star')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1000000:
        if miner.mines4 * 7 > miner.minerstype4:
            miner.balance -= 1000000
            miner.minerstype4 += 1
            miner.expenses += 5000
            miner.save()
            await call.message.edit_text(text='+1 Супер Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(text='Магазин земель горных местностей приветствует вас!', reply_markup=get2_assort())

@dp.callback_query_handler(text='🗻1⭐️')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Небольшая Шахта</b>\n\n'
                                      '💬Небольшая шахта в горной местности\n--\n'
                                      '<b>🤑Цена:</b> 8000$\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      'Доступна для шахтёров типа Новичок, 7 мест',
                                 reply_markup=get_keyboard('mines1star', '🗻4⭐️', '🗻2⭐️'))

@dp.callback_query_handler(text='🗻2⭐️')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Стандартная Шахта</b>\n\n'
                                      '💬Стандартная плодородня шахта\n--\n'
                                      '<b>🤑Цена:</b> 25 000$\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      'Доступна для шахтёров типа Бывалый, 7 мест',
                                 reply_markup=get_keyboard('mines2star', '🗻1⭐️', '🗻3⭐️'))

@dp.callback_query_handler(text='🗻3⭐️')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Глубокая Шахта</b>\n\n'
                                      '💬Достаточно глубокая шахта. Неопытные могут потеряться\n--\n'
                                      '<b>🤑Цена:</b> 100 000$\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      'Доступна для шахтёров типа Опытный, 7 мест',
                                 reply_markup=get_keyboard('mines3star', '🗻2⭐️', '🗻4⭐️'))

@dp.callback_query_handler(text='🗻4⭐️')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Очень Глубокая Шахта</b>\n\n'
                                      '💬Огромная шахта, тунеллей как в фильме "Спуск"\n--\n'
                                      '<b>🤑Цена:</b> 5 000 000$\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      'Доступна для шахтёров типа Супер, 3 места',
                                 reply_markup=get_keyboard('mines4star', '🗻3⭐️', '🗻1⭐️'))

@dp.callback_query_handler(text='mines1star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 4500:
        miner.balance -= 4500
        miner.mines1 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines2star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 25000:
        miner.balance -= 25000
        miner.mines2 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines3star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 100000:
        miner.balance -= 100000
        miner.mines3 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines4star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 5000000:
        miner.balance -= 5000000
        miner.mines4 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс', reply_markup=change_type_assort())