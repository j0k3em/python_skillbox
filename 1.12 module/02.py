def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def test():
    N = int(input('Введите число: '))
    if N > 0:
        positive()
    else:
        negative()

test()