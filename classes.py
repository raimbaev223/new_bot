from aiogram.dispatcher.filters.state import State, StatesGroup


class Users(list):
    cart = []

    def __init__(self, cart):
        self.cart = cart

    def __str__(self):
        return f'Корзина: {self.cart}'

class States_(StatesGroup):
    state_menu = State()
    state_categories = State()
    state_cart = State()