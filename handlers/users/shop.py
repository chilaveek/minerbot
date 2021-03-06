from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.peewee import Miner
from keyboards.default.menu_keyboard import menu
from loader import dp


def change_type_assort():
    buttons = [
        InlineKeyboardButton(text='๐ทโโ๏ธ ะจะฐััััั', callback_data='miners'),
        InlineKeyboardButton(text='๐ป ะจะฐััั', callback_data='mines')
    ]
    assortment = InlineKeyboardMarkup(row_width=2)
    assortment.add(*buttons)
    return assortment


def get1_assort():
    buttons = [
        InlineKeyboardButton(text='๐ทโโ๏ธโฌ๏ธ', callback_data='๐ทโโ๏ธโฌ๏ธ'),
        InlineKeyboardButton(text='๐ทโโ๏ธโฌ๏ธ', callback_data='๐ทโโ๏ธโฌ๏ธ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ๐จ', callback_data='๐ทโโ๏ธ๐จ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ๐ฆ', callback_data='๐ทโโ๏ธ๐ฆ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ1โญ๏ธ', callback_data='๐ทโโ๏ธ1โญ๏ธ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ2โญ๏ธ', callback_data='๐ทโโ๏ธ2โญ๏ธ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ3โญ๏ธ', callback_data='๐ทโโ๏ธ3โญ๏ธ'),
        InlineKeyboardButton(text='๐ทโโ๏ธ4โญ๏ธ', callback_data='๐ทโโ๏ธ4โญ๏ธ'),
    ]
    assortment = InlineKeyboardMarkup(row_width=4)
    assortment.add(*buttons)
    return assortment


def get2_assort():
    buttons = [
        InlineKeyboardButton(text='๐ปโฌ๏ธ', callback_data='๐ปโฌ๏ธ'),
        InlineKeyboardButton(text='๐ปโฌ๏ธ', callback_data='๐ปโฌ๏ธ'),
        InlineKeyboardButton(text='๐ป๐จ', callback_data='๐ป๐จ'),
        InlineKeyboardButton(text='๐ป๐ฆ', callback_data='๐ป๐ฆ'),
        InlineKeyboardButton(text='๐ป1โญ๏ธ', callback_data='๐ป1โญ๏ธ'),
        InlineKeyboardButton(text='๐ป2โญ๏ธ', callback_data='๐ป2โญ๏ธ'),
        InlineKeyboardButton(text='๐ป3โญ๏ธ', callback_data='๐ป3โญ๏ธ'),
        InlineKeyboardButton(text='๐ป4โญ๏ธ', callback_data='๐ป4โญ๏ธ'),
    ]
    assortment = InlineKeyboardMarkup(row_width=4)
    assortment.add(*buttons)
    return assortment


def get_keyboard(cb_data, cb_back, cb_forward):
    buttons = [
        types.InlineKeyboardButton(text='โฌ๏ธ', callback_data=cb_back),
        types.InlineKeyboardButton(text="๐ณ", callback_data=cb_data),
        types.InlineKeyboardButton(text="๐โโ๏ธ", callback_data='cancel'),
        types.InlineKeyboardButton(text='โก๏ธ', callback_data=cb_forward),
    ]
    keyboard = InlineKeyboardMarkup(row_width=4)
    keyboard.add(*buttons)
    return keyboard


def mines_shop(type_mine, description, type_miner, plases, default_price, miner_mines):
    price = default_price * (1 + miner_mines * 0.25)
    price = str(price)
    text = '<b>' + type_mine + '</b>\n\n' \
                               '๐ฌ ' + description + '\n--\n' \
                                                     '<b>๐ค ะฆะตะฝะฐ: </b>' + price + '$\n--\n' \
                                                                                  '<b>๐ ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> ' \
                                                                                  'ะะพัััะฟะฝะฐ ะดะปั ัะฐััััะพะฒ ัะธะฟะฐ ' + type_miner + ', ' + str(
        plases) + ' ะผะตัั'
    return text


