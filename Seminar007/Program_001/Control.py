import View
import Multi
import Summ
import Diff
import Div
import Log

def button_click():
    value_a = View.getValue() # Метод получения значений из view
    oeration_name = View.get_operation_name()
    value_b = View.getValue()
    
    result = get_operation(value_a, value_b, oeration_name) # Инициализируем входные данные нашей модели
    # result = model.sum() 
    # result = model.mult()  # Поменяли функцию sum на mult
    View.View(result, oeration_name, value_a, value_b) # возвращаем результат и имя операции
    Log.Log(result, oeration_name, value_a, value_b)

def get_operation(num1, num2, operation_name):
    match operation_name:
        case '+':
            Summ.init(num1, num2)
            return Summ.operation(num1, num2)
        case '-':
            Diff.init(num1, num2)
            return Diff.operation(num1, num2)
        case '*':
            Multi.init(num1, num2)
            return Multi.operation(num1, num2)
        case '/':
            Div.init(num1, num2)
            return Div.operation(num1, num2)

    
