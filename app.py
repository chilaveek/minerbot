import random

from data import config
from data.peewee import Miner, Courses
from utils.set_bot_commands import set_default_commands
import asyncio

async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    Miner.create_table()
    Courses.get_or_create()

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)

    for gamer in Miner.select():
        bot = Bot(config.BOT_TOKEN)
        miner = Miner.get(minerid=gamer.minerid)
        miner.balance += miner.expenses
        miner.save()
        await bot.send_message(chat_id=gamer.minerid, text='Бот был перезапущен из-за тех.причин')






async def work():
    while True:
        bot = Bot(config.BOT_TOKEN)
        for gamer in Miner.select():
            miner = Miner.get(minerid=gamer.minerid)
            if miner.work_id_expenses is True and miner.work_id_converter is True:
                miner.coal += 3 * miner.minerstype1
                miner.tin += 2 * miner.minerstype1 + 3 * miner.minerstype2
                miner.iron += 1 * miner.minerstype1 + 2 * miner.minerstype2 + 3 * miner.minerstype3
                miner.silver += 1 * miner.minerstype2 + 2 * miner.minerstype3
                miner.aurum += 1 * miner.minerstype3 + 3 * miner.minerstype4
                miner.platinum += 2 * miner.minerstype4
                miner.palladium += 1 * miner.minerstype4
                miner.save()

        await asyncio.sleep(delay=1)


async def pay():
    while True:
        bot = Bot(config.BOT_TOKEN)
        for gamer in Miner.select():
            miner = Miner.get(minerid=gamer.minerid)
            if miner.balance >= miner.expenses:
                miner.work_id_expenses = True
                miner.balance -= miner.expenses

                miner.save()
            else:
                miner.work_id_expenses = False
                miner.save()
                await bot.send_message(chat_id=miner.minerid,
                    text='Шахтёры взбунтовались! Нескольким не пришла ЗП, все устроили забастовку. Срочно вернитесь!')
        await asyncio.sleep(delay=3600)

def check_course(course, default_price):
    changer = 0
    if course < default_price:
        if course <= 0.6 * default_price:
            changer = course * random.randint(-3, 35) * 0.01
        elif course <= 0.7 * default_price:
            changer = course * random.randint(-5, 25) * 0.01
        elif course <= 0.8 * default_price:
            changer = course * random.randint(-10, 20) * 0.01
        elif course <= 0.9 * default_price:
            changer = course * random.randint(-17, 20) * 0.01
        elif course <= 0.99 * default_price:
            changer = course * random.randint(-19, 20) * 0.01

    elif course == default_price:
        changer = course * random.randint(-30, 30) * 0.01

    elif course > default_price:
        if course >= 1.4 * default_price:
            changer = course * random.randint(-30, 3) * 0.01
        elif course >= 1.3 * default_price:
            changer = course * random.randint(-20, 10) * 0.01
        elif course >= 1.2 * default_price:
            changer = course * random.randint(-20, 14) * 0.01
        elif course >= 1.1 * default_price:
            changer = course * random.randint(-20, 17) * 0.01
        elif course >= 1.01 * default_price:
            changer = course * random.randint(-20, 19) * 0.01
    return changer



async def change_courses():
    while True:
        bot = Bot(config.BOT_TOKEN)

        for course in Courses.select():
            course = Courses.get(id=1)
            course.coal += check_course(course.coal, 0.001)
            course.tin += check_course(course.tin, 0.005)
            course.iron += check_course(course.iron, 0.03)
            course.silver += check_course(course.silver, 0.1)
            course.aurum += check_course(course.aurum, 5.0)
            course.platinum += check_course(course.platinum, 8.5)
            course.palladium += check_course(course.palladium, 18.9)
            course.save()
        await asyncio.sleep(delay=1800)

async def check_work_id():
    while True:
        for gamer in Miner.select():
            miner = Miner.get(minerid=gamer.minerid)
            if miner.balance >= miner.expenses:
                miner.work_id_expenses = True
                miner.save()
            elif miner.balance < miner.expenses:
                miner.work_id_expenses = False
                miner.save()

        await asyncio.sleep(5)

if __name__ == '__main__':
    from aiogram import executor, Bot
    from handlers import dp

    loop1 = asyncio.get_event_loop()
    loop2 = asyncio.get_event_loop()
    loop3 = asyncio.get_event_loop()
    loop4 = asyncio.get_event_loop()

    loop1.create_task(work())
    loop2.create_task(pay())
    loop3.create_task(change_courses())
    loop4.create_task(check_work_id())

    executor.start_polling(dp, on_startup=on_startup)
