a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def min_num(a, b):
    return int((a + b - abs(a - b)) / 2)

print(min_num(a, b))