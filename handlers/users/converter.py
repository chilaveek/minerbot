from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from data.config import admins
from data.peewee import Miner, Courses
from keyboards.default.menu_keyboard import menu
from loader import dp


def sellkeyboard(minerid):
    miner = Miner.get(minerid=minerid)

    sell_keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            #            [
            #                KeyboardButton(text='Уголь'),
            #                KeyboardButton(text='Олово'),
            #                KeyboardButton(text='Железо'),
            #
            #            ],
            #            [
            #                KeyboardButton(text='Серебро'),
            #                KeyboardButton(text='Золото'),
            #                KeyboardButton(text='Платина'),
            #            ],
            [
            #                KeyboardButton(text='Палладий'),
                KeyboardButton(text='💵Продать всё'),
                KeyboardButton(text='🔙Назад')
            ]
        ]
    )
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

@dp.message_handler('🧾Курс')
async def info_course(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    course = Courses.get()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    await message.answer(text=
        f'\n🧾Стоимость сырья на продажу: {money:.2f}$\n'
        f'<b>📊Курс на данный момент (за 100 шт.) - </b>'
        f'\n⬛️Уголь - {course.coal * 100:.5f}'
        f'\n🟧Олово - {course.tin * 100:.5f}'
        f'\n⬜️Железо - {course.iron * 100:.5f}'
        f'\n⬜️Серебро - {course.silver * 100:.5f}'
        f'\n🟨Золото - {course.aurum * 100:.5f}'
        f'\n🟥Платина - {course.platinum * 100:.5f}'
        f'\n🟦Палладий - {course.palladium * 100:.5f}'
    )


@dp.message_handler(text='💱Конвертировать')
async def converter(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    course = Courses.get()
    miner.work_id_converter = False
    miner.save()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    await message.answer(text=f'Вас приветствует биржа руд и ценных бумаг.\nРабота в шахтах <b>приостановлена</b>.'
                              f'\n🧾Стоимость сырья на продажу: {money:.2f}$\n'
                              f'<b>📊Из них - </b>'
                              f'\n⬛️Уголь - {coal(miner.coal, course.coal)}'
                              f'\n🟧Олово - {tin(miner.tin, course.tin)}'
                              f'\n⬜️Железо - {iron(miner.iron, course.iron)}'
                              f'\n⬜️Серебро - {silver(miner.silver, course.silver)}'
                              f'\n🟨Золото - {aurum(miner.aurum, course.aurum)}'
                              f'\n🟥Платина - {platinum(miner.platinum, course.platinum)}'
                              f'\n🟦Палладий - {palladium(miner.palladium, course.palladium)}',
                         reply_markup=sellkeyboard(message.from_user.id))


@dp.message_handler(text='🔙Назад')
async def back(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    miner.work_id_converter = True
    miner.save()
    await message.answer(text='Возвращаемся в офис. Работа в шахтах возобновилась', reply_markup=menu)


@dp.message_handler(text='💵Продать всё')
async def sell(message: types.Message):
    course = Courses.get()
    miner = Miner.get(minerid=message.from_user.id)
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    miner.balance += money
    miner.coal, miner.tin, miner.iron, miner.silver, miner.aurum, miner.platinum, miner.palladium = 0, 0, 0, 0, 0, 0, 0
    miner.work_id_converter = True
    miner.save()
    await message.answer(text=f'📈Сделка прошла успешно! Вы продали всё, работа <b>возобновлена</b>.'
                              f'\n💰Баланс сейчас: {miner.balance:.2f}$', reply_markup=menu)


@dp.message_handler(Command('reset_courses'))
async def reset(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    if miner.minerid in admins:
        course = Courses.get()
        course.coal, course.tin, course.iron, course.silver, course.aurum, course.platinum, course.palladium = 0.001, 0.005, 0.03, 0.1, 5.0, 8.5, 18.9
        course.save()
        await message.reply(text='Курс валюты сброшен до значения default')
