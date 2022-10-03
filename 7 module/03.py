bank = 0
for month in range(12):
    salary = int(input('Введите зарплату: '))
    bank += salary
average = bank / 12
print('Средняя зарплата за год =', average)