def mines_script(miner, default_price, mine_type):
    if miner.balance >= default_price:
        miner.balance -= default_price
        mine_type += 1
        miner.save()
        text = '+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!'
    else:
        text = 'ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
    return text


@dp.message_handler(text='๐ ะะฐะณะฐะทะธะฝ')
async def shop(message: types.Message):
    await message.answer('ะั ะทะฐัะปะธ ะฒ <b>๐ะะฐะณะฐะทะธะฝ</b>. ะะต ััะพะดะธัะต ั ะฟััััะผะธ ััะบะฐะผะธ', reply_markup=change_type_assort())


@dp.callback_query_handler(text='miners')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(text='ะะธัะถะฐ ัััะดะฐ ัะฐััััะพะฒ ะฟัะธะฒะตัััะฒัะตั ะฒะฐั!', reply_markup=get1_assort())


@dp.callback_query_handler(text='๐ทโโ๏ธโฌ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะจะฐัััั ะะฝะปะธ ะฃะณะพะปั</b>\n\n'
                                      '๐ฌะะพ ะฝะตะฒะตะดะพะผะพะน ะฟัะธัะธะฝะต, ัะผะตะตั ะดะพะฑัะฒะฐัั ัะพะปัะบะพ ัะณะพะปั\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 75$\n--\n'
                                      '<b>๐ซะะ:</b> 10$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '10 ัะณะปั/ัะตะบ',
                                 reply_markup=get_keyboard('miner_coal', '๐ทโโ๏ธ4โญ๏ธ', '๐ทโโ๏ธโฌ๏ธ'))

@dp.callback_query_handler(text='๐ทโโ๏ธโฌ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะจะฐัััั ะะฝะปะธ ะะตะปะตะทะพ</b>\n\n'
                                      '๐ฌะะพ ะฝะตะฒะตะดะพะผะพะน ะฟัะธัะธะฝะต, ัะผะตะตั ะดะพะฑัะฒะฐัั ัะพะปัะบะพ ะถะตะปะตะทะพ\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 1500$\n--\n'
                                      '<b>๐ซะะ:</b> 650$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '10 ะถะตะปะตะทะฐ/ัะตะบ',
                                 reply_markup=get_keyboard('miner_iron', '๐ทโโ๏ธโฌ๏ธ', '๐ทโโ๏ธ๐จ'))

@dp.callback_query_handler(text='๐ทโโ๏ธ๐จ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะจะฐัััั ะะฝะปะธ ะะพะปะพัะพ</b>\n\n'
                                      '๐ฌะะพ ะฝะตะฒะตะดะพะผะพะน ะฟัะธัะธะฝะต, ัะผะตะตั ะดะพะฑัะฒะฐัั ัะพะปัะบะพ ะทะพะปะพัะพ\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 105 000$\n--\n'
                                      '<b>๐ซะะ:</b> 90 000$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '10 ะทะพะปะพัะฐ/ัะตะบ',
                                 reply_markup=get_keyboard('miner_aurum', '๐ทโโ๏ธโฌ๏ธ', '๐ทโโ๏ธ๐ฆ'))

@dp.callback_query_handler(text='๐ทโโ๏ธ๐ฆ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะจะฐัััั ะะฝะปะธ ะะฐะปะปะฐะดะธะน</b>\n\n'
                                      '๐ฌะะพ ะฝะตะฒะตะดะพะผะพะน ะฟัะธัะธะฝะต, ัะผะตะตั ะดะพะฑัะฒะฐัั ัะพะปัะบะพ ะฟะฐะปะปะฐะดะธะน\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 1 250 000$\n--\n'
                                      '<b>๐ซะะ:</b> 395 000$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '10 ะฟะฐะปะปะฐะดะธั/ัะตะบ',
                                 reply_markup=get_keyboard('miner_palladium', '๐ทโโ๏ธ๐จ', '๐ทโโ๏ธ1โญ๏ธ'))



