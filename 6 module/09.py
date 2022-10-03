number = int(input('Введите загадываемое число: '))
attempt = 0
while True:
	print('Введите число: ')
	son_number = int(input())
	if son_number > number:
		print('Число больше, чем нужно. Попробуйте ещё раз!')
		attempt += 1
	elif son_number < number:
		print('Число меньше, чем нужно. Попробуйте ещё раз!')
		attempt += 1
	else: 
		print('Вы угадали! Число попыток:', attempt)
		break
