path = 'phone_book.txt'
contacts = []

def read_file():
    global contacts
    with open (path, encoding='utf_8') as file:
       contacts = [i.strip().split('; ')for i in file.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts
    new_contact = []
    new_contact.append(str(len(contacts)+1))
    new_contact.append(input('Введите name: '))
    new_contact.append(input('Введите phone: '))
    new_contact.append(input('Введите комментарий: '))
    contacts.append(new_contact)

def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as file:
        for i in range(len(contacts)):
            if i == 0:
                file.write(f'{contacts[i][0]}; {contacts[i][1]}; {contacts[i][2]}; {contacts[i][3]}')
            else:
                file.write(f'\n{contacts[i][0]}; {contacts[i][1]}; {contacts[i][2]}; {contacts[i][3]}')
                
def change_contact():
    global contacts
    id_change_contact = int(input('Введите id контакта который хотите изменить: '))
    change_contact = []
    change_contact.append(str(id_change_contact))
    change_contact.append(input('Введите name: '))
    change_contact.append(input('Введите phone: '))
    change_contact.append(input('Введите комментарий: '))
    contacts[id_change_contact-1] = change_contact
    
def delete_contact():
    global contacts
    id_dict = [int(i[0]) for i in contacts].pop()
    id_delete_contact = int(input('Введите id удаляемого контакта: '))-1
    contacts.pop(id_delete_contact)
    for i in range(len(contacts)):
        contacts[i][0] = i+1

def seach_contact():
    global contacts
    id_dict = [int(i[0]) for i in contacts].pop()
    id_delete_contact = int(input('Введите id удаляемого контакта: '))-1
    contacts.pop(id_delete_contact)
    for i in range(len(contacts)):
        contacts[i][0] = i+1
    



    