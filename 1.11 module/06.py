print('Ввод: ')
start = int(input('Нижняя граница: '))
stop = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('Вывод: ')
print ('C', ' F','\n')
for count in range (start, stop, step):
	result = round(count * 1.8 + 32)
	print (count,' ',result)
	if count + step > stop:
		count = stop
	result = round(count * 1.8 + 32)
	print (count,' ',result)