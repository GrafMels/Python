# Cюда все функции отправляющие сообщения

from aiogram import types
from bot import bot
import os

import model


async def greetings(message: types.Message): 
    system_id = model.user_id_seach(message.from_user.id)
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки')
    await bot.send_message(message.from_user.id,
                           'В банке 150 конфет. За один ход возьми от 1 до 28 конфет включительно.\n'
                           f'Тот кто Возьмёт последнюю конфету проиграет')
    model.total_count[system_id] = 150
    model.max_turn = 1
    model.bot_move, model.sequence = model.first_move()
    if model.sequence == 1:
        await bot.send_message(message.from_user.id, 'Ты ходишь первый')
    else:
        await bot.send_message(message.from_user.id, 'Бот ходит первый')
    
        
    
async def bye_bye(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'до свидания!')
    

async def cheat(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ах, ты грязный читер!')

async def work_space(message: types.Message, My_candies, Bot_candies, In_Total):
    await bot.send_message(message.from_user.id, f'Вы взяли {My_candies} конфет!')
    await bot.send_message(message.from_user.id, f'Бот взял {Bot_candies} конфет!')
    await bot.send_message(message.from_user.id, f'В банке {In_Total} конфет!')

async def work_space_lose(message: types.Message, My_candies, Bot_candies, In_Total):
    await bot.send_message(message.from_user.id, f'Вы взяли {My_candies} конфет!')
    await bot.send_message(message.from_user.id, f'Бот взял {Bot_candies} конфет!')
    await bot.send_message(message.from_user.id, f'В банке {In_Total} конфет!')
    await bot.send_message(message.from_user.id, f'Ты решил играть со мной? Ошибка!')
    await bot.send_message(message.from_user.id, f'Ты выбрал не верную комбинацию? Фатальная ошибка!')
    
async def lose(message: types.Message):
    
    await bot.send_message(message.from_user.id, 'Ты проиграл. ИИ победил!')
    adress = str(os.path.abspath('II.jpg'))
    photo = open(f'{adress}', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    
async def bot_lose(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ты победил! Востание машин отменяется!')
    adress = str(os.path.abspath('Human.jpg'))
    photo = open(f'{adress}', 'rb')
    await bot.send_photo(message.from_user.id, photo)

async def no_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ты ещё не начал игру зачем тебе вводить число?\nВведите /start если хотите начать.')
    
async def lacks(message: types.Message):
    await bot.send_message(message.from_user.id, 'В банке меньше конфет чем ты ввёл. Введи снова.')
    
async def except_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите /help для получения списка команд.')

async def help(message: types.Message):
    await bot.send_message(message.from_user.id, '/start - начинает игру \n/finish - заканчивает игру \nВ самой игре можно вводить любые числа от 1 до 28')
    
async def end_game(message: types.Message):
    match model.angry_bot:
        case 0:
            await bot.send_message(message.from_user.id, 'Игра же уже закончена. Не пиши больше цифр')
        case 1:
            await bot.send_message(message.from_user.id, 'Я же попросил не пиши')
        case 2:
            await bot.send_message(message.from_user.id, 'Shut up and listen to me stupid mazafaka.')
            await bot.send_message(message.from_user.id, 'НЕ')
            await bot.send_message(message.from_user.id, 'ПИШИ')
            await bot.send_message(message.from_user.id, 'БОЛЬШЕ')
            await bot.send_message(message.from_user.id, 'ЦИФРЫ')
        case 3:
            await bot.send_message(message.from_user.id, 'Ладно пофиг я спать, оставляю вместо себя бота.')
            await bot.send_message(message.from_user.id, 'Нажмите /start для продолжения')
        case _:
            await bot.send_message(message.from_user.id, 'Нажмите /start для продолжения')
    
    model.angry_bot = model.angry_bot + 1