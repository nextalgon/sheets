from datetime import date
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests


class Prixod(StatesGroup):
    type = State()


class BrandingSmm(StatesGroup):
    name = State()
    type_money = State()
    money = State()
    sog = State()


class Web(StatesGroup):
    category = State()


class Rasxod(StatesGroup):
    type = State()
    money_type = State()
    money = State()
    sog = State()
    name_of = State()


def month_branding():
    month = date.today().strftime('%m/%Y') + 'branding'
    return month


def month_smm():
    month = date.today().strftime('%m/%Y') + 'smm'
    return month


def month_web():
    month = date.today().strftime('%m/%Y') + 'web'
    return month


def month_obed():
    month = date.today().strftime('%m/%Y') + 'obed'
    return month


def month_oylik():
    month = date.today().strftime('%m/%Y') + 'oylik'
    return month


def month_boshqa():
    month = date.today().strftime('%m/%Y') + 'boshqa'
    return month


def get_date():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1


def get_currency():
    url = "https://currency-exchange.p.rapidapi.com/exchange"
    querystring = {"from": "USD", "to": "UZS", "q": "1.0"}
    headers = {
        'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
        'x-rapidapi-key': "b0164644e4msh4d52f68b8f1a8dfp156ab1jsnfe8aff1a64c7"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
