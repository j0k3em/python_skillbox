length = int(input("Введите длину списка: "))
list_nums = list(range(length))
result_list = [num % 5 if list_nums.index(num) % 2 != 0
               else 1 for num in list_nums]
print("Результат:", result_list)