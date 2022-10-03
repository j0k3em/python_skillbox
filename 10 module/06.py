N = int(input('Введите число: '))
summ = 0
answer = 1
for number in range(1, N + 1):
    answer *= number
    summ += answer
print('Сумма факториалов числа', N, 'равна', summ)