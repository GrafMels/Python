# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types
from aiogram.dispatcher import FSMContext

import view
import model
from bot import bot

switch_crutch = 0

async def help(message: types.Message,  state=FSMContext):
    await view.help(message)


async def start(message: types.Message,  state=FSMContext):
    system_id = model.user_id_seach(message.from_user.id)
    await view.greetings(message)
    if model.sequence == 0:
        model.total_count[system_id] = model.total_count[system_id] - model.bot_move
        await bot.send_message(message.from_user.id, model.total_count[system_id])
        
        

   
async def finish(message: types.Message,  state=FSMContext):
    system_id = model.user_id_seach(message.from_user.id)
    await view.bye_bye(message)
    model.max_turn = 0
    model.total_count[system_id] = 150



async def getMessage(message: types.Message,  state=FSMContext):
    system_id = model.user_id_seach(message.from_user.id)
    x = 0
    number = message.text
    
    try:
        number = int(number)
        if model.max_turn == 0:
            return await view.no_start(message)
        
        if 150 > (model.total_count[system_id] - number) > 57:
            model.bot_move, model.sequence = model.first_move()
        elif 30 <= (model.total_count[system_id] - number) < 57:
            model.bot_move = model.total_count[system_id] - number - 30
            if model.bot_move == 0:
                model.bot_move = 1
        elif 1 < (model.total_count[system_id] - number) < 30:
            x = 1
            model.bot_move = model.total_count[system_id] - number - 1
            if model.bot_move == 0:
                model.bot_move = 1
        
        
        if number <= 0:
            await view.cheat(message)
        elif number >= 29:
            await view.cheat(message)
        elif model.total_count[system_id] == 0:
            await view.end_game(message)
        elif number < model.total_count[system_id] and number + model.bot_move >= model.total_count[system_id]:
            await view.bot_lose(message)
            model.total_count[system_id] = 0
        elif 0 < number < 29 and model.total_count[system_id] > number:
            model.total_count[system_id] = model.total_count[system_id] - model.bot_move - number
            if x == 0:
                await view.work_space(message, number, model.bot_move,  model.total_count[system_id])
            elif x == 1:
                await view.work_space_lose(message, number, model.bot_move,  model.total_count[system_id])
        elif model.total_count[system_id] == number:
            model.total_count[system_id] = model.total_count[system_id] - number
            await view.lose(message)
            model.total_count[system_id] = 0
        elif model.total_count[system_id] < number:
            await view.lacks(message)
    except:
        await view.except_message(message)