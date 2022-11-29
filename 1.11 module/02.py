import math
count = int(input('Введите кол-во чисел: '))
i = 1
while i <= count:
	number = float(input('Введите число:'))
	if number > 0:
		number = math.ceil(number)
		print(math.log(number))
	elif number < 0:
		number = math.floor(number)
		print(math.exp(number))
	i += 1