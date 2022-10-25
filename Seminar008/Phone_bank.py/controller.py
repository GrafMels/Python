import view, model

def start():
    while True:
        comand = view.show_menu()
        match comand:
            case '0':
                exit()
            case '1':
                view.show_contacts(model.get_contacts())
            case '2':
                model.read_file()
            case '3':
                model.save_file()
            case '4':
                model.add_contact()
            case '5':
                model.change_contact()
            case '6':
                model.delete_contact()
            case '7':
                model.seach_contact()