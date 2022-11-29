first_line = input("Первая строка: ")
second_line = input("Вторая строка: ")

final_line = []
finish = len(first_line)
shift = abs(first_line.find(first_line[0]) - second_line.find(first_line[0]))

for i in range(finish - shift, finish):
    final_line.append(first_line[i])
for i in range(0, finish - shift):
    final_line.append(first_line[i])
result = ("".join(final_line))

if result == second_line:
    print(f"Первая строка получается из второй со сдвигом {shift}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")