@dp.callback_query_handler(text='๐ทโโ๏ธ1โญ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะจะฐัััั-ะะพะฒะธัะพะบ</b>\n\n'
                                      '๐ฌะขะพะปัะบะพ-ัะพะปัะบะพ ะฒัััะธะฒัะธะนัั ะฝะฐ ัะฐััััะฐ ัััะดะตะฝั ะฑะตะท ะพะฟััะฐ\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 1000$\n--\n'
                                      '<b>๐ซะะ:</b> 50$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '3 ัะณะปั/cะตะบ, 2 ะพะปะพะฒะฐ/ัะตะบ, 1 ะถะตะปะตะทะพ/ัะตะบ',
                                 reply_markup=get_keyboard('miner1star', '๐ทโโ๏ธ๐ฆ', '๐ทโโ๏ธ2โญ๏ธ'))


@dp.callback_query_handler(text='๐ทโโ๏ธ2โญ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะัะฒะฐะปัะน</b>\n\n'
                                      '๐ฌะะพะปะตะต-ะผะตะฝะตะต ะพะฟััะฝัะน ัะฐัััั\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 10000$\n--\n'
                                      '<b>๐ซะะ:</b> 100$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '3 ะพะปะพะฒะฐ/ัะตะบ, 2 ะถะตะปะตะทะพ/ัะตะบ, 1 ัะตัะตะฑัะพ/ัะตะบ',
                                 reply_markup=get_keyboard('miner2star', '๐ทโโ๏ธ1โญ๏ธ', '๐ทโโ๏ธ3โญ๏ธ'))


@dp.callback_query_handler(text='๐ทโโ๏ธ3โญ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะะฟััะฝัะน</b>\n\n'
                                      '๐ฌะจะฐัััั ั ะฟัะธะตะผะปะธะผัะผ ะพะฟััะพะผ\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 50 000$\n--\n'
                                      '<b>๐ซะะ:</b> 1500$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '3 ะถะตะปะตะทะฐ/ัะตะบ, 2 ัะตัะตะฑัะฐ/ัะตะบ, 1 ะทะพะปะพัะพ/ัะตะบ',
                                 reply_markup=get_keyboard('miner3star', '๐ทโโ๏ธ2โญ๏ธ', '๐ทโโ๏ธ4โญ๏ธ'))


@dp.callback_query_handler(text='๐ทโโ๏ธ4โญ๏ธ')
async def shop_miners(call: CallbackQuery):
    await call.message.edit_text(parse_mode='html',
                                 text='<b>ะกัะฟะตั-ะจะฐัััั</b>\n\n'
                                      '๐ฌะจะฐัััั ั ะฝะตะพะฑััะฝะฐะนะฝัะผ ะพะฟััะพะผ ะธ ัะธะปะฐะผะธ\n--\n'
                                      '<b>๐คะฆะตะฝะฐ:</b> 1 150 000$\n--\n'
                                      '<b>๐ซะะ:</b> 80 000$/ัะฐั\n--\n'
                                      '<b>๐ะฅะฐัะฐะบัะตัะธััะธะบะธ:</b> '
                                      '3 ะทะพะปะพัะฐ/ัะตะบ 2 ะฟะปะฐัะธะฝั/ัะตะบ, 1 ะฟะฐะปะปะฐะดะธะน/ัะตะบ',
                                 reply_markup=get_keyboard('miner4star', '๐ทโโ๏ธ3โญ๏ธ', '๐ทโโ๏ธโฌ๏ธ'))


