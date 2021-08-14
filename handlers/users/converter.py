from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from data.config import admins
from data.peewee import Miner, Courses
from keyboards.default.menu_keyboard import menu
from loader import dp


def sellkeyboard(minerid):
    miner = Miner.get(minerid=minerid)
    coalprice, tinprice, ironprice = miner.coal * 0.6 / 1000, miner.tin * 1 / 1000, miner.iron * 15 / 1000
    silverprice, aurumprice, platinumprice, palladiumprice = miner.silver * 790 / 1000, miner.aurum * 58293 / 1000, miner.platinum * 32715 / 1000, miner.palladium * 89100 / 1000
    allprice = round(coalprice + tinprice + ironprice + silverprice + aurumprice + platinumprice + palladiumprice, 5)
    allprice = str(allprice)
    coalprice, tinprice, ironprice = str(coalprice), str(tinprice), str(ironprice)
    silverprice, aurumprice, platinumprice, palladiumprice = str(silverprice), str(aurumprice), str(platinumprice), str(
        palladiumprice)
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
                KeyboardButton(text='Продать всё'),
                KeyboardButton(text='Назад')
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


@dp.message_handler(text='💱Конвертировать')
async def converter(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    course = Courses.get()
    miner.work_id_converter = False
    miner.save()
    money = coal(miner.coal, course.coal) + tin(miner.tin, course.tin) + iron(miner.iron, course.iron) \
            + silver(miner.silver, course.silver) + aurum(miner.aurum, course.aurum) \
            + platinum(miner.platinum, course.platinum) + palladium(miner.palladium, course.palladium)
    await message.answer(text=f'Вас приветствует биржа руд и ценных бумаг. Работа в шахтах приостановлена.'
                              f'\nСтоимость сырья на продажу: {money:.2f}$\n'
                              f'<b>Курс на данный момент (за 100 шт.) - </b>'
                              f'\nУголь - {course.coal * 100:.5f}'
                              f'\nОлово - {course.tin * 100:.5f}'
                              f'\nЖелезо - {course.iron * 100:.5f}'
                              f'\nСеребро - {course.silver * 100:.5f}'
                              f'\nЗолото - {course.aurum * 100:.5f}'
                              f'\nПлатина - {course.platinum * 100:.5f}'
                              f'\nПалладий - {course.palladium * 100:.5f}',
                         reply_markup=sellkeyboard(message.from_user.id))


@dp.message_handler(text='Назад')
async def back(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    miner.work_id_converter = True
    miner.save()
    await message.answer(text='Возвращаемся в офис. Работа в шахтах возобновилась', reply_markup=menu)


@dp.message_handler(text='Продать всё')
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
    await message.answer(text=f'Сделка прошла успешно! Вы продали всё, работа возобновлена. '
                              f'Баланс сейчас: {miner.balance:.2f}$', reply_markup=menu)


@dp.message_handler(Command('reset_courses'))
async def reset(message: types.Message):
    miner = Miner.get(minerid=message.from_user.id)
    if miner.minerid in admins:
        course = Courses.get()
        course.coal, course.tin, course.iron, course.silver, course.aurum, course.platinum, course.palladium = 0.001, 0.005, 0.03, 0.1, 5.0, 8.5, 18.9
        course.save()
        await message.reply(text='Курс валюты сброшен до значения default')
