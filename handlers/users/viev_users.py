from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import admins
from data.peewee import Miner
from loader import dp


@dp.message_handler(Command('users'))
async def users(message: types.Message):
    mineradm = Miner.get(minerid=message.from_user.id)
    ans = 'Юзеры бота'
    if mineradm.minerid in admins:
        for gamer in Miner.select():
            miner = Miner.get(minerid=gamer.minerid)
            mines = miner.mines1 + miner.mines2 + miner.mines3 + miner.mines4
            miners = miner.minerstype1 + miner.minerstype2 + miner.minerstype3 + miner.minerstype4
            ans += '\n\n@' + str(miner.username) + ', id: ' + str(miner.minerid) + ', деньги: ' \
                   + str(miner.balance.__round__(2)) + \
                   ', расход $/мин: ' + str((miner.expenses / 60).__round__(2)) + ', шахты: ' + str(mines) \
                   + ', шахтёры: ' + str(miners)
        await message.answer_sticker(sticker='CAACAgIAAxkBAAECxjFhHfrG3chMiIpBl6GjdIm47OcCxAACmgADObZ9OR3fkdWjbQ9fIAQ')
        await message.answer(text=ans)
