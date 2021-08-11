from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from data.peewee import Miner
from keyboards.default.menu_keyboard import menu
from loader import dp

@dp.callback_query_handler(text='menu')
async def menu(call: CallbackQuery):
    await call.message.answer('Хорошо, переключаю тебя на панель управления', reply_markup=menu)

@dp.callback_query_handler(text='training')
async def training(call: CallbackQuery):
    pickaxe = ReplyKeyboardMarkup(        keyboard= [[
        KeyboardButton(text=' ⛏ ')
        ]]
    )
    await call.message.answer('Итак, эта игра про бизнес. Здесь ты строишь шахты, нанимаешь шахтёров на свою работу.'
                              '\nПосмотреть своё имущество можно, нажав в меню на кнопку <b>⛏Добыча</b>'
                              '\nНажми на кирку, чтобы перейти дальше', reply_markup=pickaxe)

@dp.message_handler(text=' ⛏ ')
async def training(message: types.Message):
    shoplite = ReplyKeyboardMarkup(
        keyboard= [[
        KeyboardButton(text=' 🛒 ')
        ]]
    )
    await message.answer('Каждая шахта обладает определёнными рудами'
                              '\nКаждый шахтёр обладает собственными характеристиками добычи'
                              '\nНажми на кнопку "🛒", чтобы перейти дальше', reply_markup=shoplite)

@dp.message_handler(text=' 🛒 ')
async def training(message: types.Message):
    last = ReplyKeyboardMarkup(
        keyboard= [[
        KeyboardButton(text=' 👷‍♂️ ')
        ]]
    )
    await message.answer('В магазине всё это дело можно приобрести. Перед тобой 2 кнопки - "Шахты" и "Шахтёры"'
                              '\nПриобретать что-либо тебе сейчас необязательно. У тебя уже есть одна '
                              '<b>Небольшая шахта</b>, на которой трудятся 2 <b>Шахтёра-Новичка</b>'
                              '\nНажми на кнопку "👷‍♂️", чтобы перейти дальше', reply_markup=last)

@dp.message_handler(text=' 👷‍♂️ ')
async def training(message: types.Message):
    await message.answer('В целом, основные азы игры ты уже прошёл. Осталось уточнить момент, что шахтёры сами добывают '
                         'руду без твоего участия. Однако, раз в час каждый просит оплату в соответствии со своей '
                         'квалификацией. Нужно понимать, что добытая ими руда не конвертируется в деньги сразу, ты, как '
                         'главный продажник, должен самостоятельно продавать свой товар (это можно сделать, нажав в меню '
                         'кнопку <b>💱Конвертировать</b>. Если денег перестанет хватать на '
                         'обслуживание персонала, то он устроит забастовку и тупо перестанет работать. Но не переживай,'
                         'если такое случится, то я пришлю весточку. Приятных сделок!', reply_markup=menu)