ticket = int(input('Введите номер билета: '))
sum = 0
i = 0
while i < 6:
	if i < 3:
		sum += ticket % 10
		ticket = ticket // 10
		i += 1
	else:
		sum -= ticket % 10
		ticket = ticket // 10
		i += 1

if sum == 0:
	print('Билет счастливый')
else:
	print('Билет не счастливый')