def show_menu():
    question = '\n1 - Показать все контакты\
\n2 - Открыть файл с контактами\
\n3 - Записать файл с контактами\
\n4 - Добавить контакт\
\n5 - Изменить контакт\
\n6 - Удалить контакт\
\n7 - Поиск по контактам\
\n0 - Выход из программы\
\nВведите необходимую команду: '
    comand = input(question)
    return comand

def show_contacts(contacts: list):
    [print(contact) for contact in contacts]