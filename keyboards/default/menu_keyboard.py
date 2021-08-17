from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⛏Добыча'),
            KeyboardButton(text='🛒Магазин'),
        ],
        [
            KeyboardButton('💱Конвертировать'),
            KeyboardButton(text='😇Создатель'),
        ],
        [
            KeyboardButton(text='💳Донат&Вывод'),
            KeyboardButton(text='⚙️Настройки')
        ],
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