base_famaly = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидорова", "Павел"): 10,
    ("Жевлокова", "Вика"): 3,
    ("Жевлокова", "Саша"): 27,
    ("Жевлоков", "Павел"): 25
}

lastname = input("Введите фамилию: ")

for key in base_famaly:
    length = len(lastname)
    length_lastname = len(key[0])
    if lastname.lower() == key[0][0:length].lower() or \
            lastname[0:length_lastname].lower() == key[0].lower():
        print(key[0], key[1], base_famaly[key])