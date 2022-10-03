people = int(input('Введите количество должников: '))
general = 0
for duty_people in range(0, people + 1, 5):
	print('Должник с номером', duty_people)
	print('Сколько должны?')
	duty = int(input())
	general += duty
print('Общая сумма долга:', general)