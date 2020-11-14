import time
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Contact, Location
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from buttons import *
from db import *
from classes import Users


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
users = {}


@dp.message_handler(commands=['start'])
async def hello(msg: types.Message):
    await bot.send_message(msg.from_user.id, f"Hello {msg.from_user.first_name}!", reply_markup=menu_btns)
    global id_
    id_ = msg.from_user.id
    users[id_] = Users(f'{id_}')


@dp.message_handler(content_types=['photo'])
async def get_photo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Фото сохранено в базу')


@dp.message_handler()
async def func_menu(msg: types.Message):
    if msg.text == 'Меню':
        await bot.send_photo(msg.from_user.id, first ,  'Гамбургер с курицей', reply_markup=btns1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, second, 'Гамбургер с говядиной', reply_markup=btns2)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, third, 'Gipper Burger', reply_markup=btns3)
    elif msg.text == 'Корзина':
        await bot.send_message(msg.from_user.id, 'Ваша корзина: ')
        for element in users[id_]:
            await bot.send_message(msg.from_user.id, element)


@dp.callback_query_handler()
async def show_description(call: types.CallbackQuery):
    msg = call.data
    if msg == 'desc1':
        await bot.send_message(call.from_user.id, first_text )
    elif msg == 'desc2':
        await bot.send_message(call.from_user.id, second_text)
    elif msg == 'desc3':
        await bot.send_message(call.from_user.id, third_text)

    elif msg == 'add1':
        users[id_].append('Гамбургер с курицей')
    elif msg == 'add2':
        users[id_].append('Гамбургер с говядиной')
    elif msg == 'add3':
        users[id_].append('Gipper Burger')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

