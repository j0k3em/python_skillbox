
friends = int(input("Кол-во друзей: "))
notes = int(input("Долговых расписок: "))
print()

friends_list = []
for number in range(friends):
    friends_list.append([number, 0])

for ex_num in range(notes):
    print(f"{ex_num + 1} расписка")
    take = int(input("Кому: "))
    given = int(input("От кого: "))
    how_many = int(input("Сколько "))
    friends_list[take - 1][1] -= how_many
    friends_list[given - 1][1] += how_many
    print()
    print("Баланс друзей:")
    for i in range(friends):
        print(f"{(friends_list[i][0]) + 1} : {friends_list[i][1]}")
