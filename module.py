phone_book = []
flag_pb_opened = False
path = 'baza.txt'


def check_file():
    global phone_book
    global flag_pb_opened
    if flag_pb_opened:
        if len(phone_book) < 1:
            message = "Телефонная книга пуста"
        else:
            message = ''
    else:
        message = "Телефонная книга не открыта"
    return message


def open_file():
    global phone_book
    global path
    global flag_pb_opened
    if not flag_pb_opened:
        with open(path, 'r', encoding="UTF-8") as data:
            file = data.readlines()
        for value in file:
            phone_book.append(value.strip().split(';'))
        flag_pb_opened = True
        message= "Файл открыт"
    else:
        message = "Файл был открыт ранее"
    return message


def get_phone_book():
    global phone_book
    return phone_book


def get_contact(index: int):
    global phone_book
    return phone_book[index]


def save_file():
    global phone_book
    global path
    pb_str = []
    for i in phone_book:
        pb_str.append(";".join(i))
    pb_str = "\n".join(pb_str)
    with open(path, 'w', encoding="UTF-8") as data:
        data.write(pb_str)


def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)


def find_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for item in contact:
            if find in item:
                result.append(contact)
                break
    # if len(result) == 0:
    #     result.append("Контакт не найден")
    return result


def delete_contact():
    print(0)


def change_contact(cor_contact: list, num_contact: int):
    global phone_book
    phone_book[num_contact] = cor_contact


def del_contact(index: int):
    global phone_book
    del phone_book[index]
