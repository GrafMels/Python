# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint

total_count = []
user_id_list = []
max_turn = 0

def user_id_seach(user_id):
    try: 
        return user_id_list.index(user_id)
    except:
        total_count.append(150)
        user_id_list.append(user_id)
        return user_id_list.index(user_id)
        
def first_move():
    bot_move = randint(1, 28)
    sequence = randint(0, 1)
    return bot_move, sequence

bot_move = 0
sequence = 0

class working_condition(StatesGroup):
    waiting_for_input = State()
    stop_Bot = State()
    repeat_Bot = State()

angry_bot = 0