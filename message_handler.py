from bot_token import bot, dp
from funcks import Prixod, Rasxod, BrandingSmm, get_date, Web, get_currency, month_branding, month_smm, \
    month_web, month_obed, month_oylik, month_boshqa
from buttons import type_money, soglasheniya, rasxod, prixod, web
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
import gspread
from aiogram.dispatcher.filters.builtin import Command

googlesheet_id = '1UIqAqRvjF3qMd2TmGId0rOyM-C5kwlLcmTGOyBFFTrQ'
gc = gspread.service_account('careful-muse-329413-28fa2b71287d.json')
di = {}
sh = gc.open_by_key(googlesheet_id)


@dp.message_handler(Command(commands=['balance']))
async def balan(msg):
    print(msg.message_id)
    li = []
    fe = []
    ke = []
    je = []
    he = []
    me = []
    a = sh.worksheet(str(month_boshqa())).get_values()
    for i in a:
        try:
            li.append(int(i[3]))
        except:
            pass
    a = sh.worksheet(str(month_oylik())).get_values()
    for i in a:
        try:
            fe.append(int(i[3]))
        except:
            pass
    a = sh.worksheet(str(month_branding())).get_values()
    for i in a:
        try:
            ke.append(int(i[3]))
        except:
            pass
    a = sh.worksheet(str(month_smm())).get_values()
    for i in a:
        try:
            je.append(int(i[3]))
        except:
            pass
    a = sh.worksheet(str(month_web())).get_values()
    for i in a:
        try:
            he.append(int(i[4]))
        except:
            pass
    a = sh.worksheet(str(month_obed())).get_values()
    for i in a:
        try:
            me.append(int(i[2]))
        except:
            pass
    await bot.send_message(msg.chat.id, f'Rasxod:\n\nBoshqa: {sum(li)}\nOylik: {sum(li)}\nobed: {sum(me)}\n\nPrixod:\n\nbranding: {sum(ke)}\n'
                                             f'smm: {sum(je)}\nweb: {sum(he)}')


@dp.message_handler()
async def tip(message):
    if message.text == 'Prixod':
        await bot.send_message(message.chat.id, 'Yo\'nalishni tanlang', reply_markup=prixod())
        await Prixod.type.set()
    if message.text == 'Rasxod':
        await bot.send_message(message.chat.id, 'Pul turini tanlang', reply_markup=rasxod())
        await Rasxod.type.set()


@dp.message_handler(state=Prixod.type)
async def money_type(msg):
    di.update({msg.chat.id: [msg.text]})
    if msg.text == 'WEB':
        await bot.send_message(msg.chat.id, 'Kategoriyasini tanlang:', reply_markup=web())
        await Web.category.set()
    elif msg.text == 'BRANDING' or "SMM":
        await bot.send_message(msg.chat.id, 'Pul kimdan kelganini yozing:', reply_markup=ReplyKeyboardRemove())
        await BrandingSmm.name.set()


@dp.message_handler(state=Web.category)
async def name(msg):
    di[msg.chat.id] += [msg.text]
    await bot.send_message(chat_id=msg.chat.id, text='Pul kimdan kelganini yozing:', reply_markup=ReplyKeyboardRemove())
    await BrandingSmm.name.set()


@dp.message_handler(state=BrandingSmm.name)
async def name(msg):
    di[msg.chat.id] += [msg.text]
    await bot.send_message(chat_id=msg.chat.id, text='Pul Turini Tanlang', reply_markup=type_money())
    await BrandingSmm.type_money.set()


@dp.message_handler(state=BrandingSmm.type_money)
async def name(msg):
    di[msg.chat.id] += [msg.text]
    await bot.send_message(chat_id=msg.chat.id, text='Pul summasini kiriting', reply_markup=ReplyKeyboardRemove())
    await BrandingSmm.money.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=BrandingSmm.money)
async def no_money(msg):
    await bot.send_message(msg.chat.id, 'xato, son kiritilishi lozim')


