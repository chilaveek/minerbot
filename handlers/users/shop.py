from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.peewee import Miner
from keyboards.default.menu_keyboard import menu
from loader import dp


def change_type_assort():
    buttons = [
        InlineKeyboardButton(text='👷‍♂️ Шахтёры', callback_data='miners'),
        InlineKeyboardButton(text='🗻 Шахты', callback_data='mines')
    ]
    assortment = InlineKeyboardMarkup(row_width=2)
    assortment.add(*buttons)
    return assortment


def get1_assort():
    buttons = [
        InlineKeyboardButton(text='👷‍♂️⬛️', callback_data='👷‍♂️⬛️'),
        InlineKeyboardButton(text='👷‍♂️⬜️', callback_data='👷‍♂️⬜️'),
        InlineKeyboardButton(text='👷‍♂️🟨', callback_data='👷‍♂️🟨'),
        InlineKeyboardButton(text='👷‍♂️🟦', callback_data='👷‍♂️🟦'),
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
        InlineKeyboardButton(text='🗻⬛️', callback_data='🗻⬛️'),
        InlineKeyboardButton(text='🗻⬜️', callback_data='🗻⬜️'),
        InlineKeyboardButton(text='🗻🟨', callback_data='🗻🟨'),
        InlineKeyboardButton(text='🗻🟦', callback_data='🗻🟦'),
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
        types.InlineKeyboardButton(text="💳", callback_data=cb_data),
        types.InlineKeyboardButton(text="🙅‍♂️", callback_data='cancel'),
        types.InlineKeyboardButton(text='➡️', callback_data=cb_forward),
    ]
    keyboard = InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard


def mines_shop(type_mine, description, type_miner, plases, default_price, miner_mines):
    price = default_price * (1 + miner_mines * 0.25)
    price = str(price)
    text = '<b>' + type_mine + '</b>\n\n' \
                               '💬 ' + description + '\n--\n' \
                                                     '<b>🤑 Цена: </b>' + price + '$\n--\n' \
                                                                                  '<b>📄 Характеристики:</b> ' \
                                                                                  'Доступна для шахтёров типа ' + type_miner + ', ' + str(
        plases) + ' мест'
    return text


def mines_script(miner, default_price, mine_type):
    if miner.balance >= default_price:
        miner.balance -= default_price
        mine_type += 1
        miner.save()
        text = '+1 Шахта в ваших владениях!'
    else:
        text = 'Не хватает денег на счету, проверьте баланс',
    return text


@dp.message_handler(text='🛒 Магазин')
async def shop(message: types.Message):
    await message.answer('Вы зашли в <b>🛒Магазин</b>. Не уходите с пустыми руками', reply_markup=change_type_assort())


@dp.callback_query_handler(text='miners')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(text='Биржа труда шахтёров приветствует вас!', reply_markup=get1_assort())


@dp.callback_query_handler(text='👷‍♂️⬛️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр Онли Уголь</b>\n\n'
                                      '💬По неведомой причине, умеет добывать только уголь\n--\n'
                                      '<b>🤑Цена:</b> 75$\n--\n'
                                      '<b>💫ЗП:</b> 10$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '10 угля/сек',
                                 reply_markup=get_keyboard('miner_coal', '👷‍♂️4⭐️', '👷‍♂️⬜️'))

@dp.callback_query_handler(text='👷‍♂️⬜️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр Онли Железо</b>\n\n'
                                      '💬По неведомой причине, умеет добывать только железо\n--\n'
                                      '<b>🤑Цена:</b> 1500$\n--\n'
                                      '<b>💫ЗП:</b> 650$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '10 железа/сек',
                                 reply_markup=get_keyboard('miner_iron', '👷‍♂️⬛️', '👷‍♂️🟨'))

@dp.callback_query_handler(text='👷‍♂️🟨')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр Онли Золото</b>\n\n'
                                      '💬По неведомой причине, умеет добывать только золото\n--\n'
                                      '<b>🤑Цена:</b> 105 000$\n--\n'
                                      '<b>💫ЗП:</b> 90 000$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '10 золота/сек',
                                 reply_markup=get_keyboard('miner_aurum', '👷‍♂️⬜️', '👷‍♂️🟦'))

@dp.callback_query_handler(text='👷‍♂️🟦')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр Онли Палладий</b>\n\n'
                                      '💬По неведомой причине, умеет добывать только палладий\n--\n'
                                      '<b>🤑Цена:</b> 1 250 000$\n--\n'
                                      '<b>💫ЗП:</b> 395 000$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '10 палладия/сек',
                                 reply_markup=get_keyboard('miner_palladium', '👷‍♂️🟨', '👷‍♂️1⭐️'))



@dp.callback_query_handler(text='👷‍♂️1⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Шахтёр-Новичок</b>\n\n'
                                      '💬Только-только выучившийся на шахтёра студент без опыта\n--\n'
                                      '<b>🤑Цена:</b> 1000$\n--\n'
                                      '<b>💫ЗП:</b> 50$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 угля/cек, 2 олова/сек, 1 железо/сек',
                                 reply_markup=get_keyboard('miner1star', '👷‍♂️🟦', '👷‍♂️2⭐️'))


@dp.callback_query_handler(text='👷‍♂️2⭐️')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>Бывалый</b>\n\n'
                                      '💬Более-менее опытный шахтёр\n--\n'
                                      '<b>🤑Цена:</b> 10000$\n--\n'
                                      '<b>💫ЗП:</b> 100$/час\n--\n'
                                      '<b>📄Характеристики:</b> '
                                      '3 олова/сек, 2 железо/сек, 1 серебро/сек',
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
                                 reply_markup=get_keyboard('miner4star', '👷‍♂️3⭐️', '👷‍♂️⬛️'))


