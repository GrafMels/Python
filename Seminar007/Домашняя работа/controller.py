import logger
import model
import view

def input_string(enter):
    a = input(enter)
    return a

def fragmentation(): 
    model.full_string = str(model.full_string).replace('-',' - ').replace('+',' + ')
    if(model.full_string[-1])=='*' or (model.full_string[-1])=='/' or (model.full_string[-1])=='+' or (model.full_string[-1])=='-':
        view.error_value()
    list_string = model.full_string.split()

    for i in range(len(list_string)):
        if list_string[i].find('*') != -1 and list_string[i].find('/') != -1:
            temp_str = list_string[i]
            temp_list = temp_str.replace('*',' * ').replace('/',' / ').split()
            temp_var = 0
            count = 0
            for j in range(len(temp_list)):
                if temp_list[j] == '*' and count == 0:
                    temp_var = int(temp_list[j-1]) * int(temp_list[j+1])
                    count+=1
                elif temp_list[j] == '/' and count == 0:
                    if int(temp_list[j+1]) == 0:
                        view.dev_by_zero()
                        return '/0'
                    temp_var = int(temp_list[j-1]) / int(temp_list[j+1])
                    if temp_var == int(temp_var):
                        temp_var = int(temp_var)
                        count+=1
                elif temp_list[j] == '*' and count != 0:
                    temp_var *= int(temp_list[j+1])
                elif temp_list[j] == '/' and count != 0:
                    if int(temp_list[j+1]) == 0:
                        view.dev_by_zero()
                        return '/0'
                    temp_var /= int(temp_list[j+1])
                    if temp_var == int(temp_var):
                        temp_var = int(temp_var)
            list_string[i] = str(temp_var)    
        elif list_string[i].find('*') != -1:
            temp_str = list_string[i]
            temp_list = temp_str.replace('*',' * ').split()
            temp_var = 0
            for j in range(len(temp_list)):
                if temp_list[j]=='*':
                    temp_var = int(temp_list[j-1]) * int(temp_list[j+1])
            
            list_string[i] = str(temp_var)
            
        elif list_string[i].find('/') != -1:
            temp_str = list_string[i]
            temp_list = temp_str.replace('/',' / ').split()
            temp_var = 0
            for j in range(len(temp_list)):
                if temp_list[j]=='/':
                    if int(temp_list[j+1]) == 0:
                        view.dev_by_zero()
                        return '/0'
                    temp_var = int(temp_list[j-1]) / int(temp_list[j+1])
                    if temp_var == int(temp_var):
                        temp_var = int(temp_var)
            list_string[i] = str(temp_var)      
                     
    model.full_string = ''.join(list_string)
    model.full_string = model.full_string.replace('-',' -').replace('+',' +')
    list_string = model.full_string.split()
    
    temp_var = 0
    for i in range(len(list_string)):
        temp_var += float(list_string[i])
    logger.logger(f'{model.start_string}={temp_var}')
    model.full_string = temp_var
