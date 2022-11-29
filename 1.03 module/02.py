firstQuarter = int(input('Введите сумму за первый квартал: '))
secondQuarter = int(input('Введите сумму за второй квартал: '))
thirdQuarter = int(input('Введите сумму за третий квартал: '))
fourthQuarter = int(input('Введите сумму за четвёртый квартал: '))
firstHalf = firstQuarter + secondQuarter
secondHalf = thirdQuarter + fourthQuarter
res = firstHalf / secondHalf
print(res)
