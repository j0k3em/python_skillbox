numberOfDay = int(input('Введите число месяца: '))
lastSymbol = numberOfDay % 10
if lastSymbol % 2 == 0:
    print('Сегодня нужно использовать зубную нить!')
