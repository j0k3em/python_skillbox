first_list = []
second_list = []

for num_one in range(3):
    print(f'Введите число {num_one + 1}:', end = " ")
    num_one_in = int(input(""))
    first_list.append(num_one_in)

for num_two in range(7):
    print(f'Введите число {num_two + 1}:', end = " ")
    num_two_in = int(input(""))
    second_list.append(num_two_in)

print("Первый список: ", first_list)
print("Второй список: ", second_list)

first_list.extend(second_list)
for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)

print("Новый первый список с уникальными элементами: ", first_list)