from aiogram import types
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp

def donate_kb():
    buttons = [
        InlineKeyboardButton(text='Пожертвование', callback_data='donate'),
    ]
    kb = InlineKeyboardMarkup(row_width=2).add(*buttons)
    return kb

@dp.message_handler(text='💳 С наилучшими пожеланиями...')
async def donate_show(message: types.Message):
    await message.answer(text='✋Добро Пожаловать!\nЭтот раздел создан для тех, кто хочет поддержать проект.',
                         reply_markup=donate_kb())

@dp.callback_query_handler(text='donate')
async def donate(call: CallbackQuery):
    await call.message.edit_text('Этот проект лично мой и делался на собственной инициативе. Можете пожертвовать любую '
                                 'сумму вашему покорному слуге для дальнейшего развития. Спасибо.'
                                 '\nhttps://www.donationalerts.com/r/chilaveek')

