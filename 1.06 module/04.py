even = 0
while True:
	num = int(input('Введите число: '))
	if num == 0:
		print(even)
		break
	if num % 2 == 0:
		even += 1