import controller
import model
import view


x = 'y'
while x == 'y':
    model.init_full()
    while controller.fragmentation() == '/0':
        model.full_string = ''
        model.init_full()
        
    controller.fragmentation()
    view.print_total_str()
    x = input('Введите символ (y)(Англ. Игрек) если хотите ввести новую строку и любой другой если не хотите: ')





