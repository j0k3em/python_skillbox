hour = int(input('Введите время в часах: '))
if 8 <= hour < 10 or 12 <= hour < 14 or 15 <= hour < 18 or 20 <= hour < 22:
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')
