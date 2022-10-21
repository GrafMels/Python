import controller


full_string = 0
start_string = 0


def init_full():
    global full_string
    global start_string
    full_string = controller.input_string('Введите строку: ')
    start_string = full_string

