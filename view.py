commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def print_info(info):
    print("***")
    print(info)
    print("***")


def start_menu():
    global commands
    print("Главное меню: ")
    for i in range(len(commands)):
        print(f"{i + 1}. {commands[i]}")
    res = input("Выберете пункт меню: ")
    while not (res.isdigit()) or (int(res) < 1 or int(res) > 9):
        print_info("Некорректный пункт меню")
        res = input("Выберете пункт меню: ")
    res = int(res)
    return res


def show_contact(phone_list: list):
        for i, contact in enumerate(phone_list):
            print(f"\t{i + 1}. {contact[0]:35} {contact[1]:15} {contact[2]:20}")



def create_contact():
    name = input("Введите ФИО: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    return (name, phone, comment)


def search_contact(message="Введите искомый контакт: "):
    search = input(message)
    return search


def input_number_contact(phone_b: list, mess="Введите номер контакта: "):
    number = " "
    flag = 0
    while not number.isdigit() or (int(number) > len(phone_b) or int(number) < 1):
        if flag != 0:
            print("Некорректный запрос")
        number = input(mess)
        flag += 1
    number = int(number) - 1
    return number


def change_contact(contact: list):
    name = contact[0]
    phone = contact[1]
    comment = contact[2]
    atrubute = ""
    i = 0
    while not atrubute.isdigit():
        if i != 0:
            print("Некорректный запрос!")
        print("\n 1. ФИО\n 2. Телефон\n 3. Комментарий\n 4. Все")
        atrubute = input('Выберете поля, которые будем измененять: ')
        if atrubute == "1":
            name = input("Введите исправленные ФИО: ")
        elif atrubute == "2":
            phone = input("Введите исправленный телефона: ")
        elif atrubute == "3":
            comment = input("Введите комментарий: ")
        elif atrubute == "4":
            name = input("Введите исправленные ФИО: ")
            phone = input("Введите исправленный телефона: ")
            comment = input("Введите комментарий: ")
        else:
            print("Некорректное значение. Введите число от 1 до 4")
        i += 1
    return [name, phone, comment]
