a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
count = 0
summ = 0
for number in range(a, b + 1):
    if number % 3 == 0:
        count += 1
        summ += number
average = summ / count
print('Среднее арифметическое чисел кратных 3 =', average)