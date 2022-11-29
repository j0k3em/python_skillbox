count_of_number = int(input("Введите кол-во клеток: "))
cells = []
for queue in range(count_of_number):
    print("Эффективность", queue + 1, "клетки:", end = "" )
    efficiency = int(input())
    cells.append(efficiency)
print("Неподходящие значение: ", end = "")
for i in range(count_of_number):
    if i > cells[i]:
        print(cells[i], end = " ")