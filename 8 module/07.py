educational_grant = int(input('Стипендия:'))
expenses = int(input('Проживание:'))
money = expenses
for month in range(2, 11):
	money += expenses * 1.03
	expenses = expenses * 1.03
print(money - educational_grant * 10)