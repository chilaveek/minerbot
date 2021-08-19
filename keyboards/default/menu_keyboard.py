from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⛏ Добыча'),
            KeyboardButton(text='🛒 Магазин'),
        ],
        [
            KeyboardButton('🏦 Банк'),
            KeyboardButton(text='😇 Создатель'),
        ],
        [
            KeyboardButton(text='💳 Донат&Вывод'),
            KeyboardButton(text='⚙️ Настройки')
        ],
    ],

    resize_keyboard=True
)

bank_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💱 Рынок руд'),
            KeyboardButton(text='💵 Вклады'),
            KeyboardButton(text='📃 Контракты'),
        ],
        [
            KeyboardButton(text='🔙Назад'),
        ]
    ],
    resize_keyboard=True
)

pickaxe = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='⛏')
        ]
    ]
)
shoplite = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🛒')
        ]
    ]
)
last = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard= [
            [
                KeyboardButton(text='👷‍♂️')
            ]
        ]
    )