number = int(input('Введите загадываемое число: '))
N = 50
top = 100
bottom = 0
while True:
    print('Твоё число равно, меньше или больше, чем число', N, '?')
    answer = int(input())
    if answer == 2:
        bottom = N
        N = top - (top - N) // 2
    elif answer == 3:
        top = N
        N = bottom + (N - bottom) // 2
    else:
        print('Ваше число', N)
        break