@dp.callback_query_handler(text='miner_coal')
async def shop_miners(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 75:
        if miner.mines_coal * 10 > miner.minerstype_coal:
            miner.balance -= 75
            miner.minerstype_coal += 1
            miner.expenses += 10
            miner.save()
            await call.message.edit_text(text='+1 ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะจะฐัััั ะะพะฒะธัะพะบ ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะัะฒะฐะปัะน ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะะฟััะฝัะน ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
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
            await call.message.edit_text(text='+1 ะกัะฟะตั ะจะฐัััั ะฒ ะฒะฐัั ัะฐััั!', reply_markup=change_type_assort())
        else:
            await call.message.edit_text(text='ะัะต ัะฐััั ะฟะตัะตะฟะพะปะฝะตะฝั! ะัะดะฐ ะฝะฐะผ?', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines')
async def shop_mines(call: CallbackQuery):
    await call.message.edit_text(text='ะะฐะณะฐะทะธะฝ ะทะตะผะตะปั ะณะพัะฝัั ะผะตััะฝะพััะตะน ะฟัะธะฒะตัััะฒัะตั ะฒะฐั!', reply_markup=get2_assort())


@dp.callback_query_handler(text='๐ปโฌ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะฃะณะพะปัะฝะฐั ะจะฐััะฐ'
    description = 'ะฃะทะบะพัะฟะตัะธะฐะปะธะทะธัะพะฒะฐะฝะฝะฐั ัะฐััะฐ ะดะปั ะดะพะฑััะธ ัะณะปั'
    type_miner = 'ะะฝะปะธ ะฃะณะพะปั'
    plases = '10'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 500, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_coal', '๐ป4โญ๏ธ', '๐ปโฌ๏ธ'))

@dp.callback_query_handler(text='๐ปโฌ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะะตะปะตะทะฝะฐั ะจะฐััะฐ'
    description = 'ะฃะทะบะพัะฟะตัะธะฐะปะธะทะธัะพะฒะฐะฝะฝะฐั ัะฐััะฐ ะดะปั ะดะพะฑััะธ ะถะตะปะตะทะฐ'
    type_miner = 'ะะฝะปะธ ะะตะปะตะทะพ'
    plases = '5'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 6500, miner.mines_iron),
                                 reply_markup=get_keyboard('mines_iron', '๐ปโฌ๏ธ', '๐ป๐จ'))

@dp.callback_query_handler(text='๐ป๐จ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะะพะปะพัะฐั ะจะฐััะฐ'
    description = 'ะฃะทะบะพัะฟะตัะธะฐะปะธะทะธัะพะฒะฐะฝะฝะฐั ัะฐััะฐ ะดะปั ะดะพะฑััะธ ะทะพะปะพัะฐ'
    type_miner = 'ะะฝะปะธ ะะพะปะพัะพ'
    plases = '5'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 150000, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_aurum', '๐ปโฌ๏ธ', '๐ป๐ฆ'))

@dp.callback_query_handler(text='๐ป๐ฆ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะะฐะปะปะฐะดะธะตะฒะฐั ะจะฐััะฐ'
    description = 'ะฃะทะบะพัะฟะตัะธะฐะปะธะทะธัะพะฒะฐะฝะฝะฐั ัะฐััะฐ ะดะปั ะดะพะฑััะธ ะฟะฐะปะปะฐะดะธั'
    type_miner = 'ะะฝะปะธ ะะฐะปะปะฐะดะธะน'
    plases = '3'
    miner = Miner.get(minerid=call.from_user.id)

    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 1500000, miner.mines_coal),
                                 reply_markup=get_keyboard('mines_palladium', '๐ป๐จ', '๐ป1โญ๏ธ'))


@dp.callback_query_handler(text='๐ป1โญ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะะตะฑะพะปััะฐั ัะฐััะฐ'
    description = 'ะะตะณะปัะฑะพะบะฐั ัะฐััะฐ ะฒ ะณะพัะฝะพะน ะผะตััะฝะพััะธ'
    type_miner = 'ะะพะฒะธัะพะบ'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 8000, miner.mines1),
                                 reply_markup=get_keyboard('mines1star', '๐ป๐ฆ', '๐ป2โญ๏ธ'))


@dp.callback_query_handler(text='๐ป2โญ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะกัะฐะฝะดะฐััะฝะฐั'
    description = 'ะกัะฐะฝะดะฐััะฝะฐั ะฟะปะพะดะพัะพะดะฝะฐั ัะฐััะฐ'
    type_miner = 'ะัะฒะฐะปัะน'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 25000, miner.mines2),
                                 reply_markup=get_keyboard('mines2star', '๐ป1โญ๏ธ', '๐ป3โญ๏ธ'))


@dp.callback_query_handler(text='๐ป3โญ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะะปัะฑะพะบะฐั ัะฐััะฐ'
    description = 'ะะพััะฐัะพัะฝะพ ะณะปัะฑะพะบะฐั ัะฐััะฐ. ะะตะพะฟััะฝัะต ะผะพะณัั ะฟะพัะตัััััั'
    type_miner = 'ะะฟััะฝัะน'
    plases = '7'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 100000, miner.mines3),
                                 reply_markup=get_keyboard('mines3star', '๐ป2โญ๏ธ', '๐ป4โญ๏ธ'))


