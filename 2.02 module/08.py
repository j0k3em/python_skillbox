number_list = [1, 4, -3, 0, 10]
result = []
finish = len(number_list)
start = 3
for i in range(finish - start, finish):
    result.append(number_list[i])
for i in range(0, finish - start):
    result.append(number_list[i])
print("Сдвиг: ", start)
print("Старый список", number_list)
print("Новый список", result)