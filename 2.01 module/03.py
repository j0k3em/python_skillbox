N = int(input('Введите число: '))
def summ_N (N):
    summ = 0
    while N > 0:
        summ += N % 10
        N //= 10
    return summ

def count_N(N):
    count = 0
    while N > 0:
        N //= 10
        count += 1
    return count

print('Сумма цифр в числе', N, '=', summ_N(N))
print('Количество символов в числе', N, '=', count_N(N))