@dp.callback_query_handler(text='๐ป4โญ๏ธ')
async def shop_mines(call: CallbackQuery):
    type_mine = 'ะัะตะฝั ะณะปัะฑะพะบะฐั ัะฐััะฐ'
    description = 'ะะณัะพะผะฝะฐั ัะฐััะฐ ััะฝะตะปะปะตะน ะบะฐะบ ะฒ ัะธะปัะผะต "ะกะฟััะบ"'
    type_miner = 'ะกัะฟะตั'
    plases = '3'
    miner = Miner.get(minerid=call.from_user.id)
    await call.message.edit_text(parse_mode='html',
                                 text=mines_shop(type_mine, description, type_miner, plases, 5000000, miner.mines4),
                                 reply_markup=get_keyboard('mines4star', '๐ป3โญ๏ธ', '๐ปโฌ๏ธ'))


@dp.callback_query_handler(text='mines_coal')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 500 * (1 + miner.mines_coal * 0.25):
        miner.balance -= 500 * (1 + miner.mines_coal * 0.25)
        miner.mines_coal += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_iron')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 6500 * (1 + miner.mines_iron * 0.25):
        miner.balance -= 6500 * (1 + miner.mines_iron * 0.25)
        miner.mines_iron += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_aurum')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 150000 * (1 + miner.mines_aurum * 0.25):
        miner.balance -= 150000 * (1 + miner.mines_aurum * 0.25)
        miner.mines_aurum += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())

@dp.callback_query_handler(text='mines_palladium')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 1500000 * (1 + miner.mines_palladium * 0.25):
        miner.balance -= 1500000 * (1 + miner.mines_palladium * 0.25)
        miner.mines_palladium += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines1star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 8000 * (1 + miner.mines1 * 0.25):
        miner.balance -= 8000 * (1 + miner.mines1 * 0.25)
        miner.mines1 += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines2star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 25000 * (1 + miner.mines2 * 0.25):
        miner.balance -= 25000 * (1 + miner.mines2 * 0.25)
        miner.mines2 += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines3star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 100000 * (1 + miner.mines3 * 0.25):
        miner.balance -= 100000 * (1 + miner.mines3 * 0.25)
        miner.mines3 += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='mines4star')
async def shop_mines(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    if miner.balance >= 5000000 * (1 + miner.mines4 * 0.25):
        miner.balance -= 5000000 * (1 + miner.mines4 * 0.25)
        miner.mines4 += 1
        miner.save()
        await call.message.edit_text(text='+1 ะจะฐััะฐ ะฒ ะฒะฐัะธั ะฒะปะฐะดะตะฝะธัั!', reply_markup=change_type_assort())
    else:
        await call.message.edit_text(text='ะะต ัะฒะฐัะฐะตั ะดะตะฝะตะณ ะฝะฐ ััะตัั, ะฟัะพะฒะตัััะต ะฑะฐะปะฐะฝั',
                                     reply_markup=change_type_assort())


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_text(text='ะะตัะฝัะปะธัั ะฝะฐ ะณะปะฐะฒะฝัั', reply_markup=change_type_assort())
