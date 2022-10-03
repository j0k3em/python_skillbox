three = 0
four = 0
five = 0
N = int(input('Введите количество человек: '))
for people in range(1, N + 1):
    mark = int(input('Введите оценку: '))
    if mark == 3:
        three += 1
    elif mark == 4:
        four += 1
    else:
        five += 1
if three > four and three > five:
    print('Троечников больше')
elif four > three and four > five:
    print('Хорошистов больше')
else:
    print('Отличников больше')