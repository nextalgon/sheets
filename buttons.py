from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def start_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('Prixod')
    btn2 = KeyboardButton('Rasxod')
    markup.add(btn1, btn2)
    return markup


def prixod():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('BRANDING')
    btn2 = KeyboardButton('SMM')
    btn3 = KeyboardButton("WEB")
    markup.add(btn1, btn2, btn3)
    return markup

def type_money():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    btn1 = KeyboardButton('USD')
    btn2 = KeyboardButton('SO\'M')
    markup.add(btn1, btn2)
    return markup


def soglasheniya():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    btn1 = KeyboardButton('Ha')
    btn2 = KeyboardButton('Yoq')
    markup.add(btn1, btn2)
    return markup


def rasxod():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('obed')
    btn2 = KeyboardButton('oylik')
    btn3 = KeyboardButton('boshqa')
    markup.add(btn1, btn2, btn3)
    return markup


def web():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('UI-UX')
    btn2 = KeyboardButton('Backend')
    btn3 = KeyboardButton("Frontend")
    markup.add(btn1, btn2, btn3)
    return markup
