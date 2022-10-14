# from tkinter import *
# from functools import partial
# import random
# root = Tk()
# root.title('Игра Баше́')
# game_run = True
# field = []
# cross_count = 0

# def new_game():
#     for row in range(3):
#         for col in range(3):
#             field[row][col]['text'] = ''
#             field[row][col]['background'] = 'lavender'
#     global game_run
#     game_run = True
#     global cross_count
#     cross_count = 0

# def one_move (my_rolls, rolls, enemy_rools):
#     my_move = '{}0'.format(new_entry_input.get())
    
#     rolls -= int(my_move)
#     my_rolls += int(my_move)
#     enemy_move = random.randint(1, 29)
#     rolls -= enemy_move
#     enemy_rools += enemy_move
#     return my_rolls, rolls, enemy_rools
    
# my_rolls = 0
# rolls = 280
# enemy_rools = 0

# new_entry_input = Entry(root, width=10) 
# new_entry_input.grid(row=1, column=1, columnspan=1, sticky='nsew')

# while(rolls>28):
#     my_rolls, rolls, enemy_rools = one_move(my_rolls, rolls, enemy_rools)


#     for row in range(1):
#         line = []
#         for col in range(3):
#             if col == 0:
#                 button = Button(root, text=f'Ваши камни:\n{my_rolls}', width=20, height=2, 
#                                 font=('Verdana', 10, ''),
#                                 background='lavender')
#                 button.grid(row=row, column=col, sticky='nsew')
#                 line.append(button)
#             elif col == 1:
#                 button = Button(root, text=f'Общие камни:\n{rolls}', width=20, height=2, 
#                                 font=('Verdana', 10, ''),
#                                 background='lavender')
#                 button.grid(row=row, column=col, sticky='nsew')
#                 line.append(button)
#             elif col == 2:
#                 button = Button(root, text=f'Вражеские камни:\n{enemy_rools}', width=20, height=2, 
#                                 font=('Verdana', 10, ''),
#                                 background='lavender')
#                 button.grid(row=row, column=col, sticky='nsew')
#                 line.append(button)
            
#         field.append(line)
#     new_button = Button(root, text='Начать игру', command=new_game)

#     new_button2 = Button(root, text='Сходить', command=partial(one_move,my_rolls,rolls,enemy_rools))
#     new_button.grid(row=1, column=0, columnspan=1, sticky='nsew')

#     new_button2.grid(row=1, column=2, columnspan=1, sticky='nsew')
#     if rolls>28:
#         continue
#     root.mainloop()




