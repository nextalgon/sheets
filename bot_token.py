from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = '1990773412:AAGuJ2sCb16TCuAkg4K2k8s3sod4uYC16Xw'

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
