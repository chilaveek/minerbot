from aiogram import types
from aiogram.dispatcher.filters import Command

from data.peewee import db
from keyboards.default.menu_keyboard import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.reply('⬇Выберите, что хотите сделать⬇', reply_markup=menu)

