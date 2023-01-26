import module
import view


def click_button():
    action = 0
    while action != 8:
        action = view.start_menu()
        match action:
            case 1:  # открыть файл
                view.print_info(module.open_file())

            case 2:  # сохранить файл
                message = module.check_file()
                if message == "":
                    module.save_file()
                    message = "Файл сохранен"
                view.print_info(message)

            case 3:  # показать все контакты
                message = module.check_file()
                if message == "":
                    phone_b = module.get_phone_book()
                    view.show_contact(phone_b)
                print(message)

            case 4:  # создать контакт
                message = module.check_file()
                if message == "" or message == "Телефонная книга пуста":
                    new_contact = list(view.create_contact())
                    module.add_contact(new_contact)
                    message = "Новый контакт создан"
                view.print_info(message)

            case 5:  # удалить контакт
                message = module.check_file()
                if message == "":
                    phone_b = module.get_phone_book()
                    view.show_contact(phone_b)
                    mes = "Выберите контакт для удаления: "
                    num_contact = view.input_number_contact(phone_b, mes)
                    module.del_contact(num_contact)
                    message = "Контакт удален"
                view.print_info(message)

            case 6:  # изменить контакт
                message = module.check_file()
                if message == "":
                    phone_b = module.get_phone_book()
                    view.show_contact(phone_b)
                    mes = "Выберите контакт для изменения: "
                    num_contact = view.input_number_contact(phone_b, mes)
                    contact = module.get_contact(num_contact)
                    сorrect_contact = view.change_contact(contact)
                    module.change_contact(сorrect_contact, num_contact)
                    message = "Контакт изменен"
                view.print_info(message)

            case 7:  # найти контакт
                message = module.check_file()
                if message == "":
                    search = view.search_contact()
                    search_contact = module.find_contact(search)
                    if not search_contact:
                        view.print_info("Контакт не найден")
                    else:
                        view.show_contact(search_contact)
                else:
                    view.print_info(message)

    view.print_info("Работа программы завершена")
