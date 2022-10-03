n = int(input('Введите число: '))
def min_del(n):
    i = 1
    while i <= n:
        i += 1
        if n % i == 0:
            print('Наименьший делитель, отличный от единицы:', i)
            break

min_del(n)
