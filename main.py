import time
import logging
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Contact, Location
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN, ID
from buttons import *
from classes import Users, States_
from database import dbase


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
users = {}


@dp.message_handler(commands=['start'],state='*')
async def hello(msg: types.Message):
    if msg.from_user.id == ID:
        await bot.send_message(msg.from_user.id, f"Привет Админ!!", reply_markup=admin_buttons)
    else:
        await bot.send_message(msg.from_user.id, f"Привет {msg.from_user.first_name}!", reply_markup=menu_btns)
        await States_.state_menu.set()
        global id_
        id_ = msg.from_user.id
        users[id_] = Users(f'{id_}')


@dp.message_handler(content_types=['photo'])
async def add_photo(msg: types.Message):
    if msg.from_user.id == ID:
        await bot.send_message(msg.from_user.id, 'Фото сохранено в базу, введите назваеие этого фото.')
        print(msg.photo[-1].file_id)
        global photo_id
        photo_id = msg.photo[-1].file_id


@dp.message_handler()
async def add_name(msg: types.Message):
    if msg.from_user.id == ID:
        name = msg.text
        dbase.add_image(photo_id, name)


@dp.message_handler(text=emojize('Меню :book:'), state=States_.state_menu)
@dp.message_handler(text=emojize("Контакты :blue_book:"), state=States_.state_menu)
@dp.message_handler(text=emojize('Оплата :dollar:'), state=States_.state_menu)
@dp.message_handler(text=emojize('В главное меню :arrow_left:'), state='*')
async def main_menu(msg: types.Message, state: FSMContext):
    if 'Меню' in msg.text:
        await bot.send_message(msg.from_user.id, "выберите категорию", reply_markup=menu_categories)
        await States_.state_categories.set()


    elif "Оплата" in msg.text:
        await bot.send_message(msg.from_user.id, 'Выберите способ оплаты', reply_markup=payments)

    elif "Контакты" in msg.text:
        await bot.send_message(msg.from_user.id, 'мы находимся там то там то,\nнаш номер такой то')

    elif "главное" in msg.text:
        await bot.send_message(msg.from_user.id, 'Главное меню', reply_markup=menu_btns)


@dp.message_handler(text=emojize('Корзина :shopping_cart:'), state='*')
async def show_cart(msg: types.Message):
    if 'Корзина' in msg.text:
        await bot.send_message(msg.from_user.id, 'Если вы хотите удалить что то из корзины, просто пришлите название.\n'
                                                 'Ваша корзина: ')
        for element in users[id_]:
            await bot.send_message(msg.from_user.id, element)
        await States_.state_cart.set()


@dp.message_handler( state=States_.state_cart)
async def edit_cart(msg: types.Message, state: FSMContext):
    try:
        del_item = msg.text
        users[id_].remove(del_item)
        await bot.send_message(msg.from_user.id, "Удалил", reply_markup=cart_btns)
    except Exception as ex:
        print(ex)
        await bot.send_message(msg.from_user.id, f"{ex}")


@dp.message_handler(text=emojize('Бургеры :hamburger:'), state=States_.state_categories)
@dp.message_handler(text=emojize("Пицца :pizza:"), state=States_.state_categories)
@dp.message_handler(text=emojize('Десерты :cake:'), state=States_.state_categories)
@dp.message_handler(text=emojize('Напитки :tropical_drink:'), state=States_.state_categories)
async def categories_menu(msg: types.Message, state: FSMContext):
    objects = []

    for i in dbase.get_object():
        objects.append((i[1], i[0]))
    objects = dict(objects)
    if 'Бургеры' in msg.text:
        await bot.send_photo(msg.from_user.id, objects['chicken burger'],  'Гамбургер с курицей', reply_markup=burg1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, objects['burger'], 'Гамбургер с говядиной', reply_markup=burg2)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, objects['gipper burger'], 'Gipper Burger', reply_markup=burg3)

    elif 'Пицца' in msg.text:
        await bot.send_photo(msg.from_user.id, objects["pizza1"], 'Пицца 1', reply_markup=pizza1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, objects["pizza2"], 'Пицца 2', reply_markup=pizza2)

    elif 'Напитки' in msg.text:
        await bot.send_photo(msg.from_user.id, objects["cola"], 'Coca Cola', reply_markup=pizza1)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, objects["pepsi"], 'Pepsi Cola', reply_markup=pizza2)
        time.sleep(1)
        await bot.send_photo(msg.from_user.id, objects["redbull"], 'Red Bull', reply_markup=pizza1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)