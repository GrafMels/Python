#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5689050348:AAH9oTEncFOVIIFd-_wkCKs9HRoObufkiXA')
dp = Dispatcher(bot, storage = storage)