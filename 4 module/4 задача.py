firstPrice = int(input('Введите первую сумму: '))
secondPrice = int(input('Введите вторую сумму: '))
thirdPrice = int(input('Введите третью сумму: '))
sum = firstPrice + secondPrice + thirdPrice
if sum > 10000:
    sum /= 10
print('Окончательная сумма', sum)
