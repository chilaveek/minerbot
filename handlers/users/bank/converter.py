from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from data.config import admins
from data.peewee import Miner, Courses
from handlers.users.bank.bank import bank_keyboard
from handlers.users.miner import statistic_keyboard
from keyboards.default.menu_keyboard import menu
from loader import dp


def sellkeyboard(minerid):
    miner = Miner.get(minerid=minerid)

    buttons = [
        InlineKeyboardButton(text='💵 Продать всё', callback_data='sell_all'),
        InlineKeyboardButton(text='Назад', callback_data='in_bank')
    ]
    sell_keyboard = InlineKeyboardMarkup(row_width=1)
    sell_keyboard.add(*buttons)

    return sell_keyboard


def coal(coal, coalcourse):
    coalprice = coal * coalcourse
    return coalprice


def tin(tin, tincourse):
    tinprice = tin * tincourse
    return tinprice


def iron(iron, ironcourse):
    ironprice = iron * ironcourse
    return ironprice


def silver(silver, silvercourse):
    silverprice = silver * silvercourse
    return silverprice


def aurum(aurum, aurumcourse):
    aurumprice = aurum * aurumcourse
    return aurumprice


def platinum(platinum, platinumcourse):
    platinumprice = platinum * platinumcourse
    return platinumprice


def palladium(palladium, palladiumcourse):
    palladiumprice = palladium * palladiumcourse
    return palladiumprice

def percent_create(ore, default_course):
    ans = ''
    percent = 100 * ore / default_course - 100
    if percent >= 0:
        ans = '+' + str(percent.__round__(1))
    elif percent < 0:
        ans = str(percent.__round__(1))
    return ans

def message_courses_await(course, money):

    text =  f'\n<b>🧾 Стоимость сырья</b>: {money:.2f}$\n' \
    f'<b>\n📊 Курс на данный момент (за 100 шт.) - </b>\n' \
    f'\n[Курс] \ [Процент по отн. к дефолтному курсу]\n' \
    f'\n⬛️ Уголь - {course.coal * 100:.5f}$ \ {percent_create(course.coal, 0.001)}%\n' \
    f'\n🟧 Олово - {course.tin * 100:.5f}$ \ {percent_create(course.tin, 0.005)}%\n' \
    f'\n⬜️ Железо - {course.iron * 100:.5f}$ \ {percent_create(course.iron, 0.03)}%\n' \
    f'\n⬜️ Серебро - {course.silver * 100:.5f}$ \ {percent_create(course.silver, 0.1)}%\n' \
    f'\n🟨 Золото - {course.aurum * 100:.5f}$ \ {percent_create(course.aurum, 5.0)}%\n' \
    f'\n🟥 Платина - {course.platinum * 100:.5f}$ \ {percent_create(course.platinum, 8.5)}%\n' \
    f'\n🟦 Палладий - {course.palladium * 100:.5f}$ \ {percent_create(course.palladium, 18.9)}%\n'
    return text

@dp.callback_query_handler(text='🧾')
async def info_courses(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    course = Courses.get()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    await call.message.edit_text(text=message_courses_await(course, money),
                                 reply_markup=statistic_keyboard('update_course', '⛏', miner.fast_sell))

@dp.callback_query_handler(text='update_course')
async def info_courses(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    course = Courses.get()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)

    await call.message.edit_text(text=message_courses_await(course, money),
                                           reply_markup=statistic_keyboard('update_course', '⛏'))


@dp.callback_query_handler(text='market_ore')
async def converter(call: CallbackQuery):
    miner = Miner.get(minerid=call.from_user.id)
    course = Courses.get()
    miner.work_id_converter = False
    miner.save()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    await call.message.edit_text(text=f'Вас приветствует биржа руд и ценных бумаг.\nРабота в шахтах <b>приостановлена</b>.'
                              f'\n🧾 Стоимость сырья на продажу: {money:.2f}$\n'
                              f'<b>\n📊 Из них - </b>\n'
                              f'\n⬛️ Уголь - {coal(miner.coal, course.coal):.2f}\n'
                              f'\n🟧 Олово - {tin(miner.tin, course.tin):.2f}\n'
                              f'\n⬜️ Железо - {iron(miner.iron, course.iron):.2f}\n'
                              f'\n⬜️ Серебро - {silver(miner.silver, course.silver):.2f}\n'
                              f'\n🟨 Золото - {aurum(miner.aurum, course.aurum):.2f}\n'
                              f'\n🟥 Платина - {platinum(miner.platinum, course.platinum):.2f}\n'
                              f'\n🟦 Палладий - {palladium(miner.palladium, course.palladium):.2f}\n',
                         reply_markup=sellkeyboard(call.from_user.id))




@dp.callback_query_handler(text='sell_all')
async def sell(call: CallbackQuery):
    course = Courses.get()
    miner = Miner.get(minerid=call.from_user.id)
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    miner.balance += money
    miner.coal, miner.tin, miner.iron, miner.silver, miner.aurum, miner.platinum, miner.palladium = 0, 0, 0, 0, 0, 0, 0
    miner.work_id_converter = True
    miner.save()
    await call.message.edit_text(text=f'📈Сделка прошла успешно! Вы продали всё, работа <b>возобновлена</b>.'
                              f'\n💰Баланс сейчас: {miner.balance:.2f}$', reply_markup=bank_keyboard())


@dp.message_handler(Command('reset_courses'))
async def reset(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    if miner.minerid in admins:
        course = Courses.get()
        course.coal, course.tin, course.iron, course.silver, course.aurum, course.platinum, course.palladium = 0.001, 0.005, 0.03, 0.1, 5.0, 8.5, 18.9
        course.save()
        await message.reply(text='Курс валюты сброшен до значения default')

@dp.callback_query_handler(text='fast_sell')
async def fast_sell(call: CallbackQuery):
    course = Courses.get()
    miner = Miner.get(minerid=call.from_user.id)
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    miner.balance += money
    miner.coal, miner.tin, miner.iron, miner.silver, miner.aurum, miner.platinum, miner.palladium = 0, 0, 0, 0, 0, 0, 0
    miner.work_id_converter = True
    miner.save()
    await call.message.edit_text(text=message_courses_await(course, money),
                                 reply_markup=statistic_keyboard('update_course', '⛏', miner.fast_sell))