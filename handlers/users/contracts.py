import random

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton

from data.peewee import Miner, Courses
from keyboards.default.menu_keyboard import menu
from loader import dp

def get_contracts():
    contract = {}
    ores = ['Уголь', 'Олово', 'Железо', 'Серебро', 'Платина', 'Палладий']
    ore1, ore2, ore3 = random.choice(ores), random.choice(ores), random.choice(ores)
    quantity1, quantity2, quantity3 = random.randint(1, 100000), random.randint(1, 100000), random.randint(1, 100000)

    if ore1 == ore2 == ore3:
        quantity123 = quantity1 + quantity2 + quantity3
        contract = {
            ore1: quantity123
        }

    elif ore1 == ore2:
        quantity12 = quantity1 + quantity2
        contract = {
            ore1: quantity12,
            ore3: quantity3
        }

    elif ore1 == ore3:
        quantity13 = quantity1 + quantity3
        contract = {
            ore1: quantity13,
            ore2: quantity2
        }

    elif ore2 == ore3:
        quantity23 = quantity2 + quantity3
        contract = {
            ore1: quantity1,
            ore2: quantity23
        }

    elif ore1 != ore2 != ore3:
        contract = {
            ore1: quantity1,
            ore2: quantity2,
            ore3: quantity3,
        }

    return contract
