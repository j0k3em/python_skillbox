x = int(input('Введите сумму вклада: '))
y = int(input('Введите процент: '))
z = int(input('Введите цель: '))
i = 0
while x < z:
	x += x * y // 100
	i += 1
print('Через', i, ' лет.')