income = int(input('Введите доход: '))
tax = 0
if income > 50000:
    tax = 0.3 * (income - 50000) + 0.2 * (50000 - 10000) + 0.13 * 10000
elif 10000 < income <= 50000:
    tax = 0.2 * (income - 10000) + 0.13 * 10000
else:
    tax = 0.13 * income
print('Сумма налога равна:', tax)
