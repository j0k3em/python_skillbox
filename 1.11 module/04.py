import math

x = float(input('Введите действительное положительное число: '))
y = x * 10
y = math.trunc(y)
print(y % 10)