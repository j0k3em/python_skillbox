plus = 0
minus = 0
while True:
	number = int(input('Введите число: '))
	if number > 0:
		plus += 1
	if number < 0: 
		minus += 1
	if number == 0:
		print('Кол-во положительных чисел: ', plus)
		print('Кол-во отрицательных чисел: ', minus)
		break
