players = int(input("Кол-во человек: "))
number_game = int(input("Какое число в считалке? "))
print(f"Значит выбывает каждый {number_game} человек")
print()

players_list = list(range(1, players + 1))

while len(players_list) > 1:
    print("Текущий круг людей:", players_list)
    begin_number = int(input("Начало счёта с номера "))
    count = players_list.index(begin_number)
    for _ in range(number_game):
        count += 1
        if count == len(players_list):
            count = 0
    print("Выбывает игрок под номером", players_list[count - 1])
    players_list.remove(players_list[count - 1])
    print()

print("Остался человек под номером", players_list[0])