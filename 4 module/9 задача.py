miliage = int(input('Введите пробег: '))
numberOfDay = int(input('Введите сегодняшнее число:  '))
a = miliage % 10
b = miliage // 10 % 10
c = miliage // 100 % 10
sum = a + b + c
if sum > numberOfDay:
    print('Сброс')
    miliage = 0
    print('Пробег:', miliage)
else:
    print('Сегодня не сломался')
    print('Пробег:', miliage)
