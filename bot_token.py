from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = 'your token'

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
