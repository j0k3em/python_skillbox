hours = int(input('Введите отработанные часов: '))
loanBalance = int(input('Введите остаток по кредиту: '))
foodMoney = int(input('Введите траты на еду: '))
salary = 200 * hours / 2 ** 3 + hours
if loanBalance + foodMoney <= salary:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')
