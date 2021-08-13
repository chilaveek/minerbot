import random

from data import config
from data.peewee import Miner, Courses
from utils.set_bot_commands import set_default_commands
import asyncio
from change import changes

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
        miner = Miner.get(minerid=gamer.miner)
        miner.balance += miner.expenses
        miner.save()
        await bot.send_message(chat_id=gamer.minerid, text='Бот был перезапущен из-за тех.причин\n' + changes)






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


async def change_coorses():
    while True:
        bot = Bot(config.BOT_TOKEN)

        for course in Courses.select():
            course = Courses.get(id=1)
            course.coal += course.coal * random.randrange(-5, 5, 1) * 0.1
            course.tin += course.tin * random.randrange(-5, 5, 1) * 0.1
            course.iron += course.iron * random.randrange(-5, 5, 1) * 0.1
            course.silver += course.silver * random.randrange(-5, 5, 1) * 0.1
            course.aurum += course.aurum * random.randrange(-5, 5, 1) * 0.1
            course.platinum += course.platinum * random.randrange(-5, 5, 1) * 0.1
            course.palladium += course.palladium * random.randrange(-5, 5, 1) * 0.1
            course.save()
        await asyncio.sleep(delay=3600)


if __name__ == '__main__':
    from aiogram import executor, Bot
    from handlers import dp

    loop1 = asyncio.get_event_loop()
    loop2 = asyncio.get_event_loop()
    loop3 = asyncio.get_event_loop()
    loop1.create_task(work())
    loop2.create_task(pay())
    loop3.create_task(change_coorses())

    executor.start_polling(dp, on_startup=on_startup)
