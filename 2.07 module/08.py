def add_contact(contacts):
    name_surname = input("Введите имя и фамилию через пробел: ").split()
    while len(name_surname) != 2:
        name_surname = input("Введите имя и фамилию через пробел: ").split()
    phone_number = int(input("Введите номер телефона: "))
    phone_books[contacts] = {
        "name": name_surname[0],
        "surname": name_surname[1],
        "phone_number": phone_number
    }
    contacts += 1
    print("Всего контактов - {0}:".format(contacts))
    for key, value in phone_books.items():
        print("     ", value["surname"], value["name"], value["phone_number"])
    return contacts


def seach_contact(dict):
    input_surname = input("Введите Фамилию для поиска: ").lower()
    for key, value in dict.items():
        if str(value["surname"]).lower() == input_surname:
            print(value["surname"], value["name"], value["phone_number"])


contacts = 0
phone_books = dict()
while True:
    answer = input("Добавить контакт - 1, "
                   "Функция поиска - 2")
    if answer == "1":
        contacts = add_contact(contacts)
    if answer == "2":
        seach_contact(phone_books)