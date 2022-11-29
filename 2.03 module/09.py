
friends = int(input("Кол-во друзей: "))
ex = int(input("Долговых расписок: "))
print()

friends_list = []
for number in range(friends):
    friends_list.append([number, 0])

for ex_num in range(ex):
    print(f"{ex_num + 1} расписка")
    take = int(input("Кому: "))
    give = int(input("От кого: "))
    how_many = int(input("Сколько "))
    friends_list[take - 1][1] -= how_many
    friends_list[give - 1][1] += how_many
    print()
    print("Баланс друзей:")
    for index in range(friends):
        print(f"{(friends_list[index][0]) + 1} : {friends_list[index][1]}")
