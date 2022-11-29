number = int(input('Введите натуральное число: '))
x = 1
for n in range(1, number + 1):
    x = ((-1) ** n) / (2 ** n)
print(x)