@dp.callback_query_handler(text='miner_coal')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 75:
        if miner.mines_coal * 10 > miner.minerstype_coal:
            miner.balance -= 75
            miner.minerstype_coal += 1
            miner.expenses += 10
            miner.save()
            await call.message.edit_text(text='+1 Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner_iron')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1500:
        if miner.mines_iron * 5 > miner.minerstype_iron:
            miner.balance -= 1500
            miner.minerstype_iron += 1
            miner.expenses += 650
            miner.save()
            await call.message.edit_text(text='+1 Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner_aurum')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 105000:
        if miner.mines_aurum * 5 > miner.minerstype_aurum:
            miner.balance -= 105000
            miner.minerstype_aurum += 1
            miner.expenses += 90000
            miner.save()
            await call.message.edit_text(text='+1 Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='miner_palladium')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1295000:
        if miner.minerstype_palladium * 3 > miner.minerstype_palladium:
            miner.balance -= 1295000
            miner.minerstype_palladium += 1
            miner.expenses += 395000
            miner.save()
            await call.message.edit_text(text='+1 Шахтёр в вашу шахту!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='Все шахты переполнены! Куда нам?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


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
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


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
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


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
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


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
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(text='Магазин земель горных местностей приветствует вас!', reply_markup=get2_assort())


@dp.callback_query_handler(text='🗻⬛️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Угольная Шахта'
    description = 'Узкоспециализированная шахта для добычи угля'
    type_miner = 'Онли Уголь'
    plases = '10'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 500, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_coal', '🗻4⭐️', '🗻⬜️'))

@dp.callback_query_handler(text='🗻⬜️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Железная Шахта'
    description = 'Узкоспециализированная шахта для добычи железа'
    type_miner = 'Онли Железо'
    plases = '5'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 6500, miner.mines_iron),
                                 reply_markup=get_keyboard('mines_iron', '🗻⬛️', '🗻🟨'))

@dp.callback_query_handler(text='🗻🟨')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Золотая Шахта'
    description = 'Узкоспециализированная шахта для добычи золота'
    type_miner = 'Онли Золото'
    plases = '5'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 150000, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_aurum', '🗻⬜️', '🗻🟦'))

@dp.callback_query_handler(text='🗻🟦')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Палладиевая Шахта'
    description = 'Узкоспециализированная шахта для добычи палладия'
    type_miner = 'Онли Палладий'
    plases = '3'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 1500000, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_palladium', '🗻🟨', '🗻1⭐️'))


@dp.callback_query_handler(text='🗻1⭐️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Небольшая шахта'
    description = 'Неглубокая шахта в горной местности'
    type_miner = 'Новичок'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 8000, miner.mines1),
                                 reply_markup=get_keyboard('mines1star', '🗻🟦', '🗻2⭐️'))


@dp.callback_query_handler(text='🗻2⭐️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Стандартная'
    description = 'Стандартная плодородная шахта'
    type_miner = 'Бывалый'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 25000, miner.mines2),
                                 reply_markup=get_keyboard('mines2star', '🗻1⭐️', '🗻3⭐️'))


@dp.callback_query_handler(text='🗻3⭐️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Глубокая шахта'
    description = 'Достаточно глубокая шахта. Неопытные могут потеряться'
    type_miner = 'Опытный'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 100000, miner.mines3),
                                 reply_markup=get_keyboard('mines3star', '🗻2⭐️', '🗻4⭐️'))


@dp.callback_query_handler(text='🗻4⭐️')
async def shop_mines(call: CallbackQuery):
    type_mine = 'Очень глубокая шахта'
    description = 'Огромная шахта тунеллей как в фильме "Спуск"'
    type_miner = 'Супер'
    plases = '3'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 5000000, miner.mines4),
                                 reply_markup=get_keyboard('mines4star', '🗻3⭐️', '🗻⬛️'))


@dp.callback_query_handler(text='mines_coal')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 500 * (1 + miner.mines_coal * 0.25):
        miner.balance -= 500 * (1 + miner.mines_coal * 0.25)
        miner.mines_coal += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_iron')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 6500 * (1 + miner.mines_iron * 0.25):
        miner.balance -= 6500 * (1 + miner.mines_iron * 0.25)
        miner.mines_iron += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_aurum')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 150000 * (1 + miner.mines_aurum * 0.25):
        miner.balance -= 150000 * (1 + miner.mines_aurum * 0.25)
        miner.mines_aurum += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_palladium')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1500000 * (1 + miner.mines_palladium * 0.25):
        miner.balance -= 1500000 * (1 + miner.mines_palladium * 0.25)
        miner.mines_palladium += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines1star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 8000 * (1 + miner.mines1 * 0.25):
        miner.balance -= 8000 * (1 + miner.mines1 * 0.25)
        miner.mines1 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines2star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 25000 * (1 + miner.mines2 * 0.25):
        miner.balance -= 25000 * (1 + miner.mines2 * 0.25)
        miner.mines2 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines3star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 100000 * (1 + miner.mines3 * 0.25):
        miner.balance -= 100000 * (1 + miner.mines3 * 0.25)
        miner.mines3 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines4star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 5000000 * (1 + miner.mines4 * 0.25):
        miner.balance -= 5000000 * (1 + miner.mines4 * 0.25)
        miner.mines4 += 1
        miner.save()
        await call.message.edit_text(text='+1 Шахта в ваших владениях!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='Не хватает денег на счету, проверьте баланс',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_text(text='Вернулись на главную', reply_markup=change_type_assort())
