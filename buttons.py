from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize

back_to_menu = KeyboardButton(emojize('В главное меню :arrow_left:'))
menu = KeyboardButton(emojize('Меню :book:'))
cart = KeyboardButton(emojize('Корзина :shopping_cart:'))
contacts = KeyboardButton(emojize("Контакты :blue_book:"))
payment = KeyboardButton(emojize('Оплата :dollar:'))
add_img = KeyboardButton(emojize('Добавить фото :framed_picture:'))
menu_btns = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).row(
    menu, cart).row(contacts, payment)
admin_buttons = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2).row(
    menu, cart).row(contacts, payment).add(add_img)

del_item = KeyboardButton('Редактировать корзину')
cart_btns = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(cart, del_item, back_to_menu)

cash_payment = KeyboardButton(emojize('Оплата наличными :dollar:'))
card_payment = KeyboardButton(emojize('Оплата картой :credit_card:'))
payments = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row(card_payment, cash_payment)

burgers = KeyboardButton(emojize('Бургеры :hamburger:'))
drinks = KeyboardButton(emojize('Напитки :tropical_drink:'))
pizza = KeyboardButton(emojize("Пицца :pizza:"))
desserts = KeyboardButton(emojize('Десерты :cake:'))
back_to_menu = KeyboardButton(emojize('В главное меню :arrow_left:'))
menu_categories = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row(burgers, pizza).row(
    desserts, drinks).add(back_to_menu, cart)



add_to_cart1 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add1')
description1 = InlineKeyboardButton(text='подробнее', callback_data='desc1')
burg1 = InlineKeyboardMarkup(row_width=2).row(add_to_cart1, description1)

add_to_cart2 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add2')
description2 = InlineKeyboardButton(text='подробнее', callback_data='desc2')
burg2 = InlineKeyboardMarkup(row_width=2).row(add_to_cart2, description2)

add_to_cart3 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add3')
description3 = InlineKeyboardButton(text='подробнее', callback_data='desc3')
burg3 = InlineKeyboardMarkup(row_width=2).row(add_to_cart3, description3)


add_pizza_cart1 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add_p1')
desc_pizza1 = InlineKeyboardButton(text='подробнее', callback_data='desc_p1')
pizza1 = InlineKeyboardMarkup(row_width=2).row(add_pizza_cart1, desc_pizza1)

add_pizza_cart2 = InlineKeyboardButton(text='Добавить в корзину', callback_data='add_p2')
desc_pizza2 = InlineKeyboardButton(text='подробнее', callback_data='desc_p2')
pizza2 = InlineKeyboardMarkup(row_width=2).row(add_pizza_cart2, desc_pizza2)