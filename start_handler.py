from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from bot_token import dp, bot
from buttons import start_button
import time


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Salom, tanlang', reply_markup=start_button())