@dp.message_handler(lambda message: message.text.isdigit(), state=BrandingSmm.money)
async def money__(msg):
    if di[msg.chat.id][0] == "WEB":
        if di[msg.chat.id][3] == 'USD':
            m = int(msg.text)
            valy = get_currency()
            valy = float(valy)
            money = m * valy
            money = int(money)
            di[msg.chat.id] += [money]
        else:
            di[msg.chat.id] += [msg.text]
        await bot.send_message(msg.chat.id, f'PRIXOD:\n'
                                            f'Kategoriya: {di.get(msg.chat.id)[0]}\n'
                                            f'Category: {di.get(msg.chat.id)[1]}\n'
                                            f'Kimdan keldi: {di.get(msg.chat.id)[2]}\n'
                                            f'Pul Turi edi: {di.get(msg.chat.id)[3]}\n'
                                            f'Pul summasi: {di.get(msg.chat.id)[4]}\n'
                                            f'sana: {get_date()}\n\n'
                                            f'Kiritilgan ma\'lumotlar to\'g\'ri va bazaga qo\'shilsinmi?',
                               reply_markup=soglasheniya())
    else:
        if di[msg.chat.id][2] == 'USD':
            m = int(msg.text)
            valy = get_currency()
            valy = float(valy)
            money = m * valy
            money = int(money)
            di[msg.chat.id] += [money]

        else:
            di[msg.chat.id] += [msg.text]
        await bot.send_message(msg.chat.id, f'PRIXOD:\n'
                                            f'Kategoriya: {di.get(msg.chat.id)[0]}\n'
                                            f'Kimdan keldi: {di.get(msg.chat.id)[1]}\n'
                                            f'Pul Turi edi: {di.get(msg.chat.id)[2]}\n'
                                            f'Pul summasi: {di.get(msg.chat.id)[3]}\n'
                                            f'sana: {get_date()}\n\n'
                                            f'Kiritilgan ma\'lumotlar to\'g\'ri va bazaga qo\'shilsinmi?',
                               reply_markup=soglasheniya())
    await BrandingSmm.sog.set()


@dp.message_handler(state=BrandingSmm.sog)
async def sog(msg, state: FSMContext):
    if msg.text == 'Ha':

        if di.get(msg.chat.id)[0] == 'BRANDING':
            a, b, c, d = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_branding()}').append_row([get_date(), a, b, d])
            except:
                sh.add_worksheet(title=month_branding(), rows=100, cols=100)
                sh.worksheet(f'{month_branding()}').append_row(['sana', 'Kategoriyasi', 'Qayerdan keldi', 'Pul Summasi'])
                sh.worksheet(f'{month_branding()}').append_row([get_date(), a, b, d])

        elif di.get(msg.chat.id)[0] == 'SMM':
            a, b, c, d = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_smm()}').append_row([get_date(), a, b, d])
            except:
                sh.add_worksheet(title=month_smm(), rows=100, cols=100)
                sh.worksheet(f'{month_smm()}').append_row(['Sana', 'Kategoriyasi', 'Qayerdan keldi', 'Pul Summasi'])
                sh.worksheet(f'{month_smm()}').append_row([get_date(), a, b, d])

        elif di.get(msg.chat.id)[0] == "WEB":
            a, b, c, d, e = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_web()}').append_row([get_date(), a, b, c, e])
            except:
                sh.add_worksheet(title=month_web(), rows=100, cols=100)
                sh.worksheet(f'{month_web()}').append_row(['Sana', 'Kategoriyasi', 'Kategoriya', 'Qayerdan keldi', 'Pul Summasi'])
                sh.worksheet(f'{month_web()}').append_row([get_date(), a, b, c, e])

        await bot.send_message(msg.chat.id, 'qoshildi, yana qoshish uchun /start', reply_markup=ReplyKeyboardRemove())

    else:
        await bot.send_message(msg.chat.id, 'otmena! qoshish uchun /start', reply_markup=ReplyKeyboardRemove())
    await state.finish()
    di.pop(msg.chat.id)


@dp.message_handler(state=Rasxod.type)
async def type__money(msg):
    di.update({msg.chat.id: [msg.text]})
    if msg.text == 'obed':
        await bot.send_message(msg.chat.id, 'Pul Turini tanlang', reply_markup=type_money())
        await Rasxod.money_type.set()

    elif msg.text == 'oylik':
        await bot.send_message(msg.chat.id, 'Oylik oluvchini ismini yozing', reply_markup=ReplyKeyboardRemove())
        await Rasxod.name_of.set()

    elif msg.text == 'boshqa':
        await bot.send_message(msg.chat.id, 'nimaga pul ketti', reply_markup=ReplyKeyboardRemove())
        await Rasxod.name_of.set()


@dp.message_handler(state=Rasxod.name_of)
async def name(msg):
    di[msg.chat.id] += [msg.text]
    await bot.send_message(chat_id=msg.chat.id, text='Pul Turini tanlang', reply_markup=type_money())
    await Rasxod.money_type.set()


@dp.message_handler(state=Rasxod.money_type)
async def name(msg):
    di[msg.chat.id] += [msg.text]
    await bot.send_message(chat_id=msg.chat.id, text='Pul summasini kiriting', reply_markup=ReplyKeyboardRemove())
    await Rasxod.money.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=Rasxod.money)
