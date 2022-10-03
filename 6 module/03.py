number = int(input('Введите число: '))
i = 1
while number // 10 != 0:
	i += 1
	number = number // 10
print('Число ', number, ' имеет ', i, ' цифр(у).')