skates = []
peoples = []

count_skates = int(input("Кол-во коньков: "))
for num_skate in range(count_skates):
    print(f"Размер {num_skate + 1} пары: ", end = " ")
    skate = int(input(""))
    skates.append(skate)
print()

count_people = int(input("Кол-во людей:  "))
for num_people in range(count_people):
    print(f"Размер {num_people + 1} пары: ", end = " ")
    people = int(input(""))
    peoples.append(people)

result = 0
for i_skates in skates:
    for i_people in range(len(peoples)):
        if peoples[i_people] == i_skates:
            i_skates = 0
            result += 1

print()
print("Наибольшее кол-во людей, которые могут взять ролики: " ,result)