from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
DESTINATION = "C:/Users/User/PycharmProjects/Geek_34_1B_bot/"
