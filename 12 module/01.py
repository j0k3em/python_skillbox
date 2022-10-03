def summa_n(N):
    sum_n = 0
    for i in range(N + 1):
        sum_n += i
    print('Я знаю, что сумма чисел от 1 до', N, 'равна', sum_n)

N = int(input('Введите число: '))
summa_n(N)