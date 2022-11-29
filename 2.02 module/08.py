number_list = [1, 4, -3, 0, 10]
result = []
finish = len(number_list)
start = 3
for index in range(finish - start, finish):
    result.append(number_list[index])
for index in range(0, finish - start):
    result.append(number_list[index])
print("Сдвиг: ", start)
print("Старый список", number_list)
print("Новый список", result)