async def no_money(msg):
    await bot.send_message(msg.chat.id, 'xato, son kiritilishi lozim')


@dp.message_handler(lambda message: message.text.isdigit(), state=Rasxod.money)
async def __money(msg):
    if di[msg.chat.id][0] == 'obed':
        if di[msg.chat.id][1] == "USD":
            m = int(msg.text)
            valy = get_currency()
            valy = float(valy)
            money = m * valy
            money = int(money)
            di[msg.chat.id] += [money]
        else:
            di[msg.chat.id] += [msg.text]
        await bot.send_message(msg.chat.id, f'RASXOD:\n'
                                            f'Kategoriya: {di.get(msg.chat.id)[0]}\n'
                                            f'Pul turi edi: {di.get(msg.chat.id)[1]}\n'
                                            f'Pul summasi: {di.get(msg.chat.id)[2]}\n\n'
                                            f'Kiritilgan ma\'lumotlar to\'g\'ri va bazaga qo\'shilsinmi?',
                               reply_markup=soglasheniya())

    elif di[msg.chat.id][0] == 'oylik' or 'boshqa':
        if di[msg.chat.id][2] == "USD":
            m = int(msg.text)
            valy = get_currency()
            valy = float(valy)
            money = m * valy
            money = int(money)
            di[msg.chat.id] += [money]
        else:
            di[msg.chat.id] += [msg.text]
        if di[msg.chat.id][0] == 'oylik':
            await bot.send_message(msg.chat.id, f'RASXOD:\n'
                                                f'Kategoriya: {di.get(msg.chat.id)[0]}\n'
                                                f'Kimga: {di.get(msg.chat.id)[1]}\n'
                                                f'Pul turi edi: {di.get(msg.chat.id)[2]}\n'
                                                f'Pul summasi: {di.get(msg.chat.id)[3]}\n\n'
                                                f'Kiritilgan ma\'lumotlar to\'g\'ri va bazaga qo\'shilsinmi?',
                                   reply_markup=soglasheniya())
        else:
            await bot.send_message(msg.chat.id, f'RASXOD:\n'
                                                f'Kategoriya: {di.get(msg.chat.id)[0]}\n'
                                                f'qaerga: {di.get(msg.chat.id)[1]}\n'
                                                f'Pul turi edi: {di.get(msg.chat.id)[2]}\n'
                                                f'Pul summasi: {di.get(msg.chat.id)[3]}\n\n'
                                                f'Kiritilgan ma\'lumotlar to\'g\'ri va bazaga qo\'shilsinmi?',
                                   reply_markup=soglasheniya())
    await Rasxod.sog.set()


@dp.message_handler(state=Rasxod.sog)
async def sog(msg, state: FSMContext):
    if msg.text == 'Ha':
        if di.get(msg.chat.id)[0] == 'obed':
            a, b, c = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_obed()}').append_row([get_date(), a, c])
            except:
                sh.add_worksheet(title=month_obed(), rows=100, cols=100)
                sh.worksheet(f'{month_obed()}').append_row(
                    ['sana', 'Kategoriyasi', 'Pul Summasi'])
                sh.worksheet(f'{month_obed()}').append_row([get_date(), a, c])

        elif di.get(msg.chat.id)[0] == 'oylik':
            a, b, c, d = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_oylik()}').append_row([get_date(), a, b, d])
            except:
                sh.add_worksheet(title=month_oylik(), rows=100, cols=100)
                sh.worksheet(f'{month_oylik()}').append_row(['Sana', 'Kategoriyasi', 'Qayerdan keldi', 'Pul Summasi'])
                sh.worksheet(f'{month_oylik()}').append_row([get_date(), a, b, d])

        elif di.get(msg.chat.id)[0] == "boshqa":
            a, b, c, d = di[msg.chat.id]
            try:
                sh.worksheet(f'{month_boshqa()}').append_row([get_date(), a, b, d])
            except:
                sh.add_worksheet(title=str(month_boshqa()), rows=100, cols=100)
                sh.worksheet(f'{month_boshqa()}').append_row(
                    ['Sana', 'Kategoriyasi', 'Qayerga ketdi', 'Pul Summasi'])
                sh.worksheet(f'{month_boshqa()}').append_row([get_date(), a, b, d])

        await bot.send_message(msg.chat.id, 'qoshildi, yana qoshish uchun /start', reply_markup=ReplyKeyboardRemove())

    else:
        await bot.send_message(msg.chat.id, 'otmena! qoshish uchun /start', reply_markup=ReplyKeyboardRemove())
    await state.finish()
    di.pop(msg.chat.id)
