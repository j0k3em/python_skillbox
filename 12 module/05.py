text = input('Введите текст: ')
K = input('Какую цифру ищем? ')
N = input('Какую букву ищём? ')

def count_letters(text, K, N):
    symb = list(text)
    count_K = 0
    count_N = 0
    for elem in symb:
        if elem == N:
            count_N += 1
        if elem == K:
            count_K += 1
    return count_N, count_K

count_N, count_K = count_letters(text, K, N)
print('Количество цифр', K + ':', count_K)
print('Количество букв', N + ':', count_N)