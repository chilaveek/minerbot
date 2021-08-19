from aiogram import types
from aiogram.dispatcher.filters import Command
from peewee import *
import psycopg2
from data import config
from keyboards.default.menu_keyboard import menu
from loader import dp

db = PostgresqlDatabase(
    'miners',
    port=5432,
    user=config.PGUSER,
    password=config.PGPASS,
    host=config.ip)


class Miner(Model):
    id = PrimaryKeyField(primary_key=1)
    username = CharField(null=True)
    minerid = IntegerField()
    work_id_expenses = BooleanField(default=True)
    work_id_converter = BooleanField(default=True)
    minerstype_coal = IntegerField(default=0)
    minerstype1 = IntegerField(default=1)
    minerstype2 = IntegerField(default=0)
    minerstype3 = IntegerField(default=0)
    minerstype4 = IntegerField(default=0)
    mines_coal = IntegerField(default=0)
    mines1 = IntegerField(default=1)
    mines2 = IntegerField(default=0)
    mines3 = IntegerField(default=0)
    mines4 = IntegerField(default=0)
    coal = IntegerField(default=1)
    tin = IntegerField(default=0)
    iron = IntegerField(default=0)
    silver = IntegerField(default=0)
    aurum = IntegerField(default=0)
    platinum = IntegerField(default=0)
    palladium = IntegerField(default=0)
    balance = FloatField(default=100.0)
    expenses = IntegerField(default=50)
    notify_balance = BooleanField(default=True)
    notify_courses = BooleanField(default=False)
    notify_reset = BooleanField(default=False)
    fast_sell = BooleanField(default=False)
    deposit = IntegerField(default=0)
    class Meta:
        database = db


class Courses(Model):
    id = PrimaryKeyField(primary_key=1)
    coal = FloatField(default=0.001)
    tin = FloatField(default=0.005)
    iron = FloatField(default=0.03)
    silver = FloatField(default=0.1)
    aurum = FloatField(default=5.0)
    platinum = FloatField(default=8.5)
    palladium = FloatField(default=18.9)

    class Meta:
        database = db
