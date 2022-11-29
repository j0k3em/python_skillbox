def nod (a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    nod = a + b
    return nod

print('Наибольший общий делитель равен:', nod(a = int(input('Введите первое число: ')), b = int(input('Введите второе число: '))))