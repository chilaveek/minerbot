from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data.peewee import Miner, db
from keyboards.default.menu_keyboard import menu, pickaxe, shoplite, last
from loader import dp


def training_active():
    buttons = [
        InlineKeyboardButton(text='Да', callback_data='training'),
        InlineKeyboardButton(text='Нет', callback_data='menu'),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def training_field(previous, next):
    buttons = [
        InlineKeyboardButton(text='<', callback_data=previous),
        InlineKeyboardButton(text='>', callback_data=next)
    ]
    kb = InlineKeyboardMarkup(row_width=2).add(*buttons)
    return kb


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    miner = Miner.get_or_create(minerid=message.from_user.id, username=message.from_user.username)
    await message.answer(f'Привет, {message.from_user.full_name}!'
                         f'\nЯ - игровой бот Шахты, зовут Виктор'
                         f'\nНе желаешь пройти обучение?', reply_markup=training_active())


@dp.callback_query_handler(text='menu')
async def menu(call: CallbackQuery):
    await call.message.edit_text('Хорошо, переключаю тебя на панель управления\n---\nВведи /menu чтобы начать')


@dp.callback_query_handler(text='training')
async def training(call: CallbackQuery):
    button = []
    await call.message.edit_text('Итак, эта игра про бизнес. Здесь ты строишь шахты, нанимаешь шахтёров на свою работу.'
                                 '\nПосмотреть своё имущество можно, нажав в меню на кнопку <b>⛏Добыча</b>'
                                 '\n', reply_markup=training_field('👷‍♂️', '⛏1'))


@dp.callback_query_handler(text='⛏1')
async def training(call: CallbackQuery):
    await call.message.edit_text('Каждая шахта обладает определёнными рудами'
                            '\nКаждый шахтёр обладает собственными характеристиками добычи'
                            '\n', reply_markup=training_field('training', '🛒'))


@dp.callback_query_handler(text='🛒')
async def training(call: CallbackQuery):
    await call.message.edit_text('В магазине всё это дело можно приобрести. Перед тобой 2 кнопки - "Шахты" и "Шахтёры"'
                            '\nПриобретать что-либо тебе сейчас необязательно. У тебя уже есть одна '
                            '<b>Небольшая шахта</b>, на которой трудятся 2 <b>Шахтёра-Новичка</b>'
                            '\n',
                            reply_markup=training_field('⛏1', '👷‍♂️'))


@dp.callback_query_handler(text='👷‍♂️')
async def training(call: CallbackQuery):
    await call.message.edit_text(
        'В целом, основные азы игры ты уже прошёл. Осталось уточнить момент, что шахтёры сами добывают '
        'руду без твоего участия. Однако, раз в час каждый просит оплату в соответствии со своей '
        'квалификацией. Нужно понимать, что добытая ими руда не конвертируется в деньги сразу, ты, как '
        'главный продажник, должен самостоятельно продавать свой товар (это можно сделать, нажав в меню '
        'кнопку <b>💱Конвертировать</b>. Если денег перестанет хватать на '
        'обслуживание персонала, то он устроит забастовку и тупо перестанет работать. Но не переживай,'
        'если такое случится, то я пришлю весточку. Приятных сделок!\n---\n'
        'Введите команду /menu , чтобы начать играть', reply_markup=training_field('🛒', 'training'))
