guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answer = ""
while answer != "Пора спать":
    print(f"Сейчас на веченике {len(guests)} человек", guests)
    answer = input("Гость пришел или ушел? ")
    if answer != "Пора спать":
        name = input("Имя гостя: ")
    if answer == "ушел":
        print(f"Пока, {name}!")
        guests.remove(name)
    if len(guests) >= 6:
        print(f"прости {name}, но мест нет")
    else:
        if answer == "пришел":
            print(f"Привет {name}!")
            guests.append(name)

print("Вечеринка закончилась, все легли спать.")